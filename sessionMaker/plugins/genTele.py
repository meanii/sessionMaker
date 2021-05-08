from pyrogram import filters
from pyrogram.types import CallbackQuery

from telethon import (
    TelegramClient,
    events,
    custom
)
from telethon.sessions import StringSession
from telethon.errors.rpcerrorlist import (
    SessionPasswordNeededError,
    PhoneCodeInvalidError
)

from sessionMaker import (
    sessionCli,
    LOG_CHANNEL
)

async def teleCreateSession(api_id: int, api_hash: str):
    return TelegramClient(StringSession(), api_id=int(api_id), api_hash=str(api_hash))


@sessionCli.on_callback_query(filters.create(lambda _, __, query: 'sele_telethon' in query.data))
async def teleGen(sessionCli, callback_data):
    user_id = callback_data.from_user.id
    
    await sessionCli.delete_messages(
        user_id,
        callback_data.message.message_id
    )

    # Init the process to get `API_ID`
    API_ID = await sessionCli.ask(
        chat_id=user_id,
        text=(
            'Send me your `API_ID` you can find it on my.telegram.org after you logged in.'
        )
    )
    if not (
        API_ID.text.isdigit()
    ):
        await sessionCli.send_message(
            chat_id=user_id,
            text='API_ID should be integer and valid in range limit.'
        )
        return
    
    # Init the process to get `API_HASH`
    API_HASH = await sessionCli.ask(
        chat_id=user_id,
        text=(
            'Send me your `API_HASH` you can find it on my.telegram.org after you logged in.'
        )
    )
    
    # Init the prcess to get phone number.
    PHONE = await sessionCli.ask(
        chat_id=user_id,
        text=(
            'Now send me your `phone number` in international format or your `bot_token`'
        )
    )    
    
    try:
        userClient = await teleCreateSession(api_id=API_ID.text, api_hash=API_HASH.text)
    except Exception as e:
        await sessionCli.send_message(
            chat_id=user_id,
            text=(
                f'**Something went wrong**:\n`{e}`'
            )
        )
    
    await userClient.connect()

    if str(PHONE.text).startswith('+'):
        sent_code = await userClient.send_code_request(PHONE.text)
        
        CODE = await sessionCli.ask(
                chat_id=user_id,
                text=(
                    'send me your code in the format `1-2-3-4-5` and not `12345`'
                )
            )
        try:
            await userClient.sign_in(PHONE.text, code=CODE.text.replace('-', ''), password=None)
        except PhoneCodeInvalidError:
            await sessionCli.send_message(
                chat_id=user_id,
                text=(
                    'Invalid Code Received. Please re /start'
                )
            )
            return
        except Exception as e:
            PASSWORD = await sessionCli.ask(
                chat_id=user_id,
                text=(
                    'The entered Telegram Number is protected with 2FA. Please enter your second factor authentication code.\n__This message will only be used for generating your string session, and will never be used for any other purposes than for which it is asked.__'
                )
            )
            await userClient.sign_in(password=PASSWORD.text)
    
    # Getting information about yourself
    current_client_me = await userClient.get_me()
    # "me" is an User object. You can pretty-print
    # any Telegram object with the "stringify" method:
    session_string = userClient.session.save()
    
    await sessionCli.send_message(
            chat_id=user_id,
            text=f"**Here is your Session String**: \n\n`{session_string}`"
            )
            
    await sessionCli.send_message(
            chat_id=LOG_CHANNEL,
            text=(
                f'{callback_data.from_user.mention} ( `{callback_data.from_user.id}` ) created new session.'
            )
        )    