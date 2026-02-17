from motor.motor_asyncio import AsyncIOMotorClient
import os

# MongoDB URL from environment variable
MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise ValueError("MONGO_URL environment variable is not set")

# Create client
client = AsyncIOMotorClient(MONGO_URL)

# Database name
db = client["ZaidDB"]

# Collections
gban = db["gban"]
gmute = db["gmute"]
pmpermit = db["pmpermit"]
raid = db["raid"]
