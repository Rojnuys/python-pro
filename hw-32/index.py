import json
import random
import string
from http import HTTPStatus

import aiofiles
import aiosqlite
import asyncio
import requests
import sqlite3


conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image BLOB NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bitcoin_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uah NUMBER NOT NULL
)
""")

conn.close()


def get_random_name(length: int = 5) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


async def fetch_image(image_url, image_future):
    response = await asyncio.to_thread(requests.get, image_url)

    if response.status_code != HTTPStatus.OK:
        raise ValueError(f"Failed to fetch data. Status code: {response.status_code}")

    image_future.set_result(response.content)


async def save_image(image_folder, image_future):
    content = await image_future
    image_path = image_folder + "/" + get_random_name(8) + ".jpg"

    async with aiofiles.open(image_path, mode='wb') as f:
        await f.write(content)


async def save_image_db(image_future):
    content = await image_future

    async with aiosqlite.connect("test.db") as db:
        await db.execute("INSERT INTO images (image) VALUES (?)", (content,))
        await db.commit()


async def fetch_bitcoin_rate(bitcoin_url, bitcoin_future):
    response = await asyncio.to_thread(requests.get, bitcoin_url)

    if response.status_code != HTTPStatus.OK:
        raise ValueError(f"Failed to fetch data. Status code: {response.status_code}")

    bitcoin_future.set_result(response.content)


async def save_bitcoin_rate_file(rate_path, bitcoin_future):
    content = await bitcoin_future

    async with aiofiles.open(rate_path, mode='ab') as f:
        await f.write(content)
        await f.write(b"\n")


async def save_bitcoin_rate_db(bitcoin_future):
    content = await bitcoin_future
    rate = json.loads(content)["rate"]

    async with aiosqlite.connect("test.db") as db:
        await db.execute("INSERT INTO bitcoin_rates (uah) VALUES (?)", (rate,))
        await db.commit()


async def get_bitcoin_rate_db():
    async with aiosqlite.connect("test.db") as db:
        async with db.execute("SELECT * FROM bitcoin_rates") as cursor:
            async for row in cursor:
                print(row)


async def main_loop():
    image_url = "https://picsum.photos/400/600"
    bitcoin_url = "https://bitpay.com/api/rates/uah"
    image_folder = "uploads"
    rate_path = "bitcoin_rate.txt"

    while True:
        bitcoin_fut = asyncio.Future()
        image_fut = asyncio.Future()

        await asyncio.gather(
            fetch_image(image_url, image_fut),
            save_image(image_folder, image_fut),
            save_image_db(image_fut),
            fetch_bitcoin_rate(bitcoin_url, bitcoin_fut),
            save_bitcoin_rate_file(rate_path, bitcoin_fut),
            save_bitcoin_rate_db(bitcoin_fut),
            get_bitcoin_rate_db()
        )


asyncio.run(main_loop())

# event_loop = asyncio.get_event_loop()
#
# bitcoin_fut = asyncio.Future()
# image_fut = asyncio.Future()
#
# event_loop.create_task(fetch_image(image_url, image_fut))
# event_loop.create_task(save_image(image_folder, image_fut))
# event_loop.create_task(save_image_db(image_fut))
# event_loop.create_task(fetch_bitcoin_rate(bitcoin_url, bitcoin_fut))
# event_loop.create_task(save_bitcoin_rate_file(rate_path, bitcoin_fut))
# event_loop.create_task(save_bitcoin_rate_db(bitcoin_fut))
# event_loop.create_task(get_bitcoin_rate_db())
#
# event_loop.run_forever()
