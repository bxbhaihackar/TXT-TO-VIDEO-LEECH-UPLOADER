

from os import environ

API_ID = int(environ.get("API_ID", "25334222"))
API_HASH = environ.get("API_HASH", "c8ee66889518bd70403e36d54113f745")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "Skyhd2308_bot1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/Skyhd2308_bot")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")








