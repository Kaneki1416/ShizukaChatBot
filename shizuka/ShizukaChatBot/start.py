from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from shizuka import SHIZUKA

SHIZUKA_START = """
I am 𝙲𝚑𝚕𝚘𝚎 𝙳𝚎𝚌𝚔𝚎𝚛 , An Intelligent ChatBot.[⠀](https://telegra.ph/file/71d85bebf14823103b201.jpg)
"""


@SHIZUKA.on_message(
    filters.command(["start"], prefixes=["/", "!"]) & ~filters.edited)
async def info(client, message):
    buttons = [
        [
            InlineKeyboardButton(text="Go inline",
                                 switch_inline_query_current_chat="shizuka "),
        ],
        [
            InlineKeyboardButton(
                "DEVLOPER",
                url="https://t.me/KaNeKi354_bot"),
            InlineKeyboardButton("ABOUT MASTER",
                                 url="https://t.me/AboutKenKaneki"),
        ],
    ]
    await SHIZUKA.send_message(
        chat_id=message.chat.id,
        text=𝙲𝚑𝚕𝚘𝚎 𝙳𝚎𝚌𝚔𝚎𝚛_START,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
