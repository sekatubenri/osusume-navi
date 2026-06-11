"""Amazon PA API が使えない間のモック商品データ"""

import urllib.parse


def _search_url(keyword: str, tag: str) -> str:
    q = urllib.parse.quote(keyword)
    return f"https://www.amazon.co.jp/s?k={q}&tag={tag}"


def _img(color: str, label: str) -> str:
    """カテゴリ別カラープレースホルダー（常に表示される）"""
    return f"https://placehold.co/300x300/{color}/FFFFFF?text={urllib.parse.quote(label)}"


# カテゴリ別カラー設定
_EC  = ("2196F3", "家電")       # 青
_GM  = ("E91E63", "ゲーム")     # ピンク
_KT  = ("FF9800", "キッチン")   # オレンジ
_TY  = ("9C27B0", "おもちゃ")   # 紫
_SP  = ("4CAF50", "スポーツ")   # 緑
_FA  = ("F44336", "ファッション") # 赤
_BT  = ("E91E63", "美容")       # ピンク
_FD  = ("FF5722", "食品")       # 深オレンジ
_PT  = ("795548", "ペット")     # ブラウン

MOCK_PRODUCTS = {
    "家電・カメラ": [
        {"asin": "MOCK001", "title": "Anker PowerCore 10000 モバイルバッテリー",        "brand": "Anker",    "price": "¥2,990",  "star_rating": 4.5, "review_count": 28431, "features": ["コンパクトサイズで持ち運びやすい", "USB-C対応・高速充電", "スマホ約2回分充電可能"],        "image_url": _img(*_EC)},
        {"asin": "MOCK002", "title": "Echo Dot 第5世代 スマートスピーカー with Alexa",  "brand": "Amazon",   "price": "¥5,980",  "star_rating": 4.4, "review_count": 15023, "features": ["音質が大幅に向上", "スマートホームのハブとして機能", "Alexa搭載で音声操作が快適"],    "image_url": _img(*_EC)},
        {"asin": "MOCK003", "title": "Kindle Paperwhite 第11世代 防水機能搭載",         "brand": "Amazon",   "price": "¥14,980", "star_rating": 4.6, "review_count": 9872,  "features": ["6.8インチ大画面で読みやすい", "防水仕様でお風呂でも読める", "1回充電で最大10週間使用可能"], "image_url": _img(*_EC)},
        {"asin": "MOCK004", "title": "Fire TV Stick 4K Max ストリーミングメディアプレーヤー", "brand": "Amazon", "price": "¥9,980", "star_rating": 4.5, "review_count": 12540, "features": ["4K Ultra HD・Dolby Vision対応", "Wi-Fi 6対応で高速ストリーミング", "Alexa対応リモコン付属"], "image_url": _img(*_EC)},
        {"asin": "MOCK005", "title": "TP-Link WiFi 無線LAN ルーター Wi-Fi6対応",        "brand": "TP-Link",  "price": "¥7,999",  "star_rating": 4.3, "review_count": 6754,  "features": ["Wi-Fi 6対応で高速・安定通信", "最大3000Mbps", "簡単セットアップでスマホから設定可能"], "image_url": _img(*_EC)},
    ],
    "ゲーム": [
        {"asin": "MOCK006", "title": "Nintendo Switch 本体 Joy-Con ネオンブルー/ネオンレッド", "brand": "Nintendo", "price": "¥32,978", "star_rating": 4.7, "review_count": 45231, "features": ["TVモード・携帯モード・テーブルモードの3スタイル", "豊富なタイトルが揃う人気ゲーム機", "家族みんなで楽しめるマルチプレイ対応"], "image_url": _img(*_GM)},
        {"asin": "MOCK007", "title": "PlayStation 5 デジタル・エディション",            "brand": "Sony",     "price": "¥59,980", "star_rating": 4.6, "review_count": 8932,  "features": ["超高速SSDで快適なゲーム体験", "4K・120fps対応の高画質", "DualSenseのハプティックフィードバックで没入感アップ"], "image_url": _img(*_GM)},
        {"asin": "MOCK008", "title": "マリオカート8 デラックス -Switch",                "brand": "Nintendo", "price": "¥5,909",  "star_rating": 4.8, "review_count": 23109, "features": ["最大8人でオンライン対戦が楽しめる", "48コース収録の大ボリューム", "全年齢が楽しめる王道レースゲーム"], "image_url": _img(*_GM)},
        {"asin": "MOCK009", "title": "ゼルダの伝説 ティアーズ オブ ザ キングダム -Switch", "brand": "Nintendo", "price": "¥6,578", "star_rating": 4.8, "review_count": 18754, "features": ["広大なハイラルを自由に冒険", "独創的なスクラビルドシステム", "やりこみ要素満載の超大作RPG"], "image_url": _img(*_GM)},
        {"asin": "MOCK010", "title": "あつまれ どうぶつの森 -Switch",                   "brand": "Nintendo", "price": "¥5,273",  "star_rating": 4.7, "review_count": 35621, "features": ["自分だけの島を自由に開発", "家族や友人とのんびり楽しめる", "季節のイベントが毎月充実"], "image_url": _img(*_GM)},
    ],
    "キッチン・日用品": [
        {"asin": "MOCK011", "title": "象印 電気圧力鍋 2.8L EL-MB30",                   "brand": "象印",         "price": "¥14,800", "star_rating": 4.3, "review_count": 7823,  "features": ["ほったらかし調理でラクラク", "圧力調理・無水調理など多機能", "内鍋はフッ素加工で洗いやすい"], "image_url": _img(*_KT)},
        {"asin": "MOCK012", "title": "バルミューダ The Toaster スチームトースター",     "brand": "BALMUDA",      "price": "¥24,200", "star_rating": 4.4, "review_count": 5432,  "features": ["スチーム技術で外サクサク中ふわふわ", "おしゃれなデザイン", "トースト・チーズトースト・ピザなど5モード"], "image_url": _img(*_KT)},
        {"asin": "MOCK013", "title": "アイリスオーヤマ 衣類スチーマー ハンディスチーマー", "brand": "アイリスオーヤマ", "price": "¥3,480", "star_rating": 4.1, "review_count": 12034, "features": ["約30秒で使用可能なスピード加熱", "ハンガーにかけたまましわ伸ばし可能", "軽量コンパクトで収納場所不要"], "image_url": _img(*_KT)},
        {"asin": "MOCK014", "title": "ダイソン Dyson V8 Slim コードレス掃除機",         "brand": "Dyson",        "price": "¥44,800", "star_rating": 4.5, "review_count": 6231,  "features": ["軽量設計でリビングから階段まで楽に掃除", "強力な吸引力でゴミをしっかりキャッチ", "衛生的なゴミ捨て機能"], "image_url": _img(*_KT)},
        {"asin": "MOCK015", "title": "山崎実業 tower マグネット冷蔵庫サイドテーブル",   "brand": "山崎実業",     "price": "¥3,520",  "star_rating": 4.4, "review_count": 8921,  "features": ["マグネットで冷蔵庫側面に設置", "スマートフォン・調理器具を置ける", "シンプルなデザインでどんなキッチンにも合う"], "image_url": _img(*_KT)},
    ],
    "おもちゃ・ホビー": [
        {"asin": "MOCK016", "title": "レゴ LEGO クラシック 黄色のアイデアボックス",     "brand": "LEGO",         "price": "¥3,630",  "star_rating": 4.7, "review_count": 14532, "features": ["484ピース入りで自由に組み立て", "4歳から楽しめる入門セット", "想像力・創造力を育む"], "image_url": _img(*_TY)},
        {"asin": "MOCK017", "title": "タカラトミー プラレール 新幹線セット",             "brand": "タカラトミー", "price": "¥4,980",  "star_rating": 4.6, "review_count": 9871,  "features": ["新幹線車両と基本レールセット", "男の子に大人気の定番おもちゃ", "拡張パーツで大きなレイアウトも可能"], "image_url": _img(*_TY)},
        {"asin": "MOCK018", "title": "バンダイ ガンプラ RG 1/144 ガンダム",             "brand": "バンダイ",     "price": "¥2,200",  "star_rating": 4.8, "review_count": 21045, "features": ["リアルグレードの精密な作り", "色分け済みパーツで塗装不要", "大人も楽しめるプレミアム品質"], "image_url": _img(*_TY)},
        {"asin": "MOCK019", "title": "任天堂 amiibo マリオ",                            "brand": "Nintendo",     "price": "¥1,320",  "star_rating": 4.6, "review_count": 8732,  "features": ["対応ゲームで特典を解放できる", "インテリアとしても飾れる高品質フィギュア", "コレクション性が高い"], "image_url": _img(*_TY)},
        {"asin": "MOCK020", "title": "メガハウス ルービックキューブ 3×3",               "brand": "メガハウス",   "price": "¥1,540",  "star_rating": 4.5, "review_count": 11234, "features": ["世界中で愛される知育パズル", "スムーズな回転で快適プレイ", "大人から子供まで楽しめる"], "image_url": _img(*_TY)},
    ],
    "スポーツ・アウトドア": [
        {"asin": "MOCK021", "title": "コールマン テント ツーリングドーム ST 2人用",     "brand": "Coleman",  "price": "¥13,980", "star_rating": 4.4, "review_count": 8934,  "features": ["設営が簡単な吊り下げ式インナー", "前室が広く荷物を置けるスペースあり", "ソロ〜2人でのキャンプに最適"], "image_url": _img(*_SP)},
        {"asin": "MOCK022", "title": "ナイキ ランニングシューズ Air Zoom Pegasus",     "brand": "Nike",     "price": "¥14,300", "star_rating": 4.5, "review_count": 15678, "features": ["クッション性が高く長距離も快適", "通気性の良いメッシュアッパー", "初心者から上級者まで対応"], "image_url": _img(*_SP)},
        {"asin": "MOCK023", "title": "FIELDOOR ハンモック 自立式スタンド付き",          "brand": "FIELDOOR", "price": "¥9,980",  "star_rating": 4.3, "review_count": 6541,  "features": ["自立式スタンドで木がなくても設置可能", "耐荷重200kgの安心設計", "室内・屋外両方で使える"], "image_url": _img(*_SP)},
        {"asin": "MOCK024", "title": "ヨネックス バドミントンラケット 初心者向けセット", "brand": "YONEX",   "price": "¥4,290",  "star_rating": 4.4, "review_count": 7823,  "features": ["ラケット2本・シャトル3個のお得なセット", "初心者でも扱いやすい軽量設計", "家族・友人と気軽に楽しめる"], "image_url": _img(*_SP)},
        {"asin": "MOCK025", "title": "ドウシシャ 折りたたみ自転車 20インチ",            "brand": "ドウシシャ", "price": "¥19,800", "star_rating": 4.2, "review_count": 4532,  "features": ["コンパクトに折りたためる", "通勤・通学・レジャーに活躍", "変速機能付きで坂道も快適"], "image_url": _img(*_SP)},
    ],
    "ファッション": [
        {"asin": "MOCK026", "title": "ユニクロ ヒートテック エクストラウォーム タートルネックT", "brand": "UNIQLO",           "price": "¥1,990",  "star_rating": 4.6, "review_count": 32145, "features": ["極暖素材で寒い冬も快適", "タートルネックで首元もあったか", "インナーとしても普段着としても使える"], "image_url": _img(*_FA)},
        {"asin": "MOCK027", "title": "無印良品 足なり直角靴下 3足組",                   "brand": "MUJI",             "price": "¥990",    "star_rating": 4.5, "review_count": 18923, "features": ["かかとがズレない直角設計", "肌に優しい綿素材", "3足セットでお買い得"], "image_url": _img(*_FA)},
        {"asin": "MOCK028", "title": "アディダス スニーカー Stan Smith メンズ",         "brand": "adidas",           "price": "¥13,200", "star_rating": 4.6, "review_count": 25431, "features": ["シンプルで合わせやすいデザイン", "カジュアルからきれいめコーデまで対応", "クッション性が高く長時間歩いても疲れない"], "image_url": _img(*_FA)},
        {"asin": "MOCK029", "title": "ワークマン イージスオーシャン 防水防寒ジャケット", "brand": "WORKMAN",          "price": "¥4,900",  "star_rating": 4.5, "review_count": 12034, "features": ["高い防水性能で雨の日も安心", "リーズナブルなのに高機能", "アウトドア・通勤どちらにも対応"], "image_url": _img(*_FA)},
        {"asin": "MOCK030", "title": "サマンサタバサ レディースバッグ トートバッグ",    "brand": "Samantha Thavasa", "price": "¥8,800",  "star_rating": 4.3, "review_count": 5612,  "features": ["A4サイズが入る大容量", "軽量素材で肩が疲れにくい", "通勤・お出かけに使いやすいデザイン"], "image_url": _img(*_FA)},
    ],
    "ビューティー": [
        {"asin": "MOCK031", "title": "パナソニック ヘアドライヤー ナノケア EH-NA0J",    "brand": "Panasonic", "price": "¥22,000", "star_rating": 4.6, "review_count": 14532, "features": ["ナノイーで髪のうるおいを保つ", "速乾性が高く時間を節約", "くせ毛もしっかりまとまる"], "image_url": _img(*_BT)},
        {"asin": "MOCK032", "title": "資生堂 マキアージュ ドラマティックスキンセンサーベース UV", "brand": "SHISEIDO", "price": "¥2,420", "star_rating": 4.4, "review_count": 8921, "features": ["SPF50+・PA++++の高い紫外線対策", "皮脂・テカリを長時間防ぐ", "化粧もちが格段にアップ"], "image_url": _img(*_BT)},
        {"asin": "MOCK033", "title": "花王 ビオレ UV アクアリッチ ウォータリーエッセンス", "brand": "花王",   "price": "¥1,045",  "star_rating": 4.5, "review_count": 21043, "features": ["SPF50+・PA++++の最高レベル", "水のようにさらっとしたテクスチャー", "コスパ最強の定番日焼け止め"], "image_url": _img(*_BT)},
        {"asin": "MOCK034", "title": "コーセー雪肌精 化粧水 500ml 大容量ボトル",        "brand": "KOSE",      "price": "¥2,530",  "star_rating": 4.5, "review_count": 9872,  "features": ["透明感のある肌へ導く美白化粧水", "ベタつかず肌なじみが良い", "500mlの大容量でコスパ抜群"], "image_url": _img(*_BT)},
        {"asin": "MOCK035", "title": "カネボウ SALA ヘアオイル まとまりスムース",       "brand": "Kanebo",    "price": "¥968",    "star_rating": 4.3, "review_count": 7654,  "features": ["アウトバストリートメントとして使いやすい", "まとまりのあるサラサラ髪に", "プチプラで毎日使いやすい"], "image_url": _img(*_BT)},
    ],
    "食品・飲料": [
        {"asin": "MOCK036", "title": "UCC 職人の珈琲 ドリップコーヒー 50袋",            "brand": "UCC",        "price": "¥1,180",  "star_rating": 4.5, "review_count": 18432, "features": ["一杯ずつ新鮮に淹れられるドリップ式", "50袋入りのお得なまとめ買い", "コクと香りのバランスが良い"], "image_url": _img(*_FD)},
        {"asin": "MOCK037", "title": "カルビー ポテトチップス うすしお味 60g×24袋",    "brand": "Calbee",     "price": "¥2,354",  "star_rating": 4.6, "review_count": 25431, "features": ["定番の味で家族全員に人気", "24袋の箱買いでストックに便利", "パーティーやおやつに最適"], "image_url": _img(*_FD)},
        {"asin": "MOCK038", "title": "伊藤園 お〜いお茶 緑茶 2L×6本",                  "brand": "伊藤園",     "price": "¥1,296",  "star_rating": 4.6, "review_count": 32145, "features": ["毎日飲みたい定番のお茶", "2Lの大容量でコスパ抜群", "無香料・無添加の本格緑茶"], "image_url": _img(*_FD)},
        {"asin": "MOCK039", "title": "明治 ザバス ホエイプロテイン100 バニラ味 1050g", "brand": "Meiji",      "price": "¥5,980",  "star_rating": 4.5, "review_count": 14532, "features": ["吸収が早いホエイプロテイン", "飲みやすいバニラ味", "1050gの大容量でコスパ良好"], "image_url": _img(*_FD)},
        {"asin": "MOCK040", "title": "ハウス食品 バーモントカレー 甘口 230g×10個",      "brand": "House Foods","price": "¥2,200",  "star_rating": 4.7, "review_count": 19876, "features": ["子供から大人まで人気の定番カレー", "10個まとめ買いでストックに便利", "りんごとはちみつの優しい甘さ"], "image_url": _img(*_FD)},
    ],
    "ペット用品": [
        {"asin": "MOCK041", "title": "ロイヤルカナン 猫用 インドア 成猫用 4kg",         "brand": "Royal Canin",   "price": "¥4,580",  "star_rating": 4.6, "review_count": 8921,  "features": ["室内飼い猫に最適な栄養バランス", "毛玉ケアに配慮したフォーミュラ", "獣医師も推奨する信頼のブランド"], "image_url": _img(*_PT)},
        {"asin": "MOCK042", "title": "コンボ 犬用おやつ 国産とりむね肉 14袋",           "brand": "COMBO",         "price": "¥980",    "star_rating": 4.5, "review_count": 12034, "features": ["国産鶏むね肉100%使用", "添加物不使用で安心", "小型犬から大型犬まで対応"], "image_url": _img(*_PT)},
        {"asin": "MOCK043", "title": "アイリスオーヤマ 猫トイレ 本体 ネコのトイレ",    "brand": "アイリスオーヤマ", "price": "¥2,980", "star_rating": 4.3, "review_count": 6543,  "features": ["スコップ付きで掃除しやすい", "飛び散り防止の深型設計", "シンプルデザインで部屋に馴染む"], "image_url": _img(*_PT)},
        {"asin": "MOCK044", "title": "GEX ジェックス 水槽セット グラステリア 300",      "brand": "GEX",           "price": "¥6,980",  "star_rating": 4.4, "review_count": 4321,  "features": ["30cm水槽とフィルターのお得なセット", "初めての熱帯魚飼育に最適", "クリアなガラスで観賞しやすい"], "image_url": _img(*_PT)},
        {"asin": "MOCK045", "title": "ピュリナ プロプラン 犬用 成犬 チキン 3kg",       "brand": "Purina",        "price": "¥3,280",  "star_rating": 4.5, "review_count": 9872,  "features": ["高タンパクで筋肉をサポート", "消化しやすい高品質チキン", "皮膚・被毛の健康維持に配慮"], "image_url": _img(*_PT)},
    ],
}


def get_mock_products(category_name: str, associate_tag: str) -> list[dict]:
    tag      = associate_tag or "mirainikibouw-22"
    products = MOCK_PRODUCTS.get(category_name, MOCK_PRODUCTS["家電・カメラ"])
    result   = []
    for p in products:
        item        = p.copy()
        item["url"] = _search_url(p["title"], tag)
        result.append(item)
    return result
