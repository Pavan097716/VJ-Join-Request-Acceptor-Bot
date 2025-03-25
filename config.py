from os import environ

API_ID = int(environ.get("API_ID", "20793620"))
API_HASH = environ.get("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")
BOT_TOKEN = environ.get("BOT_TOKEN", "8010179329:AAEcvL08wwIKrKkskRqPmWs0-sCvt0VPgZw")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "1002296271857"))
ADMINS = int(environ.get("ADMINS", "6853851676"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://pokemonchannel098:yaE7BvFwWIXdb3HQ@cluster0.gdr57.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
