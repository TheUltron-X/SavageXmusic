from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters2, other_filters



@Client.on_message(command("start") & other_filters2)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""home_text_pm = """
*π Hα΄ΚΚα΄ !*

β *My Nα΄α΄α΄ Iα΄’ [π₯π©π±πδΉπππππππͺπ₯](https://t.me/savagexrobot).*
β *I'α΄ Tα΄Κα΄Ι’Κα΄α΄ Vα΄Ιͺα΄α΄ CΚα΄α΄ Aα΄α΄Ιͺα΄ WΙͺα΄Κ Sα΄α΄α΄ Uκ±α΄κ°α΄Κ Fα΄α΄α΄α΄Κα΄κ±.
!*
ββββββββββββββββββββββββ
β *Pα΄α΄‘α΄Κα΄α΄ π BΚ: [TYCHON](https://t.me/itz_me_tychon)!*
______________________________________

All commands can be used with: /help """

@Client.on_message(command("start") & other_filters)
async def ghelp(_, message: Message):
    await message.reply_text(f"**{bn} :-** Hey! PM me to get all the commands π")

