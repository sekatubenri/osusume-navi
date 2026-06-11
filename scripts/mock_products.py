"""Amazon PA API が使えない間のモック商品データ（実 ASIN + Amazon ウィジェット画像）"""


def _amz_img(asin: str) -> str:
    """Amazon 公式ウィジェットで実際の商品写真を返す"""
    return (
        f"https://ws-fe.amazon-adsystem.com/widgets/q"
        f"?_encoding=UTF8&MarketPlace=JP&ASIN={asin}"
        f"&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL300_"
    )


MOCK_PRODUCTS = {
    "家電・カメラ": [
        {"asin": "B081YPQPXH", "title": "Anker PowerCore Slim 10000 モバイルバッテリー",         "brand": "Anker",   "price": "¥2,990",  "star_rating": 4.5, "review_count": 28431, "features": ["コンパクトサイズで持ち運びやすい", "USB-C対応・高速充電", "スマホ約2回分充電可能"],        "image_url": _amz_img("B081YPQPXH")},
        {"asin": "B09B8SZLLG", "title": "Echo Dot 第5世代 スマートスピーカー with Alexa",        "brand": "Amazon",  "price": "¥5,980",  "star_rating": 4.4, "review_count": 15023, "features": ["音質が大幅に向上", "スマートホームのハブとして機能", "Alexa搭載で音声操作が快適"],    "image_url": _amz_img("B09B8SZLLG")},
        {"asin": "B09S3KZK4N", "title": "Kindle Paperwhite 第11世代 防水機能搭載 8GB",          "brand": "Amazon",  "price": "¥14,980", "star_rating": 4.6, "review_count": 9872,  "features": ["6.8インチ大画面で読みやすい", "防水仕様でお風呂でも読める", "1回充電で最大10週間使用可能"], "image_url": _amz_img("B09S3KZK4N")},
        {"asin": "B0BW37QY2V", "title": "Fire TV Stick 4K Max ストリーミングメディアプレーヤー", "brand": "Amazon",  "price": "¥9,980",  "star_rating": 4.5, "review_count": 12540, "features": ["4K Ultra HD・Dolby Vision対応", "Wi-Fi 6対応で高速ストリーミング", "Alexa対応リモコン付属"], "image_url": _amz_img("B0BW37QY2V")},
        {"asin": "B08H4PZGZS", "title": "TP-Link WiFi 無線LAN ルーター AX3000 Wi-Fi6対応",     "brand": "TP-Link", "price": "¥7,999",  "star_rating": 4.3, "review_count": 6754,  "features": ["Wi-Fi 6対応で高速・安定通信", "最大3000Mbps", "簡単セットアップでスマホから設定可能"], "image_url": _amz_img("B08H4PZGZS")},
    ],
    "ゲーム": [
        {"asin": "B098RL6SLQ", "title": "Nintendo Switch 有機ELモデル Joy-Con ホワイト",           "brand": "Nintendo", "price": "¥37,980", "star_rating": 4.7, "review_count": 45231, "features": ["7インチ有機ELディスプレイで鮮やかな映像", "TVモード・携帯モード・テーブルモードの3スタイル", "有線LANポート内蔵でオンラインプレイが安定"], "image_url": _amz_img("B098RL6SLQ")},
        {"asin": "B0CFZS9J4B", "title": "PlayStation 5 デジタル・エディション（薄型）",          "brand": "Sony",     "price": "¥59,980", "star_rating": 4.6, "review_count": 8932,  "features": ["超高速SSDで快適なゲーム体験", "4K・120fps対応の高画質", "DualSenseのハプティックフィードバックで没入感アップ"], "image_url": _amz_img("B0CFZS9J4B")},
        {"asin": "B01N12G06K", "title": "マリオカート8 デラックス -Switch",                      "brand": "Nintendo", "price": "¥5,909",  "star_rating": 4.8, "review_count": 23109, "features": ["最大8人でオンライン対戦が楽しめる", "48コース収録の大ボリューム", "全年齢が楽しめる王道レースゲーム"], "image_url": _amz_img("B01N12G06K")},
        {"asin": "B0BV94KXFR", "title": "ゼルダの伝説 ティアーズ オブ ザ キングダム -Switch",    "brand": "Nintendo", "price": "¥6,578",  "star_rating": 4.8, "review_count": 18754, "features": ["広大なハイラルを自由に冒険", "独創的なスクラビルドシステム", "やりこみ要素満載の超大作RPG"], "image_url": _amz_img("B0BV94KXFR")},
        {"asin": "B084HPGQ9W", "title": "あつまれ どうぶつの森 -Switch",                         "brand": "Nintendo", "price": "¥5,273",  "star_rating": 4.7, "review_count": 35621, "features": ["自分だけの島を自由に開発", "家族や友人とのんびり楽しめる", "季節のイベントが毎月充実"], "image_url": _amz_img("B084HPGQ9W")},
    ],
    "キッチン・日用品": [
        {"asin": "B07WFYWW5K", "title": "象印 電気圧力鍋 2.8L EL-MB30-HA",                     "brand": "象印",         "price": "¥14,800", "star_rating": 4.3, "review_count": 7823,  "features": ["ほったらかし調理でラクラク", "圧力調理・無水調理など多機能", "内鍋はフッ素加工で洗いやすい"], "image_url": _amz_img("B07WFYWW5K")},
        {"asin": "B08HCTTL8B", "title": "バルミューダ The Toaster スチームトースター K05A-BK",  "brand": "BALMUDA",      "price": "¥24,200", "star_rating": 4.4, "review_count": 5432,  "features": ["スチーム技術で外サクサク中ふわふわ", "おしゃれなデザイン", "トースト・チーズトースト・ピザなど5モード"], "image_url": _amz_img("B08HCTTL8B")},
        {"asin": "B08TPHXG68", "title": "アイリスオーヤマ 衣類スチーマー ハンディスチーマー NIS-200", "brand": "アイリスオーヤマ", "price": "¥3,480", "star_rating": 4.1, "review_count": 12034, "features": ["約30秒で使用可能なスピード加熱", "ハンガーにかけたまましわ伸ばし可能", "軽量コンパクトで収納場所不要"], "image_url": _amz_img("B08TPHXG68")},
        {"asin": "B09VQVXGV1", "title": "ダイソン Dyson V8 Slim Fluffy コードレス掃除機",       "brand": "Dyson",        "price": "¥44,800", "star_rating": 4.5, "review_count": 6231,  "features": ["軽量設計でリビングから階段まで楽に掃除", "強力な吸引力でゴミをしっかりキャッチ", "衛生的なゴミ捨て機能"], "image_url": _amz_img("B09VQVXGV1")},
        {"asin": "B07MQRJ3VK", "title": "山崎実業 tower マグネット冷蔵庫サイドテーブル ホワイト", "brand": "山崎実業",    "price": "¥3,520",  "star_rating": 4.4, "review_count": 8921,  "features": ["マグネットで冷蔵庫側面に設置", "スマートフォン・調理器具を置ける", "シンプルなデザインでどんなキッチンにも合う"], "image_url": _amz_img("B07MQRJ3VK")},
    ],
    "おもちゃ・ホビー": [
        {"asin": "B09KN33J7Y", "title": "レゴ LEGO クラシック 黄色のアイデアボックス 10696",   "brand": "LEGO",         "price": "¥3,630",  "star_rating": 4.7, "review_count": 14532, "features": ["484ピース入りで自由に組み立て", "4歳から楽しめる入門セット", "想像力・創造力を育む"], "image_url": _amz_img("B09KN33J7Y")},
        {"asin": "B09Q67M7X5", "title": "タカラトミー プラレール N700S 確認試験車セット",       "brand": "タカラトミー", "price": "¥4,980",  "star_rating": 4.6, "review_count": 9871,  "features": ["新幹線車両と基本レールセット", "男の子に大人気の定番おもちゃ", "拡張パーツで大きなレイアウトも可能"], "image_url": _amz_img("B09Q67M7X5")},
        {"asin": "B00LYW27UI", "title": "バンダイ RG 1/144 RX-78-2 ガンダム プラモデル",        "brand": "バンダイ",     "price": "¥2,200",  "star_rating": 4.8, "review_count": 21045, "features": ["リアルグレードの精密な作り", "色分け済みパーツで塗装不要", "大人も楽しめるプレミアム品質"], "image_url": _amz_img("B00LYW27UI")},
        {"asin": "B00SFTJGRK", "title": "任天堂 amiibo マリオ (スーパーマリオシリーズ)",        "brand": "Nintendo",     "price": "¥1,320",  "star_rating": 4.6, "review_count": 8732,  "features": ["対応ゲームで特典を解放できる", "インテリアとしても飾れる高品質フィギュア", "コレクション性が高い"], "image_url": _amz_img("B00SFTJGRK")},
        {"asin": "B07CYHBGMZ", "title": "メガハウス ルービックキューブ 3×3 ver.3.0",           "brand": "メガハウス",   "price": "¥1,540",  "star_rating": 4.5, "review_count": 11234, "features": ["世界中で愛される知育パズル", "スムーズな回転で快適プレイ", "大人から子供まで楽しめる"], "image_url": _amz_img("B07CYHBGMZ")},
    ],
    "スポーツ・アウトドア": [
        {"asin": "B009HBLSRO", "title": "コールマン テント ツーリングドーム ST 2人用",          "brand": "Coleman",   "price": "¥13,980", "star_rating": 4.4, "review_count": 8934,  "features": ["設営が簡単な吊り下げ式インナー", "前室が広く荷物を置けるスペースあり", "ソロ〜2人でのキャンプに最適"], "image_url": _amz_img("B009HBLSRO")},
        {"asin": "B09QK35JX5", "title": "ナイキ ランニングシューズ Air Zoom Pegasus 39",      "brand": "Nike",      "price": "¥14,300", "star_rating": 4.5, "review_count": 15678, "features": ["クッション性が高く長距離も快適", "通気性の良いメッシュアッパー", "初心者から上級者まで対応"], "image_url": _amz_img("B09QK35JX5")},
        {"asin": "B07NHKJ6WZ", "title": "FIELDOOR ハンモック 自立式スタンド付き 200cm",        "brand": "FIELDOOR",  "price": "¥9,980",  "star_rating": 4.3, "review_count": 6541,  "features": ["自立式スタンドで木がなくても設置可能", "耐荷重200kgの安心設計", "室内・屋外両方で使える"], "image_url": _amz_img("B07NHKJ6WZ")},
        {"asin": "B00A2GF2UK", "title": "ヨネックス バドミントンラケット セット CB-10",        "brand": "YONEX",     "price": "¥4,290",  "star_rating": 4.4, "review_count": 7823,  "features": ["ラケット2本・シャトル3個のお得なセット", "初心者でも扱いやすい軽量設計", "家族・友人と気軽に楽しめる"], "image_url": _amz_img("B00A2GF2UK")},
        {"asin": "B09B5Z5YNL", "title": "HUMMER 折りたたみ自転車 20インチ 6段変速",            "brand": "HUMMER",    "price": "¥19,800", "star_rating": 4.2, "review_count": 4532,  "features": ["コンパクトに折りたためる", "通勤・通学・レジャーに活躍", "6段変速機能付きで坂道も快適"], "image_url": _amz_img("B09B5Z5YNL")},
    ],
    "ファッション": [
        {"asin": "B09NCJRVBR", "title": "ユニクロ ヒートテック エクストラウォーム タートルネックT 極暖", "brand": "UNIQLO",           "price": "¥1,990",  "star_rating": 4.6, "review_count": 32145, "features": ["極暖素材で寒い冬も快適", "タートルネックで首元もあったか", "インナーとしても普段着としても使える"], "image_url": _amz_img("B09NCJRVBR")},
        {"asin": "B092T4VSJF", "title": "無印良品 足なり直角靴下 婦人・三足組",               "brand": "MUJI",             "price": "¥990",    "star_rating": 4.5, "review_count": 18923, "features": ["かかとがズレない直角設計", "肌に優しい綿素材", "3足セットでお買い得"], "image_url": _amz_img("B092T4VSJF")},
        {"asin": "B000FTMKWY", "title": "アディダス スタンスミス スニーカー メンズ",            "brand": "adidas",           "price": "¥13,200", "star_rating": 4.6, "review_count": 25431, "features": ["シンプルで合わせやすいデザイン", "カジュアルからきれいめコーデまで対応", "クッション性が高く長時間歩いても疲れない"], "image_url": _amz_img("B000FTMKWY")},
        {"asin": "B0BJR1XYVR", "title": "コロンビア バガブー インターチェンジ 防水 ジャケット", "brand": "Columbia",         "price": "¥16,500", "star_rating": 4.5, "review_count": 12034, "features": ["高い防水性能で雨の日も安心", "インナー付き2WAY仕様", "アウトドア・通勤どちらにも対応"], "image_url": _amz_img("B0BJR1XYVR")},
        {"asin": "B07ZGJJZ5P", "title": "サマンサタバサ レディース トートバッグ シンプル",      "brand": "Samantha Thavasa", "price": "¥8,800",  "star_rating": 4.3, "review_count": 5612,  "features": ["A4サイズが入る大容量", "軽量素材で肩が疲れにくい", "通勤・お出かけに使いやすいデザイン"], "image_url": _amz_img("B07ZGJJZ5P")},
    ],
    "ビューティー": [
        {"asin": "B0B72LXVV5", "title": "パナソニック ヘアドライヤー ナノケア EH-NA0J-W",       "brand": "Panasonic", "price": "¥22,000", "star_rating": 4.6, "review_count": 14532, "features": ["ナノイーで髪のうるおいを保つ", "速乾性が高く時間を節約", "くせ毛もしっかりまとまる"], "image_url": _amz_img("B0B72LXVV5")},
        {"asin": "B0BXHQXBPX", "title": "資生堂 マキアージュ ドラマティックスキンセンサーベース UV SPF50+", "brand": "SHISEIDO", "price": "¥2,420", "star_rating": 4.4, "review_count": 8921, "features": ["SPF50+・PA++++の高い紫外線対策", "皮脂・テカリを長時間防ぐ", "化粧もちが格段にアップ"], "image_url": _amz_img("B0BXHQXBPX")},
        {"asin": "B09Q3CYK6Q", "title": "花王 ビオレ UV アクアリッチ ウォータリーエッセンス SPF50+", "brand": "花王",    "price": "¥1,045",  "star_rating": 4.5, "review_count": 21043, "features": ["SPF50+・PA++++の最高レベル", "水のようにさらっとしたテクスチャー", "コスパ最強の定番日焼け止め"], "image_url": _amz_img("B09Q3CYK6Q")},
        {"asin": "B07BV3SCXX", "title": "コーセー 雪肌精 化粧水 500ml 大容量ボトル",           "brand": "KOSE",      "price": "¥2,530",  "star_rating": 4.5, "review_count": 9872,  "features": ["透明感のある肌へ導く美白化粧水", "ベタつかず肌なじみが良い", "500mlの大容量でコスパ抜群"], "image_url": _amz_img("B07BV3SCXX")},
        {"asin": "B07P8T7HZT", "title": "カネボウ SALA ヘアオイル まとまりスムース 60ml",      "brand": "Kanebo",    "price": "¥968",    "star_rating": 4.3, "review_count": 7654,  "features": ["アウトバストリートメントとして使いやすい", "まとまりのあるサラサラ髪に", "プチプラで毎日使いやすい"], "image_url": _amz_img("B07P8T7HZT")},
    ],
    "食品・飲料": [
        {"asin": "B0DGGGHQF6", "title": "UCC 職人の珈琲 ドリップコーヒー まろやかマイルドブレンド 54袋", "brand": "UCC",         "price": "¥1,180",  "star_rating": 4.5, "review_count": 18432, "features": ["一杯ずつ新鮮に淹れられるドリップ式", "54袋入りのお得なまとめ買い", "コクと香りのバランスが良い"], "image_url": _amz_img("B0DGGGHQF6")},
        {"asin": "B07MZGNTDP", "title": "カルビー ポテトチップス うすしお味 60g×24袋",          "brand": "Calbee",      "price": "¥2,354",  "star_rating": 4.6, "review_count": 25431, "features": ["定番の味で家族全員に人気", "24袋の箱買いでストックに便利", "パーティーやおやつに最適"], "image_url": _amz_img("B07MZGNTDP")},
        {"asin": "B017K1NJFE", "title": "伊藤園 お〜いお茶 緑茶 2L×9本",                        "brand": "伊藤園",      "price": "¥1,296",  "star_rating": 4.6, "review_count": 32145, "features": ["毎日飲みたい定番のお茶", "2Lの大容量でコスパ抜群", "無香料・無添加の本格緑茶"], "image_url": _amz_img("B017K1NJFE")},
        {"asin": "B07KQWJ6ZN", "title": "明治 ザバス ホエイプロテイン100 バニラ味 1050g",       "brand": "Meiji",       "price": "¥5,980",  "star_rating": 4.5, "review_count": 14532, "features": ["吸収が早いホエイプロテイン", "飲みやすいバニラ味", "1050gの大容量でコスパ良好"], "image_url": _amz_img("B07KQWJ6ZN")},
        {"asin": "B09D3CZWYB", "title": "ハウス食品 バーモントカレー 甘口 230g×10個",           "brand": "House Foods", "price": "¥2,200",  "star_rating": 4.7, "review_count": 19876, "features": ["子供から大人まで人気の定番カレー", "10個まとめ買いでストックに便利", "りんごとはちみつの優しい甘さ"], "image_url": _amz_img("B09D3CZWYB")},
    ],
    "ペット用品": [
        {"asin": "B0DR9BXLNW", "title": "ロイヤルカナン 猫用 インドア 成猫用 2kg",              "brand": "Royal Canin",    "price": "¥4,580",  "star_rating": 4.6, "review_count": 8921,  "features": ["室内飼い猫に最適な栄養バランス", "毛玉ケアに配慮したフォーミュラ", "獣医師も推奨する信頼のブランド"], "image_url": _amz_img("B0DR9BXLNW")},
        {"asin": "B098JVTFKC", "title": "コンボ 犬用おやつ 国産とりむね肉 14袋セット",          "brand": "COMBO",          "price": "¥980",    "star_rating": 4.5, "review_count": 12034, "features": ["国産鶏むね肉100%使用", "添加物不使用で安心", "小型犬から大型犬まで対応"], "image_url": _amz_img("B098JVTFKC")},
        {"asin": "B001R96CX0", "title": "アイリスオーヤマ 猫トイレ ネコのトイレ フード付き",    "brand": "アイリスオーヤマ", "price": "¥2,980", "star_rating": 4.3, "review_count": 6543,  "features": ["スコップ付きで掃除しやすい", "飛び散り防止の深型設計", "シンプルデザインで部屋に馴染む"], "image_url": _amz_img("B001R96CX0")},
        {"asin": "B07WJZL7Y5", "title": "GEX ジェックス 水槽セット グラステリア300 フィルター付き", "brand": "GEX",          "price": "¥6,980",  "star_rating": 4.4, "review_count": 4321,  "features": ["30cm水槽とフィルターのお得なセット", "初めての熱帯魚飼育に最適", "クリアなガラスで観賞しやすい"], "image_url": _amz_img("B07WJZL7Y5")},
        {"asin": "B07X2XXRLX", "title": "ネスレ ピュリナ プロプラン 犬用 成犬 チキン 3kg",      "brand": "Purina",         "price": "¥3,280",  "star_rating": 4.5, "review_count": 9872,  "features": ["高タンパクで筋肉をサポート", "消化しやすい高品質チキン", "皮膚・被毛の健康維持に配慮"], "image_url": _amz_img("B07X2XXRLX")},
    ],
}


def get_mock_products(category_name: str, associate_tag: str) -> list[dict]:
    tag      = associate_tag or "mirainikibouw-22"
    products = MOCK_PRODUCTS.get(category_name, MOCK_PRODUCTS["家電・カメラ"])
    result   = []
    for p in products:
        item        = p.copy()
        # 実 ASIN から直接商品ページへのリンク（アフィリエイトタグ付き）
        item["url"] = f"https://www.amazon.co.jp/dp/{p['asin']}?tag={tag}"
        result.append(item)
    return result
