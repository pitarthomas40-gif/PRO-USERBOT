from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DB_URI = os.environ.get("MONGO_DB_URI")

if not MONGO_DB_URI:
    raise ValueError("MONGO_DB_URI environment variable is not set")

client = AsyncIOMotorClient(MONGO_DB_URI)

db = client["ZaidDB"]

gban = db["gban"]
gmute = db["gmute"]
pmpermit = db["pmpermit"]
raid = db["raid"]
