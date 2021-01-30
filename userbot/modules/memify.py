import asyncio
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register

THUMB_IMAGE_PATH = "./thumb_image.jpg"


@register(outgoing=True, pattern=r"^\.mmf(?: |$)(.*)")
async def mim(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit(
            "Mohon Balas Ke Gambar Ketik `.mmf 'Teks Atas' ; 'Teks Bawah'` "
        )
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```Mohon Balas Ke Gambar/Sticker/Gif```")
        return
    reply_message.sender
    await bot.download_file(reply_message.media)
    if reply_message.sender.bot:
        await event.edit("```Balas ke pesan pengguna yang sebenarnya.```")
        return
    else:
        await event.edit(
            "```Mengubah Gambar Ini Mwahaha Saatnya Menulis ツ ```"
        )
        await asyncio.sleep(5)
        text = event.pattern_match.group(1)
        if event.reply_to_msg_id:
            file_name = "meme.jpg"
            reply_message = await event.get_reply_message()
            to_download_directory = TEMP_DOWNLOAD_DIRECTORY
            downloaded_file_name = os.path.join(
                to_download_directory, file_name)
            downloaded_file_name = await bot.download_media(
                reply_message,
                downloaded_file_name,
            )
            dls_loc = downloaded_file_name
        webp_file = await draw_meme_text(dls_loc, text)
        await event.client.send_file(
            event.chat_id, webp_file, reply_to=event.reply_to_msg_id
        )
        await event.delete()
        os.remove(webp_file)


async def draw_meme_text(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype(
        "userbot/utils/styles/MutantAcademyStyle.ttf", int(
            (70 / 640) * i_width)
    )
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=18):
            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(
                xy=(((i_width - u_width) / 2) - 1,
                    int((current_h / 730) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1,
                    int((current_h / 730) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2,
                    int(((current_h / 730) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2),
                    int(((current_h / 730) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 730) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=18):
            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((30 / 730) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((30 / 730) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((30 / 730) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((30 / 730) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((30 / 730) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad

    image_name = "memify.webp"
    webp_file = os.path.join(TEMP_DOWNLOAD_DIRECTORY, image_name)
    img.save(webp_file, "WebP")
    return webp_file


@register(outgoing=True, pattern=r"^\.mmf2(?: |$)(.*)")
async def mim(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit(
            "Mohon Balas Ke Gambar Ketik `.mmf2 'Teks Atas' ; 'Teks Bawah'` "
        )
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```Mohon Balas Ke Gambar/Sticker/Gif```")
        return
    reply_message.sender
    await bot.download_file(reply_message.media)
    if reply_message.sender.bot:
        await event.edit("```Balas Ke Pesan Pengguna Yang Sebenarnya.```")
        return
    else:
        await event.edit(
            "```Mengubah Gambar Ini Mwahaha Saatnya Menulis ツ ```"
        )
        await asyncio.sleep(5)
        text = event.pattern_match.group(1)
        if event.reply_to_msg_id:
            file_name = "meme.jpg"
            reply_message = await event.get_reply_message()
            to_download_directory = TEMP_DOWNLOAD_DIRECTORY
            downloaded_file_name = os.path.join(
                to_download_directory, file_name)
            downloaded_file_name = await bot.download_media(
                reply_message,
                downloaded_file_name,
            )
            dls_loc = downloaded_file_name
        webp_file = await draw_meme_text(dls_loc, text)
        await event.client.send_file(
            event.chat_id, webp_file, reply_to=event.reply_to_msg_id
        )
        await event.delete()
        os.remove(webp_file)


async def draw_meme_text(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype(
        "userbot/utils/styles/FontLord.ttf", int((95 / 730) * i_width)
    )
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=16):
            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 730) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 730) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 730) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 730) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 730) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=16):
            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((30 / 730) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((30 / 730) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((30 / 730) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((30 / 730) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((30 / 730) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad

    image_name = "memify.webp"
    webp_file = os.path.join(TEMP_DOWNLOAD_DIRECTORY, image_name)
    img.save(webp_file, "WebP")
    return webp_file

@register(outgoing=True, pattern="^.lordmmf(?: |$)(.*)")
async def mim(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("Mohon Balas Ke Gambar Ketik `.lordmmf 'teks atas' ; 'teks bawah'` ")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.edit("```Mohon Balas Ke Gambar/Sticker/Gif```")
       return
    chat = "@MemeAutobot"
    sender = reply_message.sender
    file_ext_ns_ion = "@memetime.png"
    file = await bot.download_file(reply_message.media)
    uploaded_gif = None
    if reply_message.sender.bot:
       await event.edit("```Balas Ke Pesan Pengguna Yang Sebenarnya.```")
       return
    else:
     await event.edit("```Mengubah Gambar Ini Mwahaha Saatnya Menulis ツ```")
     await asyncio.sleep(5)
    
    async with bot.conversation("@MemeAutobot") as bot_conv:
          try:
            memeVar = event.pattern_match.group(1)
            await silently_send_message(bot_conv, "/start")
            await asyncio.sleep(1)
            await silently_send_message(bot_conv, memeVar)
            await bot.send_file(chat, reply_message.media)
            response = await bot_conv.get_response()
          except YouBlockedUserError: 
              await event.reply("```Mohon Buka Blokir @MemeAutobot Dan Coba Lagi```")
              return
          if response.text.startswith("Forward"):
              await event.edit("```Mohon Maaf Lord, Bisakah Anda Membuka Pengaturan Privasi Forward/Pesan Terusan Anda?```")
          if "Okay..." in response.text:
            await event.edit("```Mohon Maaf Lord Ini Bukan Gambar ヅ```")
            thumb = None
            if os.path.exists(THUMB_IMAGE_PATH):
                thumb = THUMB_IMAGE_PATH
            input_str = event.pattern_match.group(1)
            if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
                os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
            if event.reply_to_msg_id:
                file_name = "meme.png"
                reply_message = await event.get_reply_message()
                to_download_directory = TEMP_DOWNLOAD_DIRECTORY
                downloaded_file_name = os.path.join(to_download_directory, file_name)
                downloaded_file_name = await bot.download_media(
                    reply_message,
                    downloaded_file_name,
                    )
                if os.path.exists(downloaded_file_name):
                    await bot.send_file(
                        chat,
                        downloaded_file_name,
                        force_document=False,
                        supports_streaming=False,
                        allow_cache=False,
                        thumb=thumb,
                        )
                    os.remove(downloaded_file_name)
                else:
                    await event.edit("File Tidak Ditemukan {}".format(input_str))
            response = await bot_conv.get_response()
            the_download_directory = TEMP_DOWNLOAD_DIRECTORY
            files_name = "memes.webp"
            download_file_name = os.path.join(the_download_directory, files_name)
            await bot.download_media(
                response.media,
                download_file_name,
                )
            requires_file_name = TEMP_DOWNLOAD_DIRECTORY + "memes.webp"
            await bot.send_file(  # pylint:disable=E0602
                event.chat_id,
                requires_file_name,
                supports_streaming=False,
                caption="Memifyed",
            )
            await event.delete()
            #await bot.send_message(event.chat_id, "`Yare - Yare`")
          elif not is_message_image(reply_message):
            await event.edit("`Pesan Tidak Valid, Harap Pilih Pesan Yang Valid Lord.`")
            return
          else: 
               await bot.send_file(event.chat_id, response.media)

def is_message_image(message):
    if message.media:
        if isinstance(message.media, MessageMediaPhoto):
            return True
        if message.media.document:
            if message.media.document.mime_type.split("/")[0] == "image":
                return True
        return False
    return False
    
async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response

CMD_HELP.update({
    "memify":
        "`.mmf` atau `mmf2` Teks Atas ; Teks Bawah\
        \nUsage: Balas Ke Sticker/Gambar/Gif.\n"
        "`.lordmmf` Teks Atas ; Teks Bawah\
        \nUsage: Balas Ke Sticker/Gambar/Gif."
})
