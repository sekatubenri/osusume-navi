"""Claude API で商品紹介記事を生成し、Hugoマークダウンを返す"""

import json
import anthropic
from config import ANTHROPIC_API_KEY

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

PROMPT = """
あなたはAmazonアフィリエイトブログのプロライターです。
以下の商品情報をもとに、読者が購入したくなる魅力的な日本語記事を書いてください。

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

## 出力形式（必ずこのJSONのみを返すこと）
{{
  "title": "SEO最適化された記事タイトル",
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


def _build_product_card(p: dict) -> str:
    return (
        f'<div class="product-card">'
        f'<a href="{p["url"]}" target="_blank" rel="nofollow noopener">'
        f'<img src="{p["image_url"]}" alt="{p["title"]}" loading="lazy">'
        f'<div class="product-card-info">'
        f'<span class="product-title">{p["title"]}</span>'
        f'<span class="product-price">{p["price"]}</span>'
        f'<span class="product-rating">★{p["star_rating"]} ({p["review_count"]}件のレビュー)</span>'
        f'<span class="cta-button">Amazonで見る →</span>'
        f'</div></a></div>'
    )


def generate_article(category: str, products: list[dict]) -> dict:
    """記事を生成してHugo用dictを返す"""
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": PROMPT.format(
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
    article["image"]   = products[0]["image_url"] if products else ""
    return article
