import os
import re
from telethon import *
from userbot import bot
from userbot.utils import admin_cmd
from userbot import CMD_HELP

@bot.on(events.NewMessage(pattern="dm \.(.*)", outgoing=True))
async def _(event):
 
    d = dc.pattern_match.group(1)
    
    c = d.split(" ")

    chat_id = c[0]
    try:  #dc hehe
        chat_id = int(chat_id)
    #hmm 🤔🤔🤔🤔
    except BaseException:
        
        pass
  
    msg = ""
    masg = await dc.get_reply_message() 
    if dc.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await dc.edit("`✉ Lord Pesan Anda Sudah Terkirim ✉`")
    for i in c[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit("`✉ Lord Pesan Anda Sudah Terkirim ✉`")
    except BaseException:
        await dc.edit("Harap Lakukan Perintahnya Seperti Ini `.dm (username) (pesan)`")

CMD_HELP.update({"dm": "`.dm (username) (pesan)`\n atau\n .dm (username)(balas ke pesan)\n Itu akan meneruskan balasan pesan"})
