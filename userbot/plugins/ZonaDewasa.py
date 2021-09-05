# credits to userge
# ported to PETERCORDBOT by ILHAM MANSIEZ
# will be adding more soon
#TENTANG AKU DAN DIA

import asyncio
import os
import urllib

import requests

from userbot import *
from PETERCORDBOT.utils import *
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd("payudara$"))
@bot.on(sudo_cmd(pattern="payudara$", allow_sudo=True))
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Menemukan beberapa payudara besar untukmu 😂")
    await asyncio.sleep(0.5)
    await a.edit("Ini besar banget nih 😂")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@bot.on(admin_cmd("pantat$"))
@bot.on(sudo_cmd(pattern="pantat$", allow_sudo=True))
async def butts(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("Menemukan beberapa pantat yang indah untuk Anda 🧐")
    await asyncio.sleep(0.5)
    await a.edit("Mengirim beberapa pantat yang indah 😂")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()

CmdHelp("zonadewasa").add_command(
  'payudara', None, 'Mengirim gambar payudara acak'
).add_command(
  'pantat', None, 'Mengirim gambar pantat acak'
).add()
