"""Add the user(s) to the current chat
Syntax: .edd <User(s)>"""

from telethon import functions
from userbot.utils import admin_cmd
from PETERCORDBOT import CMD_HELP

@borg.on(admin_cmd(pattern="masuk ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("`.add` users to a chat, don't use this in PM")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("SAYA JOIN WKWK.")
        else:
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("WKWK KECULIK HAHAHA.")
CMD_HELP.update(
    {
        "adduser": 
    ".masuk <username>"
    "\nAdd the username in the grp/channel where u type."
    })
