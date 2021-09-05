# thanks to @Skastickers for stickers....
# Among us.....
# credits to Ilham mansiez


import asyncio
from userbot.cmdhelp import CmdHelp

from userbot import *
from PETERCORDBOT.utils import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "PETERCORD"


@bot.on(admin_cmd(pattern="imp(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="imp(|n) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    h1m4n5hu0p = bot.uid
    USERNAME = f"tg://user?id={h1m4n5hu0p}"
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    text1 = await edit_or_reply(event, "Hmm... Sepertinya ada yang salah di sini🤔🧐!!")
    await asyncio.sleep(2)
    await text1.delete()
    stcr1 = await event.client.send_file(
        event.chat_id, "CAADAQADRwADnjOcH98isYD5RJTwAg"
    )
    text2 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Saya sedang berdiskusi sekarang"
    )
    await asyncio.sleep(3)
    await stcr1.delete()
    await text2.delete()
    stcr2 = await event.client.send_file(
        event.chat_id, "CAADAQADRgADnjOcH9odHIXtfgmvAg"
    )
    text3 = await event.reply(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Kita harus mengeluarkan penipu itu atau akan kalah :) "
    )
    await asyncio.sleep(3)
    await stcr2.delete()
    await text3.delete()
    stcr3 = await event.client.send_file(
        event.chat_id, "CAADAQADOwADnjOcH77v3Ap51R7gAg"
    )
    text4 = await event.reply(f"**Boncel :** Dimana Astaga hiks ")
    await asyncio.sleep(2)
    await text4.edit(f"**Boncel :** Siapa itu? ")
    await asyncio.sleep(2)
    await text4.edit(
        f"**[{DEFAULTUSER}]({USERNAME}) :** Ok Boncel , Kita bantai nanti {name}  Aku pukul kepalanya,"
    )
    await asyncio.sleep(3)
    await text4.edit(f"**Boncel kita tebas :**Okay.. setuju gak? {name} ")
    await asyncio.sleep(2)
    await stcr3.delete()
    await text4.delete()
    stcr4 = await event.client.send_file(
        event.chat_id, "CAADAQADLwADnjOcH-wxu-ehy6NRAg"
    )
    PETERCORDevent = await event.reply(f"{name} Gamau ya yaudah aku diam aja hiks.......🤐")
    await asyncio.sleep(2)
    await PETERCORDevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.5)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    await stcr4.delete()
    if cmd == "":
        await PETERCORDevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} Dia menggila.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Makin menggila    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await PETERCORDevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADLQADnjOcH39IqwyR6Q_0Ag")
    elif cmd == "n":
        await PETERCORDevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ{name} Dia mulai sange wkwk.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Beneran dia sange tapi gada cewek yang mau dimainin hiks selesai   　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
        await asyncio.sleep(4)
        await PETERCORDevent.delete()
        await event.client.send_file(event.chat_id, "CAADAQADQAADnjOcH-WOkB8DEctJAg")


@bot.on(admin_cmd(pattern="timp(|n) (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="timp(|n) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    PETERCORDevent = await edit_or_reply(event, f"{name} is ejected.......")
    await asyncio.sleep(2)
    await PETERCORDevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.8)
    await PETERCORDevent.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    if cmd == "":
        await PETERCORDevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} ini orang  sangeean.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         0 Penjahat kelamin   　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )
    elif cmd == "n":
        await PETERCORDevent.edit(
            f". 　　　。　　　　•　 　ﾟ　　。 　　.\n .　　　 　　.　　　　　。　　 。　. 　\n\n  . 　　 。   　     ඞ         。 . 　　 • 　　　　•\n\n  ﾟ {name} sangean hati2 kalian buat para cewek.      。　. 　 　       。　.                                        。　. \n                                   　.          。　  　. \n　'         1 Penjahat kelamin   　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。\n　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"
        )


CmdHelp("amongus").add_command(
  'imp', 'Name/username', 'Menemukan penipu dengan stiker. Penipu-Benar'
).add_command(
  'impn', 'Name/Username', 'Menemukan penipu dengan stiker. Penipu-Salah'
).add_command(
  'timp', 'name/username', 'Menemukan penipu tanpa stiker (Hanya teks). Penipu - Benar'
).add_command(
  'timpn', 'name/username', 'Menemukan penipu tanpa stiker (Hanya teks). Penipu - Salah'
).add()
