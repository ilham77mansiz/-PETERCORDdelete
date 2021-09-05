from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from PETERCORDBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from telethon import events


@bot.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"gmute ?(\d+)?", allow_sudo=True))
async def blowjob(event):
    private = False
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    if user_id == (await borg.get_me()).id:	
        await edit_or_reply(event, "MELAKUKAN GMUTED")	
        	
        return
    elif event.is_private:
        await edit_or_reply(event, "`GLOBAL MUTED")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(event, "ABA KISI KO TAG TOO KARO KHA SAA AATA HAA YA LOG PATA NAHI 😂😂")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await edit_or_reply(event, "This retard cant speak. Was already gmutted earlier")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "GLOBAL MUTED")


@bot.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"ungmute ?(\d+)?", allow_sudo=True))
async def cumshot(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await edit_or_reply(event, "UNMUTED GLOBAL")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(event, "MEMAAFKAN PENGGUNA MERESAHKAN")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "😭 huaaa")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "BERHASIL UNGMUTED ")
        
@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
