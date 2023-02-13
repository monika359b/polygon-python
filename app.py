import asyncio
import requests

async def send_requests(url, interval):
    while True:
        resp = requests.get(url)
        print(resp.json())
        await asyncio.sleep(interval)

async def main():
    url = "https://tronb2.vercel.app/"
    interval = 0
    await send_requests(url, interval)

asyncio.run(main())
