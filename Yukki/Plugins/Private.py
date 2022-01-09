from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("start") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""home_text_pm = """
*👋 Hᴇʟʟᴏ !*

✗ *My Nᴀᴍᴇ Iᴢ [🔥𓆩𝐱𝐃乛𝐒𝐚𝐕𝐚𝐆𝐞𓆪🔥](https://t.me/savagexrobot).*
✗ *I'ᴍ Tᴇʟᴇɢʀᴀᴍ Vᴏɪᴄᴇ Cʜᴀᴛ Aᴜᴅɪᴏ Wɪᴛʜ Sᴏᴍᴇ Uꜱᴇꜰᴜʟ Fᴇᴀᴛᴜʀᴇꜱ.
!*
────────────────────────
✗ *Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: [TYCHON](https://t.me/itz_me_tychon)!*
______________________________________

All commands can be used with: /help """

@Client.on_message(command("start") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**{bn} :-** Hey! PM me to get all the commands 😉")

