from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ضيفني", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="الدعم", url=config.SUPPORT_CHAT),
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
            InlineKeyboardButton(text="مطور اليكس", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="الدعم", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="قناة المطور", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="قناة السورس", url=f"https://t.me/rr_yn7"),
        ],
    ]
    return buttons
