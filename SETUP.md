# セットアップ手順（匿名・完全無料構成）

## システム全体像

```
[GitHub Actions] 毎日 JST 07:00
       │
       ├─ Python scripts/main.py
       │     ├─ Amazon PA API → ベストセラー商品取得
       │     └─ Claude API    → 記事生成 → content/posts/*.md
       │
       ├─ Hugo --minify → public/（静的HTML）
       │
       └─ GitHub Pages → https://USERNAME.github.io/REPO_NAME/
```

---

## Step 1: 仮名GitHubアカウントを作成

1. https://github.com/signup を開く
2. メールアドレスは新規作成した捨てアドレスを使う（Protonmail等が便利）
3. ユーザー名はブログの仮名に合わせて設定（例: `navi-products`）
4. アカウント作成後、**このフォルダをリポジトリとしてプッシュ**:

```bash
cd amazon-affiliate-blog
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## Step 2: GitHub Pages を有効化

1. リポジトリの **Settings → Pages**
2. Source: `Deploy from a branch`
3. Branch: `gh-pages` / `/ (root)`
4. Save → 数分後に `https://USERNAME.github.io/REPO_NAME/` が公開される

> ※ `hugo.toml` の `baseURL` を上記URLに変更してコミット・プッシュする

---

## Step 3: Amazon アソシエイトに登録

1. https://affiliate.amazon.co.jp/ → アカウント作成
   - 氏名・住所は本名が必要（収益の受け取りに使用）だが、ブログ自体は仮名でOK
2. ブログURL欄に `https://USERNAME.github.io/REPO_NAME/` を入力
3. アソシエイトID取得（例: `myblog-22`）

### PA API の有効化（重要）
- 登録後 **3日以上経過** かつ **売上実績が必要**
- 最初の数日はアソシエイトリンクを手動で作成 → 友人等に購入してもらう or 自分で購入
- 売上が1件でも入ると PA API が申請可能になる
- アソシエイトセントラル → ツール → Product Advertising API → 認証情報を発行

---

## Step 4: Anthropic API キーを取得

1. https://console.anthropic.com/ でアカウント作成
2. API Keys → Create Key → コピーしておく

---

## Step 5: GitHub Secrets に認証情報を登録

リポジトリの **Settings → Secrets and variables → Actions → New repository secret**

| Secret 名 | 値 |
|---|---|
| `AMAZON_ACCESS_KEY` | PA API アクセスキーID |
| `AMAZON_SECRET_KEY` | PA API シークレットキー |
| `AMAZON_ASSOCIATE_TAG` | アソシエイトID（例: `myblog-22`）|
| `ANTHROPIC_API_KEY` | Claude API キー |

---

## Step 6: 手動テスト実行

GitHub リポジトリの **Actions → Daily Post & Deploy → Run workflow**

成功すると:
- `content/posts/` に `.md` ファイルが追加される
- Hugo でビルドされた静的サイトが `gh-pages` ブランチにプッシュされる
- ブログが更新される

---

## Step 7: ブログ名・仮名を変更

`hugo.toml` を編集:
```toml
title = "あなたのブログ名"
[params]
  author = "あなたの仮名"
  description = "ブログの説明文"
```

---

## ローカルでの確認方法

```bash
# Hugoをインストール (Windows)
winget install Hugo.Hugo.Extended

# ローカルサーバー起動
hugo server

# ブラウザで確認
# http://localhost:1313/
```

---

## コスト

| 項目 | 費用 |
|---|---|
| GitHub (コード・Pages・Actions) | **無料** |
| Hugo (静的サイトジェネレーター) | **無料** |
| Claude Sonnet (記事90本/月) | 約 $5〜10/月 |
| Amazon アソシエイト | **無料** |
| **合計** | **約 ¥700〜1,500/月** |

---

## 注意事項

- Amazonアソシエイト規約でアフィリエイトリンクの開示が必要です（コードに組み込み済み）
- AI生成コンテンツはGoogleの品質評価の対象になります。定期的に記事の品質を確認することを推奨
- PA API の利用規約: https://affiliate.amazon.co.jp/help/operating/policies
