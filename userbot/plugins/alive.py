 
# Made by @diemmmmmmmmmm
# Porting in PETERCORD Userbot by @diemmmmmmmmmm

from telethon import __version__, version
from platform import python_version
from userbot.Config import Config
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import *
from PETERCORDBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# TENTANG AKU DAN DIA
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Petercord Userbot"

# alive.py for @diemmmmmmmmmm

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

PETERCORD = bot.uid



""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b52e42266a323cbe9f849.jpg"
file2 = "https://telegra.ph/file/b52e42266a323cbe9f849.jpg"
file3 = "https://telegra.ph/file/e4142fc1d14bc3c8181a3.jpg"
file4 = "https://telegra.ph/file/2d2a335d26a0d33a1e385.jpg"
""" =======================CONSTANTS====================== """

    
@Petercord.on(admin_cmd(outgoing=True, pattern="alive$"))
@Petercord.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    output = (
        f"**🪐 PETERCORD USERBOT 🪐** \n"
        f"┏━━━━━━━━━━━━━━━━━━━ \n"
        f"┣|⚡ `Petercord:`{DEFAULTUSER} \n"
        f"┣|⚡ `Telethon :`Ver {version.__version__} \n"
        f"┣|⚡ `Python   :`Ver {python_version()} \n"
        f"┣|⚡ `Branch   :`{Config.UPSTREAM_REPO_BRANCH} \n"
        f"┣|⚡ `Bot Ver  :`{PETERCORDversion} \n"
        f"┣|⚡ `Sudo     :`{ludosudo} \n"
        f"┣|⚡ `Modules  :`{len(CMD_HELP)} Modules \n"
        f"┗━━━━━━━━━━━━━━━━━━━ \n\n")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=output)
            await asyncio.sleep(500)
            await msg.delete()
        except BaseException:
            await alive.edit(
                output + "\n\n *`Logo Yang Disediakan Tidak Valid."
                "\nPastikan Tautan Yang Anda Gunakan Valid`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(output)
        await asyncio.sleep(100)
        await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Menampilkan logo Bot.'
).add()
