import os
from dotenv import load_dotenv

load_dotenv()

AMAZON_ACCESS_KEY  = os.getenv("AMAZON_ACCESS_KEY")
AMAZON_SECRET_KEY  = os.getenv("AMAZON_SECRET_KEY")
AMAZON_ASSOCIATE_TAG = os.getenv("AMAZON_ASSOCIATE_TAG")
AMAZON_MARKETPLACE = os.getenv("AMAZON_MARKETPLACE", "www.amazon.co.jp")

ANTHROPIC_API_KEY  = os.getenv("ANTHROPIC_API_KEY")

ARTICLES_PER_DAY   = int(os.getenv("ARTICLES_PER_DAY", "3"))

# 記事を生成するカテゴリー（BrowseNode IDはamazon.co.jp基準）
CATEGORIES = [
    {"name": "家電・カメラ",         "node_id": "3210981"},
    {"name": "本・雑誌",             "node_id": "465392"},
    {"name": "ゲーム",               "node_id": "637394"},
    {"name": "おもちゃ・ホビー",     "node_id": "13299531"},
    {"name": "キッチン・日用品",     "node_id": "3828871"},
    {"name": "ファッション",         "node_id": "352484011"},
    {"name": "スポーツ・アウトドア", "node_id": "14304371"},
    {"name": "ビューティー",         "node_id": "370470011"},
    {"name": "食品・飲料",           "node_id": "2277721051"},
    {"name": "ペット用品",           "node_id": "2492760051"},
]
