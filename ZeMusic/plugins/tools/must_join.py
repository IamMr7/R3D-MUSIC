from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/rr_yn7":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("ՏOᑌᖇᑕᗴ ᖇ3ᗪ", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/rr_yn7".isalpha():
                link = "https://t.me/rr_yn7"
            else:
                chat_info = await bot.get_chat("ՏOᑌᖇᑕᗴ ᖇ3ᗪ")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\n⌯︙قناة .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ՏOᑌᖇᑕᗴ ᖇ3ᗪ", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @rr_yn7!")