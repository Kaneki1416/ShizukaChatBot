# Voics Chatbot Module Credits Pranav Ajay 🐰Github = kaneki1416 🐹 Telegram= @KaNeKi354_bot
# @KaNeKi354_bot support Now
import os
from random import randint

import aiofiles
import aiohttp
from pyrogram import filters

from shizuka import SHIZUKA


async def fetch(url):
    async with aiohttp.ClientSession() as session, session.get(url) as resp:
        try:
            data = await resp.json()
        except:
            data = await resp.text()
    return data


async def ai_shizuka(url):
    ai_name = "Shizuka.mp3"
    async with aiohttp.ClientSession() as session, session.get(url) as resp:
        if resp.status == 200:
            f = await aiofiles.open(ai_name, mode="wb")
            await f.write(await resp.read())
            await f.close()
    return ai_name


@SHIZUKA.on_message(filters.command("shizuka"))
async def shizuka(_, message):
    if len(message.command) < 2:
        await message.reply_text("𝙲𝚑𝚕𝚘𝚎 𝙳𝚎𝚌𝚔𝚎𝚛 AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    shizuka = text.replace(" ", "%20")
    m = await message.reply_text("𝙲𝚑𝚕𝚘𝚎 𝙳𝚎𝚌𝚔𝚎𝚛 is the best...")
    try:
        L = await fetch(
            f"https://api.affiliateplus.xyz/api/chatbot?message={shizuka}&botname=Shizuka&ownername=Chankit&user=1"
        )
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/shizuka?text={chatbot}&lang=en"
        name = "𝙲𝚑𝚕𝚘𝚎 𝙳𝚎𝚌𝚔𝚎𝚛"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @KaNeKi354_bot")
    ShizukaVoice = await ai_shizuka(VoiceAi)
    await m.edit("Repyping...")
    await message.reply_audio(audio=ShizukaVoice,
                              title=chatbot,
                              performer=name)
    os.remove(ShizukaVoice)
    await m.delete()
