"""Amazon Product Advertising API 5.0 — ベストセラー商品取得"""

import hashlib
import hmac
import json
import datetime
import requests
from config import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG

SERVICE  = "ProductAdvertisingAPI"
REGION   = "us-west-2"
HOST     = "webservices.amazon.co.jp"
ENDPOINT = f"https://{HOST}/paapi5"


def _sign(key: bytes, msg: str) -> bytes:
    return hmac.new(key, msg.encode(), hashlib.sha256).digest()


def _signing_key(secret: str, date: str) -> bytes:
    k = _sign(("AWS4" + secret).encode(), date)
    k = _sign(k, REGION)
    k = _sign(k, SERVICE)
    return _sign(k, "aws4_request")


def _call(operation: str, payload: dict) -> dict:
    now       = datetime.datetime.utcnow()
    amz_date  = now.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = now.strftime("%Y%m%d")
    target    = f"com.amazon.paapi5.v1.ProductAdvertisingAPIv1.{operation}"
    body      = json.dumps(payload)
    body_hash = hashlib.sha256(body.encode()).hexdigest()

    canonical = "\n".join([
        "POST",
        f"/paapi5/{operation.lower()}",
        "",
        f"content-encoding:amz-1.0\ncontent-type:application/json; charset=utf-8\nhost:{HOST}\nx-amz-date:{amz_date}\nx-amz-target:{target}\n",
        "content-encoding;content-type;host;x-amz-date;x-amz-target",
        body_hash,
    ])

    scope      = f"{date_stamp}/{REGION}/{SERVICE}/aws4_request"
    sts        = "\n".join(["AWS4-HMAC-SHA256", amz_date, scope, hashlib.sha256(canonical.encode()).hexdigest()])
    sig        = hmac.new(_signing_key(AMAZON_SECRET_KEY, date_stamp), sts.encode(), hashlib.sha256).hexdigest()
    auth       = f"AWS4-HMAC-SHA256 Credential={AMAZON_ACCESS_KEY}/{scope}, SignedHeaders=content-encoding;content-type;host;x-amz-date;x-amz-target, Signature={sig}"

    resp = requests.post(
        f"{ENDPOINT}/{operation.lower()}",
        headers={
            "content-encoding": "amz-1.0",
            "content-type": "application/json; charset=utf-8",
            "host": HOST,
            "x-amz-date": amz_date,
            "x-amz-target": target,
            "Authorization": auth,
        },
        data=body,
        timeout=15,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"PA API {resp.status_code}: {resp.text[:300]}")
    return resp.json()


def _parse_item(item: dict) -> dict:
    info    = item.get("ItemInfo", {})
    offers  = item.get("Offers", {}).get("Listings", [{}])
    price   = offers[0].get("Price", {}) if offers else {}
    images  = item.get("Images", {}).get("Primary", {}).get("Large", {})
    reviews = item.get("CustomerReviews", {})
    feats   = info.get("Features", {}).get("DisplayValues", [])

    return {
        "asin":         item.get("ASIN", ""),
        "url":          item.get("DetailPageURL", ""),
        "title":        info.get("Title", {}).get("DisplayValue", ""),
        "brand":        info.get("ByLineInfo", {}).get("Brand", {}).get("DisplayValue", ""),
        "features":     [f.get("DisplayValue", "") for f in feats[:4]],
        "price":        price.get("DisplayAmount", "価格未定"),
        "image_url":    images.get("URL", ""),
        "review_count": reviews.get("Count", 0),
        "star_rating":  reviews.get("StarRating", {}).get("Value", 0),
    }


def get_best_sellers(node_id: str, count: int = 5) -> list[dict]:
    """指定BrowseNodeのベストセラー商品を取得"""
    data = _call("SearchItems", {
        "PartnerTag":   AMAZON_ASSOCIATE_TAG,
        "PartnerType":  "Associates",
        "Marketplace":  "www.amazon.co.jp",
        "BrowseNodeId": node_id,
        "SortBy":       "AvgCustomerReviews",
        "ItemCount":    count,
        "Resources": [
            "ItemInfo.Title", "ItemInfo.ByLineInfo", "ItemInfo.Features",
            "Offers.Listings.Price", "Images.Primary.Large",
            "CustomerReviews.Count", "CustomerReviews.StarRating",
        ],
    })
    return [_parse_item(i) for i in data.get("SearchResult", {}).get("Items", [])]
