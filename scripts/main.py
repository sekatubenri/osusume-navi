"""
メイン処理: Amazon → Claude → Hugoマークダウンファイルを生成する
MOCK_MODE=true の場合はダミー商品データを使用（PA API不要）
"""

import os
import json
import logging
import datetime
import re
from pathlib import Path

from config import CATEGORIES, ARTICLES_PER_DAY
from content_generator import generate_article

MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("affiliate_bot.log", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)

STATE_FILE  = Path("state.json")
CONTENT_DIR = Path(__file__).parent.parent / "content" / "posts"


def _load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"category_index": 0, "posted_today": 0, "last_date": ""}


def _save_state(s: dict) -> None:
    STATE_FILE.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")


def _slug(title: str, date: str) -> str:
    clean = re.sub(r"[^\w　-鿿]", "-", title)
    clean = re.sub(r"-+", "-", clean).strip("-")[:60]
    return f"{date}-{clean}"


def _write_markdown(article: dict, category: str, date_str: str) -> Path:
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    slug     = _slug(article["title"], date_str)
    filepath = CONTENT_DIR / f"{slug}.md"
    tags_yaml = "\n".join(f'  - "{t}"' for t in article.get("tags", []))
    frontmatter = f"""---
title: "{article['title'].replace('"', '\\"')}"
date: "{date_str}T07:00:00+09:00"
description: "{article['description'].replace('"', '\\"')}"
categories:
  - "{category}"
tags:
{tags_yaml}
image: "{article.get('image', '')}"
---
"""
    filepath.write_text(frontmatter + "\n" + article["content"], encoding="utf-8")
    return filepath


def _get_products(category: dict) -> list[dict]:
    if MOCK_MODE:
        from mock_products import get_mock_products
        log.info("[MOCK] ダミー商品データを使用")
        return get_mock_products(category["name"], os.getenv("AMAZON_ASSOCIATE_TAG", "yourstore-22"))
    from amazon_api import get_best_sellers
    return get_best_sellers(category["node_id"], count=5)


def run() -> None:
    today = datetime.date.today().isoformat()
    state = _load_state()

    if state["last_date"] != today:
        state["posted_today"] = 0
        state["last_date"]    = today

    if state["posted_today"] >= ARTICLES_PER_DAY:
        log.info("本日の投稿数上限(%d)に達しました。", ARTICLES_PER_DAY)
        return

    remaining = ARTICLES_PER_DAY - state["posted_today"]
    log.info("生成予定記事数: %d", remaining)

    for _ in range(remaining):
        idx      = state["category_index"] % len(CATEGORIES)
        category = CATEGORIES[idx]

        log.info("[%s] 商品データ取得中...", category["name"])
        try:
            products = _get_products(category)
            if not products:
                log.warning("商品が取得できませんでした: %s", category["name"])
                state["category_index"] += 1
                continue

            log.info("商品%d件取得。記事生成中...", len(products))
            article  = generate_article(category["name"], products)
            filepath = _write_markdown(article, category["name"], today)

            log.info("マークダウン生成完了: %s", filepath.name)
            state["posted_today"]   += 1
            state["category_index"] += 1
            _save_state(state)

        except Exception as e:
            log.error("エラー: %s", e, exc_info=True)
            state["category_index"] += 1
            _save_state(state)

    log.info("完了。本日の生成数: %d", state["posted_today"])


if __name__ == "__main__":
    run()
