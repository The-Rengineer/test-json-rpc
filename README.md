# JSON-RPC FastAPI サンプル

このプロジェクトは、[JSON-RPC サクッと入門](https://zenn.dev/hachimada/articles/jsonrpc-basic) のサンプルコードをベースに、`FastAPI` を使用して JSON-RPC サーバーを構築するものです。

---

## ✅ 前提

- 元記事：[JSON-RPC サクッと入門](https://zenn.dev/hachimada/articles/jsonrpc-basic) のサンプルコードを使用
- Python バージョン：**3.12.3** で動作確認済み

---

## 🚀 セットアップ手順

以下のコマンドを順に実行してください：

```bash
git clone https://github.com/The-Rengineer/test-json-rpc.git
cd test-json-rpc

# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate  # Windows の場合は venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt

# サーバーの起動
python3 test.py


別のターミナルで以下の curl コマンドを実行してください：

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}' \
  http://localhost:8000/api

 正常なレスポンス例：

```json
{
  "jsonrpc": "2.0",
  "result": 19,
  "id": 1
}


