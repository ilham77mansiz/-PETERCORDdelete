import asyncio
from datetime import datetime

from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from ..cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PETERCORD User"
h1m4n5hu0p = borg.uid



@bot.on(admin_cmd(pattern="ping$", outgoing=True))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "__**(❛ ᑭσɳց ❜!__**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"┏━━━━━━━━━━━━━━━━━\n__**꧁ PING ꧂__**\n\n   ⚘ ➳➠UPTIME: {ms}\n   ⚘ ➳➠__**PENGGUNA**__: [{DEFAULTUSER}](tg://user?id={h1m4n5hu0p})\n┗━━━━━━━━━━━━━━━━━"
    )


CmdHelp("ping").add_command(
  "ping", None, "Shows you the ping speed of server"
).add_command(
  "hbping", None, "Shows you the ping speed of server with an animation"
).add()
