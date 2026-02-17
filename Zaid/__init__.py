from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
from datetime import datetime
import time
import asyncio
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)

# --- पक्का फिक्स: aiosession को डायरेक्ट कॉल नहीं करेंगे ---
# हम इसे None रखेंगे ताकि बूट होते समय एरर न आए
aiosession = None 

# एक छोटा सा फंक्शन जो जरूरत पड़ने पर सेशन बना देगा
async def get_aiosession():
    global aiosession
    if aiosession is None:
        aiosession = ClientSession()
    return aiosession

# Python 3.10+ के लिए इवेंट लूप फिक्स
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
# -------------------------------------------------------

if API_ID:
   API_ID = API_ID
else:
   print("WARNING: API ID NOT FOUND USING ZAID API ⚡")
   API_ID = "6435225"

if API_HASH:
   API_HASH = API_HASH
else:
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

if STRING_SESSION1:
   print("Client1: Found.. Starting..📳")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="Zaid/modules"))
   clients.append(client1)

if STRING_SESSION2:
   print("Client2: Found.. Starting.. 📳")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="Zaid/modules"))
   clients.append(client2)

if STRING_SESSION3:
   print("Client3: Found.. Starting.. 📳")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="Zaid/modules"))
   clients.append(client3)

if STRING_SESSION4:
   print("Client4: Found.. Starting.. 📳")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="Zaid/modules"))
   clients.append(client4)

if STRING_SESSION5:
   print("Client5: Found.. Starting.. 📳")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="Zaid/modules"))
   clients.append(client5)

if STRING_SESSION6:
   print("Client6: Found.. Starting.. 📳")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="Zaid/modules"))
   clients.append(client6)

if STRING_SESSION7:
   print("Client7: Found.. Starting.. 📳")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="Zaid/modules"))
   clients.append(client7)

if STRING_SESSION8:
   print("Client8: Found.. Starting.. 📳")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="Zaid/modules"))
   clients.append(client8)

if STRING_SESSION9:
   print("Client9: Found.. Starting.. 📳")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="Zaid/modules"))
   clients.append(client9)

if STRING_SESSION10:
   print("Client10: Found.. Starting.. 📳")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="Zaid/modules")) 
   clients.append(client10)
