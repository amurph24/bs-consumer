from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def receive_oauth_redirect(code: str | None = None):
    data = {}
    if code:
        data.update({"code": code})
    return data
