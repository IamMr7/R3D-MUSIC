import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["","‹ اوامر التشغيل ›"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b4e01d217d9dfcd10f8c0.jpg",
        caption=f"""**- اوامر التشغيل اتبع مايلي
        
 [— — — — — — — — — —](https://te.legra.ph/file/b4e01d217d9dfcd10f8c0.jpg)
◇︰ تشغيل أو شغل : لبدء تشغيل الاغاني .

◇︰ بينج : لقياس سرعة النت في البوت .

◇︰أوامر القناة : تشغيل + أسم الأغنية  .

◇︰ كتم او مؤقت : لكتم الأغنية الحالية .

◇︰ كمل : لألغاء كتم الاغنية الحالية .

◇︰ تخطي : لتخطي الأغنية الحالية .

◇︰ ايقاف : لايقاف تشغيل الأغنية الحالية .**
""",
        reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("‹ السورس ›", url="https://t.me/rr_yn7"),
            InlineKeyboardButton("‹ الدعم ›", url="https://t.me/F_b_i_u"),
        ],
        [
            InlineKeyboardButton("Ꭺ𝟽𝖬𝖊𝖣 . 🇵🇸 ›", url="https://t.me/F_b_i_z"),
        ],
        [
            InlineKeyboardButton("𝑅𝐴𝑌𝐴𝑁⛧", url="https://t.me/F_k_Q"),
        ],
    ]
)

@app.on_message(
    command(["","‹ اوامر التفعيل ›"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b4e01d217d9dfcd10f8c0.jpg",
        caption=f"""**
- اوامر التفعيل اتبع مايلي

— — — — — — — — — —

‹ طريقه تفعيل البوت في الكروبات والقنوات ⤈ ›

اضف البوت مع كامل الصلاحيات عدا البقاء متخفي 

افتح اتصال في المجموعة او القناة 

اكتب تشغيل + اسم الأغنية 

- سيتم انضمام الحساب المساعد الى المحادثة الصوتية وتشغيل الاغنية التي اردتها .
- الحساب المساعد عبارة عن حساب وهمي وضيفته فقط تشغيل الموسيقى 

- لاتقم بطرده او حضره اثناء تشغيل الموسيقى يمكنك استخدام الامر

- ايقاف لانهاء تشغيل المقطع الصوتي وخروج الحساب المساعد دون مشاكل**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/rr_yn7"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/F_b_i_u"),
                ],
                [
                   InlineKeyboardButton(
                        "Ꭺ𝟽𝖬𝖊𝖣 . 🇵🇸 ›", url=f"https://t.me/F_b_i_z"),
                [
                   InlineKeyboardButton(
                        "𝑅𝐴𝑌𝐴𝑁⛧", url=f"https://t.me/F_k_Q"),
                ],       
            ]
        ),
    )

@app.on_message(
    command(["",""])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/b4e01d217d9dfcd10f8c0.jpg",
        caption=f"""**
-  اوامر التسليه
 — — — — — — — — — — 
 
- ( غنيلي ) يرسل لك اغنية عشوائية

- ( فيلم ) فيلم كامل عشوائي

- ( متحركة ) متحركات عشوائيه مميزة

- ( اقتباسات ) اقتباس بالصورة جميل

- ( اسمي ) لعرض اسمك الكامل

- ( ا ) لعرض معلوماتك

- ( تاك ) لعمل تاك جماعي في المجموعه

- لو خيروك ↫ لعبة لو خيروك

- كت تويت ↫ لعبة كت تويت عشوائي 

- صراحه ↫ لعبة صراحه

- اسئلة ↫ اسئلة عشوائيه
— — — — — — — — — — — — — —**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/rr_yn7"),
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/F_b_i_u"),
                ],
                [
                   InlineKeyboardButton(
                        "Ꭺ𝟽𝖬𝖊𝖣 . 🇵🇸 ›", url=f"https://t.me/F_b_i_z"),
                [
                   InlineKeyboardButton(
                        "𝑅𝐴𝑌𝐴𝑁⛧", url=f"https://t.me/F_k_Q"),
                ],       
            ]
        ),
    )
