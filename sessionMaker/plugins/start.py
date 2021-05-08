from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from sessionMaker import sessionCli

START_MESSAGE = (
        'Hello there!\n'
        'I can generate session of [pyrogram](https://t.me/pyrogram) and [telethon](https://t.me/TelethonUpdates).\n\n'
        '**Note**: We don\'t collect or log users\' credentials.\n'
        'If something happens to your account, we aren\'t responsible for it.\n\n'
        'If you want to host your own bot then here is the github repo under the terms of the [GNU General Public License v3.0](https://github.com/meanii/sessionMaker/blob/master/LICENSE).\n'
        '> https://github.com/meanii/sessionMaker\n\n'
        'News channel: @spookyanii\n'
        'Support chat: @nina77chat' 
    )

KEYBOARD = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text='Pyrogram', callback_data='sele_pyrogram')],
    [InlineKeyboardButton(text='Telethon', callback_data='sele_telethon')]]
)

@sessionCli.on_message(filters.command('start'))
async def start(sessionCli, message):
    await message.reply(
        text=START_MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=True
    )
