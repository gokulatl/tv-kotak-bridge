from fastapi import FastAPI, Request
import datetime

app = FastAPI()

@app.get("/")
def home():
    return {"message": "TradingView → Kotak bridge is running"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("Received alert:", data)
    return {
        "status": "ok",
        "received": data,
        "time": str(datetime.datetime.now())
    }
