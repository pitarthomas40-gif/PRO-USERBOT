import asyncio
import time
from datetime import datetime
from aiohttp import ClientSession
from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, \
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, \
    STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, \
    STRING_SESSION9, STRING_SESSION10

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)

# --- यहाँ बदलाव किया गया है ---
# सीधे ClientSession() कॉल करने के बजाय इसे None रखें 
# या मैन्युअली लूप सेटअप करें
aiosession = None

async def get_session():
    global aiosession
    if aiosession is None:
        aiosession = ClientSession()
    return aiosession

# Python 3.10+ के लिए इवेंट लूप फिक्स
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
# ------------------------------

if not API_ID:
   print("WARNING: API ID NOT FOUND USING ZAID API ⚡")
   API_ID = 6435225

if not API_HASH:
   print("WARNING: API HASH NOT FOUND USING ZAID API ⚡")   
   API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN NOT FOUND PLZ ADD ⚡")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

# बाकी का क्लाइंट कोड (client1, client2...) वैसे ही रहने दें
