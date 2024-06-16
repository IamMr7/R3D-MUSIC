from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app

@app.on_message(filters.incoming & filters.private, group=-2)
async def MUST_JOINN_channel(bot: Client, msg: Message):
    if not "https://t.me/F_b_i_u":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("F_b_i_u", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/F_b_i_u".isalpha():
                link = "https://t.me/F_b_i_u"
            else:
                chat_info = await bot.get_chat("F_b_i_u")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"❃︙عذࢪاَ عزيزي ↫ {msg.from_user.mention} \n❃︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ .\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("𝐆𝐫𝐨𝐮𝐩 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOINN chat @F_b_i_u !")