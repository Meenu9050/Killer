import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 28976608

API_HASH = "1e200bdfdcc3cc816f9f6a62e6e6f4a0"
BOT_TOKEN = ""
BOT_ID = 7825870013

BOT_USERNAME = "@Infinity_powerfull_bot""

OWNER_USERNAME = "@DarkGamer7t2rI""

BOT_NAME = "━──『 🎶Infinity x music🎶 』──━"

ASSUSERNAME = "Assistant"

MONGO_DB_URI = "mongodb+srv://Sarkar123:GAUTAMMISHRA@sarkar.1uiwqkd.mongodb.net/?retryWrites=true&w=majority"
DURATION_LIMIT_MIN = 500000

LOGGER_ID =  "-1002843572899"

DISASTER_LOG =  "-1002843572899"

OWNER_ID = 7487670897

SPECIAL_USER = 8250510325

HEROKU_APP_NAME = None

HEROKU_API_KEY = None

UPSTREAM_REPO = "https://github.com/"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = ""

SUPPORT_CHANNEL = "https://t.me/dark_x_knight_musiczz_support/112"

SUPPORT_CHAT = "https://t.me/+zyocLmf3JvIwOWY9"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = getenv("STRING1", "")
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://graph.org/file/a2fcf8b4ef4087473818c-f812627a9ef012cff5.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/ppifj3.jpg"
STATS_IMG_URL = "https://files.catbox.moe/iyr906.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ppifj3.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/ppifj3.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/ppifj3.jpg"
SOUNCLOUD_IMG_URL ="https://files.catbox.moe/ppifj3.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/ppifj3.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/ppifj3.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/ppifj3.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/ppifj3.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
