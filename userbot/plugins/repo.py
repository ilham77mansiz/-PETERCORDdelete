
import asyncio
from collections import deque

from telethon.tl.functions.users import GetFullUserRequest

from userbot import *
from PETERCORDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern=f"repo", outgoing=True))
@bot.on(sudo_cmd(pattern=f"repo", allow_sudo=True))
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await edit_or_reply(e, "╭┄┅┯┅┄┄┅┯┅┄╮**\n\n [𝗣 𝗘 𝗧 𝗘 𝗥 𝗖 𝗢 𝗥 𝗗](https://github.com/IlhamMansiez/PETERCORDBOT)\n\n [𝗢 𝗪 𝗡 𝗘 𝗥 𝗦](t.me/diemmmmmmmmmm)\n\n [GRUP SUPPORT](https://t.me/TEAMSquadUserbotSupport)\n\n**╰┄┅┷┅┄┄┅┷┅┄╯**\n")


CmdHelp("repo").add_command(
  'repo', None, 'Menapilkan repo bot'
).add()
