from fastapi import FastAPI, Request
import trafilatura

app = FastAPI()

@app.post("/extract")
async def extract(request: Request):
    data = await request.json()
    url = data.get("url")
    html = data.get("html")
    content = ""
    if html:
        content = trafilatura.extract(html)
    elif url:
        downloaded = trafilatura.fetch_url(url)
        content = trafilatura.extract(downloaded)
    return {"content": content}
