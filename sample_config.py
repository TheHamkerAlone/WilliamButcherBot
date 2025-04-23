import os

from dotenv import load_dotenv

load_dotenv(
    "config.env" if os.path.isfile("config.env") else "sample_config.env"
)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6392016724:")
API_ID = os.environ.get("API_ID", "17596251")
SESSION_STRING = os.environ.get("SESSION_STRING", "")
API_HASH = os.environ.get("API_HASH", "e58343b4c0193e293e391daf97603fcd")
USERBOT_PREFIX = os.environ.get("USERBOT_PREFIX", "\\")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
SUDO_USERS_ID = list(map(int, os.environ.get("SUDO_USERS_ID", "7552579717").split()))
LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID", "-1001603822916"))
GBAN_LOG_GROUP_ID = int(os.environ.get("GBAN_LOG_GROUP_ID", "-1001603822916"))
MESSAGE_DUMP_CHAT = int(os.environ.get("MESSAGE_DUMP_CHAT", "-1001603822916"))
WELCOME_DELAY_KICK_SEC = int(os.environ.get("WELCOME_DELAY_KICK_SEC", 600))
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://hny")
ARQ_API_KEY = os.environ.get("ARQ_API_KEY", "QBCFLQ-GIMBVP-CZAMUW-YGDWLM-ARQ")
ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://arq.hamker.dev")
LOG_MENTIONS = os.environ.get("LOG_MENTIONS", "True").lower() in ["true", "1"]
RSS_DELAY = int(os.environ.get("RSS_DELAY", 300))
PM_PERMIT = os.environ.get("PM_PERMIT", "True").lower() in ["true", "1"]
