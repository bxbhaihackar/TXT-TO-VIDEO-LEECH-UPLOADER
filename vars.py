

from os import environ

API_ID = int(environ.get("25334222", ""))
API_HASH = environ.get("c8ee66889518bd70403e36d54113f745", "")
BOT_TOKEN = environ.get("8908100142:AAG0JhHB1EQ71rWrTU2WrOmkNKj_u4nk6SY", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "votemey")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/votemey")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("8396934512", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





