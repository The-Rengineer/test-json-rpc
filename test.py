from fastapi import FastAPI, Request
from jsonrpc import JSONRPCResponseManager, dispatcher
import uvicorn

app = FastAPI()

@dispatcher.add_method
def add(addend1: float, addend2: float) -> float:
    return addend1 + addend2

@dispatcher.add_method
def subtract(minuend: float, subtrahend: float) -> float:
    return minuend - subtrahend

@dispatcher.add_method
def multiply(multiplicand: float, multiplier: float) -> float:
    return multiplicand * multiplier

@dispatcher.add_method
def divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return dividend / divisor

@app.post("/api")
async def handle_rpc(request: Request) -> dict:

    # リクエストのバイトデータを取得し、文字列にデコードする
    body: bytes = await request.body()
    request_str: str = body.decode("utf-8")
    # JSON-RPC のリクエスト文字列を jsonrpc ライブラリで処理する
    response = JSONRPCResponseManager.handle(request_str, dispatcher)
    # レスポンスの data 部分を返却する
    return response.data

if __name__ == "__main__":
    # サーバーをホスト 0.0.0.0、ポート 8000 で起動する
    uvicorn.run(app, host="0.0.0.0", port=8000)
