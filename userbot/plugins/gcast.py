
from PETERCORDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

from userbot import bot


@bot.on(admin_cmd(pattern=r"gcast"))
@bot.on(sudo_cmd(pattern=r"gcast", allow_sudo=True))
async def gcast(event):
    xx = event.pattern_match.group(1)
    if not xx:
        return await edit_or_reply(event, "`Berikan Saya Text Untuk Di Broadcast`")
    tt = event.text
    msg = tt[6:]
    kk = await edit_or_reply(event, "`• 📢 Global Broadcast Di Prosess Cok...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kk.edit(f"**╭✠╼━━━━━━❖━━━━━━━✠╮** Broadcast Terkirim Ke =** `{done}` **Grup, Broadcast Gagal Terkirim =** `{er}`**Grup**╰✠╼━━━━━━❖━━━━━━━✠╯**")

CmdHelp("gcast").add_command(
  'gcast', '<text>', 'Global broadcast ke semu grup yang dimasuki'
).add()
