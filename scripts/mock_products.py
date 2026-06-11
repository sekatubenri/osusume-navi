"""Amazon PA API が使えない間のモック商品データ"""

MOCK_PRODUCTS = {
    "家電・カメラ": [
        {"asin": "B0CX4KQBFR", "title": "Anker PowerCore 10000 モバイルバッテリー 10000mAh", "brand": "Anker", "price": "¥2,990", "star_rating": 4.5, "review_count": 28431, "features": ["コンパクトサイズで持ち運びやすい", "USB-C対応、高速充電", "スマホ約2回分の充電が可能"], "image_url": "https://m.media-amazon.com/images/I/51YuLKTahZL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B0CX4KQBFR?tag=ASSOCIATE_TAG"},
        {"asin": "B09KMBNPQ8", "title": "Echo Dot 第5世代 - スマートスピーカー with Alexa", "brand": "Amazon", "price": "¥5,980", "star_rating": 4.4, "review_count": 15023, "features": ["音質が大幅に向上", "スマートホームデバイスのハブとして機能", "Alexa搭載で音声操作が快適"], "image_url": "https://m.media-amazon.com/images/I/61S6O5DPJVL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B09KMBNPQ8?tag=ASSOCIATE_TAG"},
        {"asin": "B09B8YWXDF", "title": "Kindle Paperwhite 第11世代 防水機能搭載 8GB", "brand": "Amazon", "price": "¥14,980", "star_rating": 4.6, "review_count": 9872, "features": ["6.8インチ大画面で読みやすい", "防水仕様でお風呂でも読める", "1回充電で最大10週間使用可能"], "image_url": "https://m.media-amazon.com/images/I/61Key1bGq9L._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B09B8YWXDF?tag=ASSOCIATE_TAG"},
        {"asin": "B08L5TNJHG", "title": "Fire TV Stick 4K Max ストリーミングメディアプレーヤー", "brand": "Amazon", "price": "¥9,980", "star_rating": 4.5, "review_count": 12540, "features": ["4K Ultra HD・Dolby Vision対応", "Wi-Fi 6対応で高速ストリーミング", "Alexa対応リモコン付属"], "image_url": "https://m.media-amazon.com/images/I/51TjBuNTsbL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B08L5TNJHG?tag=ASSOCIATE_TAG"},
        {"asin": "B09G9FPHY6", "title": "TP-Link WiFi 無線LAN ルーター AX3000 Wi-Fi6対応", "brand": "TP-Link", "price": "¥7,999", "star_rating": 4.3, "review_count": 6754, "features": ["Wi-Fi 6対応で高速・安定通信", "最大3000Mbpsの高速通信", "簡単セットアップでスマホから設定可能"], "image_url": "https://m.media-amazon.com/images/I/51P5FEFbunL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B09G9FPHY6?tag=ASSOCIATE_TAG"},
    ],
    "ゲーム": [
        {"asin": "B0CJGNLMZQ", "title": "Nintendo Switch 本体 (ニンテンドースイッチ) Joy-Con(L)/(R) ネオンブルー/ネオンレッド", "brand": "Nintendo", "price": "¥32,978", "star_rating": 4.7, "review_count": 45231, "features": ["TVモード・携帯モード・テーブルモードの3スタイル", "豊富なタイトルが揃う人気ゲーム機", "家族みんなで楽しめるマルチプレイ対応"], "image_url": "https://m.media-amazon.com/images/I/61-PblYntsL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B0CJGNLMZQ?tag=ASSOCIATE_TAG"},
        {"asin": "B0C1P9Y9WT", "title": "PlayStation 5 デジタル・エディション (CFI-2000B01)", "brand": "Sony", "price": "¥59,980", "star_rating": 4.6, "review_count": 8932, "features": ["超高速SSDで快適なゲーム体験", "4K・120fps対応の高画質", "DualSenseのハプティックフィードバックで没入感アップ"], "image_url": "https://m.media-amazon.com/images/I/41YRxY9NRRL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B0C1P9Y9WT?tag=ASSOCIATE_TAG"},
        {"asin": "B09VV6MW3T", "title": "マリオカート8 デラックス -Switch", "brand": "Nintendo", "price": "¥5,909", "star_rating": 4.8, "review_count": 23109, "features": ["最大8人でオンライン対戦が楽しめる", "48コース収録の大ボリューム", "全年齢が楽しめる王道レースゲーム"], "image_url": "https://m.media-amazon.com/images/I/81O7bJ0HSSL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B09VV6MW3T?tag=ASSOCIATE_TAG"},
        {"asin": "B0BG2BQNGT", "title": "VALORANT ポイントカード 1000VP", "brand": "Riot Games", "price": "¥1,100", "star_rating": 4.2, "review_count": 3421, "features": ["人気FPSゲームのポイントカード", "スキンやエージェント購入に使える", "コード配信で即利用可能"], "image_url": "https://m.media-amazon.com/images/I/71VJD0RMPVL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B0BG2BQNGT?tag=ASSOCIATE_TAG"},
        {"asin": "B0CGS4HFXY", "title": "ゼルダの伝説 ティアーズ オブ ザ キングダム -Switch", "brand": "Nintendo", "price": "¥6,578", "star_rating": 4.8, "review_count": 18754, "features": ["広大なハイラルを自由に冒険", "独創的なスクラビルドシステム", "やりこみ要素満載の超大作RPG"], "image_url": "https://m.media-amazon.com/images/I/81IUbm3BPHL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B0CGS4HFXY?tag=ASSOCIATE_TAG"},
    ],
    "キッチン・日用品": [
        {"asin": "B07WHVTM9T", "title": "象印 電気圧力鍋 2.8L ブラック EL-MB30-BA", "brand": "象印", "price": "¥14,800", "star_rating": 4.3, "review_count": 7823, "features": ["ほったらかし調理でラクラク", "圧力調理・無水調理など多機能", "内鍋はフッ素加工で洗いやすい"], "image_url": "https://m.media-amazon.com/images/I/51P6fxe+g+L._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B07WHVTM9T?tag=ASSOCIATE_TAG"},
        {"asin": "B08CZHGW3H", "title": "バルミューダ The Toaster トースター スチームトースター", "brand": "BALMUDA", "price": "¥24,200", "star_rating": 4.4, "review_count": 5432, "features": ["スチーム技術で外はサクサク中はふわふわ", "おしゃれなデザインでキッチンのインテリアに", "トースト・チーズトースト・ピザなど5つのモード"], "image_url": "https://m.media-amazon.com/images/I/41cg8BFQPPL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B08CZHGW3H?tag=ASSOCIATE_TAG"},
        {"asin": "B09NQKND1C", "title": "アイリスオーヤマ 衣類スチーマー ハンディスチーマー", "brand": "アイリスオーヤマ", "price": "¥3,480", "star_rating": 4.1, "review_count": 12034, "features": ["約30秒で使用可能なスピード加熱", "ハンガーにかけたまましわ伸ばし可能", "軽量コンパクトで収納場所を取らない"], "image_url": "https://m.media-amazon.com/images/I/51M9sTFePFL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B09NQKND1C?tag=ASSOCIATE_TAG"},
        {"asin": "B0899N7KXQ", "title": "山崎実業 tower マグネット冷蔵庫サイドテーブル", "brand": "山崎実業", "price": "¥3,520", "star_rating": 4.4, "review_count": 8921, "features": ["マグネットで冷蔵庫側面に設置", "スマートフォン・調理器具などを置ける", "シンプルなデザインでどんなキッチンにも合う"], "image_url": "https://m.media-amazon.com/images/I/51d+aSajOOL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B0899N7KXQ?tag=ASSOCIATE_TAG"},
        {"asin": "B0862W23J5", "title": "ダイソン Dyson V8 Slim Fluffy コードレス掃除機", "brand": "Dyson", "price": "¥44,800", "star_rating": 4.5, "review_count": 6231, "features": ["軽量設計でリビングから階段まで楽に掃除", "強力な吸引力でゴミをしっかりキャッチ", "後処理が簡単な衛生的なゴミ捨て機能"], "image_url": "https://m.media-amazon.com/images/I/41HBs8wuTQL._AC_SL1000_.jpg", "url": f"https://www.amazon.co.jp/dp/B0862W23J5?tag=ASSOCIATE_TAG"},
    ],
}


def get_mock_products(category_name: str, associate_tag: str) -> list[dict]:
    """カテゴリ名に対応するモック商品リストを返す（URLのタグを置換）"""
    import random
    # カテゴリが見つからない場合は家電データを使用
    products = MOCK_PRODUCTS.get(category_name, MOCK_PRODUCTS["家電・カメラ"])
    result = []
    for p in products:
        item = p.copy()
        item["url"] = item["url"].replace("ASSOCIATE_TAG", associate_tag or "yourstore-22")
        result.append(item)
    random.shuffle(result)
    return result[:5]
