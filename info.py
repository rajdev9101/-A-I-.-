# ©️biisal jai shree krishna 😎
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_ID = environ.get("API_ID" , "27084955")
API_HASH = environ.get("API_HASH" , "91c88b554ab2a34f8b0c72228f06fc0b")
BOT_TOKEN = environ.get("BOT_TOKEN" , "")
ADMIN = int(environ.get("ADMIN" , "5804953849"))
CHAT_GROUP = int(environ.get("CHAT_GROUP", "-1002031770441"))
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002391366258")
MONGO_URL = environ.get("MONGO_URL" , "mongodb+srv://harikrishnaakkireddi1:AeeBOzCUextQBCaa@cluster0.8w1om.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNEL = int(
    environ.get("AUTH_CHANNEL", "-1002391366258")
)
FSUB = environ.get("FSUB", False)
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME"
).split()
COOL_TIMER = 20  # keep this atleast 20
ONLY_SCAN_IN_GRP = environ.get(
    "ONLY_SCAN_IN_GRP", True
)  # If IMG_SCAN_IN_GRP is set to True, image scanning is restricted to your support group only. If it's False, the image scanning feature can be used anywhere.
REACTIONS = ["❤️‍🔥", "⚡", "🔥"]
