from pyrogram import Client
from pyromod import listen

from sessionMaker.setting import BasicSettings


# Init bot session
API_ID = BasicSettings.API_ID
API_HASH = BasicSettings.API_HASH
BOT_TOKEN = BasicSettings.BOT_TOKEN
LOG_CHANNEL = BasicSettings.LOG_CHANNEL

sessionCli = Client(
    'botSession',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(
        root='sessionMaker.plugins'
    )
)
