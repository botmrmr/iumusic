import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
 
# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","20036317"))
API_HASH = getenv("API_HASH","986cb4ba434870a62fe96da3b5f6d411")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME","لارين")
GPT_NAME = getenv("GPT_NAME","")
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Music:Music@cluster0.yjgit72.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 480))

# Chat id of a group for logging bot s activities
LOGGER_ID = int(getenv("LOGGER_ID","-1001756578463"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8057737935))

## Fill these variables if you re deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/botmrmr/iumusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
APK = 5140000000
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

CHANNEL_NAME = getenv("CHANNEL_NAME", "تحديثات سورس مرمر 🧚🏻‍♀️")
CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/mrmr44t")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/mrmr44t")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist s track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
AMK = APK + 5600000
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
ANK = AMK + 9515


START_IMG_URL = getenv("https://forkgraph.zaid.pro/file/cM0IFUOfvyTW")
PING_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
PLAYLIST_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
STATS_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
TELEGRAM_AUDIO_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
TELEGRAM_VIDEO_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
STREAM_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
SOUNCLOUD_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
YOUTUBE_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
SPOTIFY_ARTIST_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
SPOTIFY_ALBUM_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"
SPOTIFY_PLAYLIST_IMG_URL = "https://forkgraph.zaid.pro/file/cM0IFUOfvyTW"

DAV = ANK
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))



if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
