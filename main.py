from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import requests
import json

async def on_fetch(request, env):
    import asgi
    return await asgi.fetch(app, request, env)

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def read_longlat(long: str, lat: str):
    item = {"long": long, "lat": lat}
    url = "http://api.open-meteo.com/v1/forecast/?latitude="+str(item["lat"])+"&longitude="+str(item["long"])+"&current=temperature_2m,precipitation"
    async def gather_response(url):
        r = requests.get(url)
        return r.json()
    result = await gather_response(url)
    return str(result["current"]["temperature_2m"])+","+str(result["current"]["precipitation"])