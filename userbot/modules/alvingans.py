# Lord-Userbot
# Create By Alvin
# Dont Remove License
# Yang Baca Dalem Hati Bau Sawi

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(117)

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            f"🌖"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@register(outgoing=True, pattern='^.helikopter(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ Hallo Semuanya :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \ \n")


@register(outgoing=True, pattern='^.tembak(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("_/﹋\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**")


@register(outgoing=True, pattern='^.bundir(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Dadah Semuanya...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n")

# Alvin Gans

@register(outgoing=True, pattern='^.pistol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░▄▌░░░░░░░░░▄\n"
                     "████████████▄\n"
                     "░░░░░░░░▀▐████\n"
                     "░░░░░░░░░░░▐██▌\n")


# Yang Baca Jomblo -Alvin

@register(outgoing=True, pattern='^.ano(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Anonymous \n"
                     "─────█─▄▀█──█▀▄─█─────\n"
                     "────▐▌──────────▐▌────\n"
                     "────█▌▀▄──▄▄──▄▀▐█────\n"
                     "───▐██──▀▀──▀▀──██▌───\n"
                     "──▄████▄──▐▌──▄████▄──\n")

@register(outgoing=True, pattern='^.kucing(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("──────▄▀▄─────▄▀▄\n"
                     "─────▄█░░▀▀▀▀▀░░█▄\n"
                     "─▄▄──█░░░░░░░░░░░█──▄▄\n"
                     "█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n")

@register(outgoing=True, pattern='^.alien(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒\n"
                     "▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒\n"
                     "▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒\n"
                     "▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒\n"
                     "▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒\n")


@register(outgoing=True, pattern='^.dinosaurus(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░▄▄▄▄░\n"
                     "▀▀▄██►\n"
                     "▀▀███►\n"
                     "░▀███►░█►\n"
                     "▒▄████▀▀\n")

@register(outgoing=True, pattern='^.robot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░░░░▄█▄▄▄█▄\n"
                     "▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄\n"
                     "█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█\n"
                     "░▐▌░░░░▀▀███▀▀░░░░▐▌\n"
                     "████░▄█████████▄░████\n")



@register(outgoing=True, pattern='^.iblis(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("───▄█▌─▄─▄─▐█▄\n"
                     "───██▌▀▀▄▀▀▐██\n"
                     "───██▌─▄▄▄─▐██\n"
                     "───▀██▌▐█▌▐██▀\n"
                     "▄██████─▀─██████▄\n")




@register(outgoing=True, pattern='^.snowman(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░▄░█░░░▄▀▀▀▀▀▄░░░█░▄░\n"
                     "▄▄▀▄░░░█─▀─▀─█░░░▄▀▄▄\n"
                     "░░░░▀▄▒▒▒▒▒▒▒▒▒▄▀░░░░\n"
                     "░░░░░█────▀────█░░░░░\n"
                     "░░░░░█────▀────█░░░░░\n")



@register(outgoing=True, pattern='^.paus(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("─────▀▄▀─────▄─────▄\n"
                     "──▄███████▄──▀██▄██▀\n"
                     "▄█████▀█████▄──▄█\n"
                     "███████▀████████▀\n"
                     "─▄▄▄▄▄▄███████▀\n")



@register(outgoing=True, pattern='^.radio(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░█▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                     "██▀▀▀██▀▀▀▀▀▀██▀▀▀██\n"
                     "█▒▒▒▒▒█▒▀▀▀▀▒█▒▒▒▒▒█\n"
                     "█▒▒▒▒▒█▒████▒█▒▒▒▒▒█\n"
                     "██▄▄▄██▄▄▄▄▄▄██▄▄▄██\n")


@register(outgoing=True, pattern='^.ikan(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("─▀▀▌───────▐▀▀\n"
                     "─▄▀░◌░░░░░░░▀▄\n"
                     "▐░░◌░▄▀██▄█░░░▌\n"
                     "▐░░░▀████▀▄░░░▌\n"
                     "═▀▄▄▄▄▄▄▄▄▄▄▄▀═\n")



@register(outgoing=True, pattern='^.siput(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("───▄▄▄\n"
                     "─▄▀░▄░▀▄\n"
                     "─█░█▄▀░█\n"
                     "─█░▀▄▄▀█▄█▄▀\n"
                     "▄▄█▄▄▄▄███▀\n")



@register(outgoing=True, pattern='^.hello(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("┈┈┈┈┈┈╱╱╱▕╲╱▏╲┈┈┈\n"
                      "┈┈┈┈┈▕╱╱╱▕╱╲▏╲▏┈┈\n"
                      "┈╭━╮┈▕╱╱╭╮╭╮╲╲▏┈┈\n"
                      "┈┃┈┗╮▕╱▏┳╭╮┳▕╲▏┈┈\n"
                      "┈┃┈╭╯▕┊╲╰━━╯╱┊▏┈┈\n"
                      "┈┣━┫┈▕┊┊▔▏▕▔┊┊▏┈┈\n"
                      "┏┓┏┳━━┳┓┏┓┏━━┓┏┓\n"
                      "┃┗┛┃━━┫┃┃┃┃╭╮┃┃┃\n"
                      "┃┏┓┃━━┫┗┫┗┫╰╯┃┗┛\n"
                      "┗┛┗┻━━┻━┻━┻━━┛┏┓\n"
                      "┈┈┈┈┈┈┈┈┈┈┈┈┈┈┗┛\n")


@register(outgoing=True, pattern='^.awkwok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`")


@register(outgoing=True, pattern='^.ular(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n")


@register(outgoing=True, pattern='^.y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n")


@register(outgoing=True, pattern='^.tank(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n")


@register(outgoing=True, pattern='^.babi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")


@register(outgoing=True, pattern='^.ajg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")


@register(outgoing=True, pattern='^.bernyanyi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ganteng Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")


@register(outgoing=True, pattern='^.kucing(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("──────▄▀▄─────▄▀▄\n"
                     "─────▄█░░▀▀▀▀▀░░█▄\n"
                     "─▄▄──█░░░░░░░░░░░█──▄▄\n"
                     "█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█\n")
    sleep(1)
    await typew.edit("░▄▄▄▄░\n"
                     "▀▀▄██►\n"
                     "▀▀███►\n"
                     "░▀███►░█►\n"
                     "▒▄████▀▀\n")
    sleep(1)
    await typew.edit("─────▀▄▀─────▄─────▄\n"
                     "──▄███████▄──▀██▄██▀\n"
                     "▄█████▀█████▄──▄█\n"
                     "███████▀████████▀\n"
                     "─▄▄▄▄▄▄███████▀\n")
    sleep(1)
    await typew.edit("─▀▀▌───────▐▀▀\n"
                     "─▄▀░◌░░░░░░░▀▄\n"
                     "▐░░◌░▄▀██▄█░░░▌\n"
                     "▐░░░▀████▀▄░░░▌\n"
                     "═▀▄▄▄▄▄▄▄▄▄▄▄▀═\n")
    sleep(1)
    await typew.edit("───▄▄▄\n"
                     "─▄▀░▄░▀▄\n"
                     "─█░█▄▀░█\n"
                     "─█░▀▄▄▀█▄█▄▀\n"
                     "▄▄█▄▄▄▄███▀\n")
    sleep(1)
    await typew.edit("░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n")
    sleep(1)
    await typew.edit("┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")
    sleep(1)
    await typew.edit("╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
    await asyncio.sleep(5)
    await event.delete()













CMD_HELP.update({
    "vip":
    "`.bulan` ; `.hati`\n`.bernyanyi` ; `.hewan`\
    \nUsage: animasi.\
    \n\n`.helikopter` ; `.tank` ; `.tembak`\n`.bundir` ; `.pistol` `.radio`\
    \nUsage: liat sendiri\
    \n\n`.y` ; `.hello`\
    \nUsage: liat sendiri\
    \n\n`.awkwok`\
    \nUsage: ketawa lari.\
    \n\n`.robot` ; `.ano` ; `.snowman`\n`.iblis` ;\
    \nUsage: art.\
    \n\n`.ular` ; `.babi` ; `.ajg`\n`.ikan` ; `.paus` ; `.siput`\n`.kucing` ; `.dinosaurus`\
    \nUsage: Bermacam - macam art hewan."
})
