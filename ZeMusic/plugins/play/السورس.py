import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","رعد","السورس","سورس رعد"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b4e01d217d9dfcd10f8c0.jpg",
        caption=f"""
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "• 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 Ꭺ𝟽𝖬𝖊𝖣 . 🇵🇸 ›", url=f"https://t.me/F_b_i_z"),
               ],[
                    InlineKeyboardButton(
                        "ՏOᑌᖇᑕᗴ ᖇ3ᗪ", url=f"https://t.me/rr_yn7"),
                ],[
                    InlineKeyboardButton(
                        "• 𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 •", url=f"https://t.me/F_b_i_u"),
                ],[
                    InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data="close"),
            ]
        ]
         ),
     )

