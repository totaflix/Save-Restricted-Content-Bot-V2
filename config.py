# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22920744"))
API_HASH = getenv("API_HASH", "31cb93c017f265e4fa6d0ba91236b826")
BOT_TOKEN = getenv("BOT_TOKEN", "7885103214:AAFgkSCh2e-LBEA5uE6qS4cwcYgqHOGXQdw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5659668981").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://starastar230:<password>@cluster0.5mhoa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-4511616877")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002426245991"))
