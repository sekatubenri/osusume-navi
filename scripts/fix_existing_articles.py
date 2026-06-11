"""
既存の記事を一括修正するスクリプト
- 旧式の商品カード（画像付き）→ 新式のテキストカードに置換
- /dp/ASIN リンク → /s?k=商品名 検索リンクに変換（リンク切れ防止）
- frontmatter の image: → カテゴリ別サムネイルに更新
"""

import re
import urllib.parse
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "content" / "posts"
TAG = "mirainikibouw-22"

CATEGORY_THUMBS = {
    "家電・カメラ":         "https://placehold.co/800x400/2C3E50/FFF?text=Electronics",
    "ゲーム":               "https://placehold.co/800x400/8E44AD/FFF?text=Gaming",
    "キッチン・日用品":     "https://placehold.co/800x400/E67E22/FFF?text=Kitchen",
    "おもちゃ・ホビー":     "https://placehold.co/800x400/E74C3C/FFF?text=Hobby",
    "スポーツ・アウトドア": "https://placehold.co/800x400/27AE60/FFF?text=Sports",
    "ファッション":         "https://placehold.co/800x400/2980B9/FFF?text=Fashion",
    "ビューティー":         "https://placehold.co/800x400/E91E8C/FFF?text=Beauty",
    "食品・飲料":           "https://placehold.co/800x400/795548/FFF?text=Food",
    "ペット用品":           "https://placehold.co/800x400/009688/FFF?text=Pets",
}

# 旧商品カードのパターン
OLD_CARD_RE = re.compile(
    r'<div class="product-card">'
    r'<a href="([^"]+)" target="_blank" rel="nofollow noopener">'
    r'<img [^>]*alt="([^"]*)"[^>]*>'
    r'<div class="product-card-info">'
    r'<span class="product-title">([^<]*)</span>'
    r'<span class="product-price">([^<]*)</span>'
    r'<span class="product-rating">★([0-9.]+) \(([0-9,]+)件のレビュー\)</span>'
    r'<span class="cta-button">Amazonで見る →</span>'
    r'</div></a></div>'
)


def build_new_card(title: str, price: str, rating: str, review_count: str) -> str:
    search_url = f"https://www.amazon.co.jp/s?k={urllib.parse.quote(title)}&tag={TAG}"
    return (
        f'<div class="product-card">'
        f'<div class="product-card-header">'
        f'<span class="product-badge">Amazonおすすめ</span>'
        f'<span class="product-rating">&#9733;{rating}（{review_count}件のレビュー）</span>'
        f'</div>'
        f'<p class="product-title">{title}</p>'
        f'<div class="product-price-row">'
        f'<span class="product-price">{price}</span>'
        f'</div>'
        f'<a href="{search_url}" class="cta-button-full" target="_blank" rel="nofollow noopener">'
        f'Amazonで見る &#x2192;'
        f'</a>'
        f'</div>'
    )


def get_category_thumb(content: str) -> str:
    m = re.search(r'categories:\s*\n\s*-\s*"([^"]+)"', content)
    if m:
        return CATEGORY_THUMBS.get(m.group(1), CATEGORY_THUMBS["家電・カメラ"])
    return CATEGORY_THUMBS["家電・カメラ"]


def fix_article(filepath: Path) -> bool:
    text = filepath.read_text(encoding="utf-8")
    original = text

    # 1. frontmatter の image: を更新
    thumb = get_category_thumb(text)
    text = re.sub(
        r'^image: ".*"',
        f'image: "{thumb}"',
        text,
        flags=re.MULTILINE,
    )

    # 2. 旧商品カードを新カードに置換
    def replace_card(m):
        # group(2) or group(3) = title, group(4) = price, group(5) = rating, group(6) = review_count
        title        = m.group(2) or m.group(3)
        price        = m.group(4)
        rating       = m.group(5)
        review_count = m.group(6)
        return build_new_card(title, price, rating, review_count)

    text = OLD_CARD_RE.sub(replace_card, text)

    if text != original:
        filepath.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    md_files = sorted(POSTS_DIR.glob("*.md"))
    fixed = 0
    skipped = 0
    for f in md_files:
        if f.name == "welcome.md":
            continue
        if fix_article(f):
            print(f"  修正: {f.name[:70]}")
            fixed += 1
        else:
            skipped += 1

    print(f"\n完了: {fixed}件修正, {skipped}件スキップ（変更なし）")


if __name__ == "__main__":
    main()
