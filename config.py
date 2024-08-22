from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/3c5ba5eaddad3b9aa2790.jpg" , "https://graph.org/file/1135f6756396a2d130921.jpg" , "https://graph.org/file/e24ddcc48bf5c191978b7.jpg" , "https://graph.org/file/45476e244abde5f6e4ae3.jpg" , "https://graph.org/file/df74d3cb75436c6f1e345.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/8fe8c4eb2886376e48423.jpg" , "https://graph.org/file/e8a56835015bf849637cf.jpg" , "https://graph.org/file/829b7bcb6eb706765b3d2.jpg" , "https://graph.org/file/3c61dd910606440ee8f66.jpg" , "https://graph.org/file/3c5ba5eaddad3b9aa2790.jpg" , "https://graph.org/file/45476e244abde5f6e4ae3.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/YorXsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/YorXUpdate")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6209871909").split()))


FAILED = "https://graph.org/file/2b8987507d39625a88520.jpg"
