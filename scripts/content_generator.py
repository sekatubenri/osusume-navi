"""Claude API で商品紹介記事を生成し、Hugoマークダウンを返す"""

import json
import datetime
import anthropic
from config import ANTHROPIC_API_KEY

CURRENT_YEAR = datetime.date.today().year

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

PROMPT = """
あなたはAmazonアフィリエイトブログのプロライターです。
以下の商品情報をもとに、読者が購入したくなる魅力的な日本語記事を書いてください。

【現在の年】{year}年
【カテゴリ】{category}
【商品一覧】
{products_text}

## 記事の要件
- 文字数: 1500〜2500文字
- 構成:
  1. 導入部（読者の悩みに共感する100〜200文字）
  2. 各商品の詳細紹介（それぞれ200〜300文字、特徴・メリット・おすすめポイント）
  3. まとめ（どんな人にどの商品が向くかを整理）
- 語調: フレンドリーで親しみやすく
- 各商品紹介に「価格」「評価」を自然に組み込む
- 各商品の紹介箇所に `[PRODUCT_CARD_ASIN]` を1回挿入（ASINを実際の値に置き換え）
- HTML形式で出力（h2, h3, p, ul, li, strong タグを使用）
- 冒頭に必ず: <p class="affiliate-disclosure">※本記事にはアフィリエイト広告が含まれています。</p>
- タイトルには必ず「{year}年」を含めること（例:「{year}年最新！{category}おすすめランキングTOP5」）

## 出力形式（必ずこのJSONのみを返すこと）
{{
  "title": "SEO最適化された記事タイトル（{year}年を含めること）",
  "description": "記事の概要（150文字以内）",
  "content": "HTML形式の本文",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"]
}}
"""


def _products_text(products: list[dict]) -> str:
    lines = []
    for i, p in enumerate(products, 1):
        feats = "\n  - ".join(p["features"][:3]) if p["features"] else "なし"
        lines.append(
            f"{i}. {p['title']}\n"
            f"   ASIN: {p['asin']}\n"
            f"   価格: {p['price']}\n"
            f"   評価: ★{p['star_rating']} ({p['review_count']}件)\n"
            f"   ブランド: {p['brand']}\n"
            f"   特徴:\n  - {feats}"
        )
    return "\n\n".join(lines)


CATEGORY_THUMBS = {
    "家電・カメラ":     "https://placehold.co/800x400/2C3E50/FFF?text=Electronics",
    "ゲーム":           "https://placehold.co/800x400/8E44AD/FFF?text=Gaming",
    "キッチン・日用品": "https://placehold.co/800x400/E67E22/FFF?text=Kitchen",
    "おもちゃ・ホビー": "https://placehold.co/800x400/E74C3C/FFF?text=Hobby",
    "スポーツ・アウトドア": "https://placehold.co/800x400/27AE60/FFF?text=Sports",
    "ファッション":     "https://placehold.co/800x400/2980B9/FFF?text=Fashion",
    "ビューティー":     "https://placehold.co/800x400/E91E8C/FFF?text=Beauty",
    "食品・飲料":       "https://placehold.co/800x400/795548/FFF?text=Food",
    "ペット用品":       "https://placehold.co/800x400/009688/FFF?text=Pets",
}


def _build_product_card(p: dict) -> str:
    features_html = "".join(f"<li>{f}</li>" for f in p.get("features", [])[:3])
    review_count  = f"{p['review_count']:,}" if isinstance(p.get("review_count"), int) else p.get("review_count", "")
    return (
        f'<div class="product-card">'
        f'<div class="product-card-header">'
        f'<span class="product-badge">Amazonおすすめ</span>'
        f'<span class="product-rating">&#9733;{p["star_rating"]}&#xFF08;{review_count}件のレビュー&#xFF09;</span>'
        f'</div>'
        f'<p class="product-title">{p["title"]}</p>'
        f'<div class="product-price-row">'
        f'<span class="product-price">{p["price"]}</span>'
        f'<span class="product-brand">{p.get("brand", "")}</span>'
        f'</div>'
        f'<ul class="product-features-list">{features_html}</ul>'
        f'<a href="{p["url"]}" class="cta-button-full" target="_blank" rel="nofollow noopener">'
        f'Amazon&#x3067;&#x898B;&#x308B; &#x2192;'
        f'</a>'
        f'</div>'
    )


def generate_article(category: str, products: list[dict]) -> dict:
    """記事を生成してHugo用dictを返す"""
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": PROMPT.format(
                year=CURRENT_YEAR,
                category=category,
                products_text=_products_text(products),
            ),
        }],
    )

    raw = msg.content[0].text.strip()
    if "```json" in raw:
        raw = raw.split("```json")[1].split("```")[0].strip()
    elif "```" in raw:
        raw = raw.split("```")[1].split("```")[0].strip()

    article = json.loads(raw)

    # プレースホルダーを商品カードHTMLに置換
    content = article["content"]
    for p in products:
        content = content.replace(f"[PRODUCT_CARD_{p['asin']}]", _build_product_card(p))

    article["content"] = content
    article["image"]   = CATEGORY_THUMBS.get(category, "https://placehold.co/800x400/FF9900/FFF?text=Amazon")
    return article
