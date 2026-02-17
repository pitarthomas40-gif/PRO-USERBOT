import os
from motor.motor_asyncio import AsyncIOMotorClient

# रेंडर पर मौजूद MONGO_DB_URI को कनेक्ट करना
MONGO_DB_URI = os.environ.get("MONGO_DB_URI")

if MONGO_DB_URI:
    cli = AsyncIOMotorClient(MONGO_DB_URI)
    dbb = cli # यही वो 'dbb' है जिसे gbandb.py ढूँढ रहा है
else:
    cli = None
    dbb = None
    
