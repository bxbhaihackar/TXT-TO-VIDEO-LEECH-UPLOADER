

from os import environ

API_ID = int(environ.get("API_ID", "27433400"))
API_HASH = environ.get("API_HASH", "1a286620de5ffe0a7d9b57e604293555")
BOT_TOKEN = environ.get("BOT_TOKEN", "7962269907:AAF2a18wMGIp9-DaeGA0ctMqufgr6ROy6f8")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "roxybasicneedbot1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/roxybasicneedbot1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





