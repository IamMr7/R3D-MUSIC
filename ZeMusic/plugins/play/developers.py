import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["اليكس","المبرمج اليكس","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/565bbca337260f008c5fd.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪𝘼⤾🇵🇸](https://t.me/F_b_i_z)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @F_b_i_z❫
◉ 𝙸𝙳      : ❪ 6890685964 ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@F_b_i_z) my world (@rr_yn7 - @F_b_i_u) my bro (@F_k_Q) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝘼⤾🇵🇸", url=f"https://t.me/F_b_i_z"), 
                 ],[
                   InlineKeyboardButton(
                        "ՏOᑌᖇᑕᗴ ᖇ3ᗪ", url=f"https://t.me/rr_yn7"),
                ],

            ]

        ),

    )
