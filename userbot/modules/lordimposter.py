# thanks to @Skastickers for stickers....
# Among us.....
# credits to catuserbot
# Migrate To Lord Userbot 
# Please dont delete this

import asyncio
from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
from userbot import ALIVE_NAME, CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"


@bot.on(admin_cmd(pattern="imposter(|n) (.*)", outgoing=True))
async def _(event):
    kraken = bot.uid
    USERNAME = f"tg://user?id={kraken}"
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    text1 = await edit_or_reply(event, "Hmm... Looks like Something is wrong here🤔🧐!!")
    await sleep(2)
    await text1.delete()
    stcr1 = await event.client.send_file(
        event.chat_id, "CAADAQADRwADnjOcH98isYD5RJTwAg"
    )
    text2 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** I have to call discussion😯"
    )
    await sleep(3)
    await stcr1.delete()
    await text2.delete()
    stcr2 = await event.client.send_file(
        event.chat_id, "CAADAQADRgADnjOcH9odHIXtfgmvAg"
    )
    text3 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** We have to eject the imposter or will lose😥 "
    )
    await sleep(3)
    await stcr2.delete()
    await text3.delete()
    stcr3 = await event.client.send_file(
        event.chat_id, "CAADAQADOwADnjOcH77v3Ap51R7gAg"
    )
    text4 = await event.reply(f"**Others :** Where???🤨 ")
    await sleep(2)
    await text4.edit(f"**Others :** Who??🤔 ")
    await sleep(2)
    await text4.edit(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Its {name} , I saw {name}  using🤨 vent,"
    )
    await asyncio.sleep(3)
    await text4.edit(f"**Others :**Okay.. 😲Vote {name} ")
    await asyncio.sleep(2)
    await stcr3.delete()
    await text4.delete()
    stcr4 = await event.client.send_file(
        event.chat_id, "CAADAQADLwADnjOcH-wxu-ehy6NRAg"
    )
    hellevent = await event.reply(f"{name} is ejected.......🤐")
    await sleep(2)
    await event.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await sleep(0.5)
    await event.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await sleep(0.5)
    await event.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await sleep(0.5)
    await event.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await sleep(0.5)
    await event.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await sleep(0.5)
    await event.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await sleep(0.5)
    await event.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await sleep(0.5)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await sleep(0.5)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await sleep(0.5)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await sleep(0.2)
    await stcr4.delete()
    if cmd == "":
        await event.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await sleep(4)
        await event.delete()
        await event.client.send_file(event.chat_id, "CAADAQADLQADnjOcH39IqwyR6Q_0Ag")
    elif cmd == "n":
        await event.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await sleep(4)
        await event.delete()
        await event.client.send_file(event.chat_id, "CAADAQADQAADnjOcH-WOkB8DEctJAg")


@bot.on(admin_cmd(pattern="timp(|n) (.*)", outgoing=True))
async def _(event):
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    event = await event.edit(event, f"{name} is ejected.......")
    await sleep(2)
    await event.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await sleep(0.8)
    await event.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await sleep(0.8)
    await event.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await sleep(0.8)
    await event.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await sleep(0.8)
    await event.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await sleep(0.2)
    if cmd == "":
        await event.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
    elif cmd == "n":
        await event.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} was not an Imposter.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )


CMD_HELP.update(
    {
        "imposter": "**Modules** `imposter`\
\n\n>`.imposter` / `.impostern` <teks>\
\n**Usage:** dapatkan imposter sama stickers.\
\n\n>`.timp` / `.timpn` <teks>\
\n**Usage:** dapatkan imposter hanya teks."
    }
)
