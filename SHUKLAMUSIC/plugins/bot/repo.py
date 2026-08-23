# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------
import httpx
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC.utils.errors import capture_err 
from SHUKLAMUSIC import app
from config import BOT_USERNAME

start_txt = (
    "🌟 🎶 <b>sᴜᴋᴜɴᴀ ᴍᴜsɪᴄ</b> 🎶 🌟\n\n"
    "✨ ʙᴀᴅᴀ ᴀᴀʏᴀ ʙᴏᴛ sᴛᴀᴛs ᴅᴇᴋʜɴᴇ,\n"
    "💗 ᴘᴀʜʟᴇ ᴀᴘɴɪ ʟɪɢᴇ ᴋᴇ sᴛᴀᴛs sᴜᴅʜᴀʀ ᴊᴀᴀᴋᴇ !\n\n"
    "<pre>|| ➡️ ᴜᴩᴛɪᴍᴇ    :  𝟷ʜ:𝟹𝟺ᴍ:𝟻𝟺s\n"
    " ➡️ sᴛᴏʀᴀɢᴇ  :  𝟸𝟽.𝟺%\n"
    " ➡️ ᴄᴩᴜ      :  𝟷𝟷.𝟸%\n"
    " ➡️ ʀᴀᴍ      :  𝟷𝟽.𝟻%||</pre>\n\n"
    "🌹 ᴘᴏᴡєʀєᴅ ʙʏ» <a href=\"https://t.me/+0PYdr4hTM6c2MTA1\">ᴠɪsʜᴀʟ</a>\n"
    "💐 🌸 🎀 ❤️"
)


@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌐 ηєᴛᴡᴏʀᴋ",
                url="https://t.me/VillainLoves1",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text="🏠 ʜᴏϻє",
                url="https://t.me/+0PYdr4hTM6c2MTA1",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text="👑 ᴍᴀsᴛᴇʀ",
                url="https://t.me/",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]

    await msg.reply_photo(
        photo="https://files.catbox.moe/pyt85v.jpg",
        caption=start_txt,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
