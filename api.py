from fastapi import FastAPI, HTTPException, Depends, Query
from imei_service import ImeiService
from config import AUTHENTICATION_TOKEN

app = FastAPI()

@app.post("/api/check-imei")
async def check_imei(imei: str, token: str):

    if token != AUTHENTICATION_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    if not imei:
        raise HTTPException(status_code=400, detail="IMEI is required")

    result = ImeiService.check_imei(imei)
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)