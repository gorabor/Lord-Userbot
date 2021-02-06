# Better now - @its_xditya
# Based off plugin by @okay_retard && @hellboi_atul
# Alvin Gans

from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputMessagesFilterMusic
from userbot.events import register
from userbot import CMD_HELP

PROF = f"[нет](tg://user?id=828715391)"

# Alvin Gans
@register(outgoing=True, pattern=r"^\.musik(?: |$)(.*)")
async def _(event):
    try:
        await event.client(ImportChatInviteRequest("DdR2SUvJPBouSW4QlbJU4g"))
    except UserAlreadyParticipantError:
        pass
    except Exception as e:
        await event.edit(
            f"`Hmm.. Terjadi Kesalahan Yang Tidak Diketahui!\nMembatalkan...\nEr - {str(e)}`"
        )
        return
    name = event.pattern_match.group(1)
    if not name:
        await event.edit(
            "Terjadi Kesalahan `.musik Judul`\nPencarian Lebih Baik Gunakan, Artis - Judul Musik."
        )
        return
    chat = -1001271479322
    current_chat = event.chat_id
    current_msg = event.id
    cap = """
⫸ **Judul Musik** - `{}`
⫸ **Diunggah Dari** {}
"""
    try:
        async for event in userbot.iter_messages(
            chat, search=name, limit=1, filter=InputMessagesFilterMusic
        ):
            ok = cap.format(event.message, PROF)
            await userbot.delete_messages(current_chat, current_msg)
            await userbot.send_file(current_chat, event, caption=ok)
    except BaseException:
        await event.reply(
            f"`Maaf Lord Saya Tidak Menemukan Musik {name}. Untuk Pencarian Lebih Anda Bisa Menggunakan, Artis - Judul Lagu.`"
        )
        return


CMD_HELP.update({
    "musik":
    "`.musik` <Judul Musik>"
    "\nUsage: Dapatkan Musik Anda"
})
