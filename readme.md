#  Session Maker

This bot can generate session string of **pyrogram** and **telethon**.

## Note
> We don't collect or log users\' credentials.
> If something happens to your account, we aren't responsible for it.

## Host own bot
- Fork this repo.
- Rename `sessionMaker/sample_setting.py` file to `sessionMaker/setting.py`.
- Fill the **basic configrations**.

## setting file
```
class  BasicSettings:
	API_ID: int = 2094105
	API_HASH: str = 91eb9e4b583b6e7ec3a6df7ef5be2be0
	BOT_TOKEN: str = 2126915830:AAE2l5MOAGU6ZByc5zKC04fin-mx582pbHE
	LOG_CHANNEL: int = None
```
- You can get your `API_ID` and `API_HASH` from my.telegram.org.
- `BOT_TOKEN` from [@botfather](https://t.me/botfather)
- `LOG_CHANNEL` is your channel id.

### Requirements
-   Python 3.6 or higher.
-   A  [Telegram API key](https://docs.pyrogram.org/intro/setup#api-keys).

### Installing
`python3 -m sessionMaker`

###  Copyright & License
- Copyright (C)  2021 [meanii](https://github.om/meanii )
- Licensed under the terms of the [GNU General Public License v3.0](https://github.com/meanii/sessionMaker/blob/master/LICENSE)
