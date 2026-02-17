import asyncio
import importlib
from pyrogram import Client, idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app, ids
from flask import Flask
import threading

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is alive!"

def run():
    web_app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run).start()


async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Zaid.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
