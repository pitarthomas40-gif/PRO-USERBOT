import os
from motor.motor_asyncio import AsyncIOMotorClient

# रेंडर पर आपने जो नाम रखा है (MONGO_DB_URI या MONGO_URL) वही यहाँ लिखें
MONGO_DB_URI = os.environ.get("MONGO_DB_URI")

if MONGO_DB_URI:
    cli = AsyncIOMotorClient(MONGO_DB_URI)
else:
    cli = None # अगर URL नहीं मिली तो बॉट क्रैश नहीं होगा
