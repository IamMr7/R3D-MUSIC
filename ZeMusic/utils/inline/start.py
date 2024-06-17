from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني", url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الاوامر", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="𓏺 𝗗𝗲𝘃 𝘀𝗼𝘂𝗿𝗰𝗲 .", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="قناة السورس", url=f"https://t.me/rr_yn7"),
        ],
    ]
    return buttons
