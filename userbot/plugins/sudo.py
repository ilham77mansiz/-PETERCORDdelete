
from userbot import *
from PETERCORDBOT.utils import *
from userbot.cmdhelp import CmdHelp

import heroku3
from telethon.tl.functions.users import GetFullUserRequest

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = Config.SUDO_USERS



@bot.on(admin_cmd(pattern="sudo"))
async def sudo(event):
    sudo = "True" if Config.SUDO_USERS else "False"
    users = Config.SUDO_USERS
    if sudo == "True":
        await edit_or_reply(event, f"**Petercord Userbot mengaktifkan**\nSudo - `Menyala`\nSudo user(s) - `{users}`")
    else:
        await edit_or_reply(event, f"**Petercord Userbot menonaktifkan**\nSudo - `Tidak Aktif`")


@bot.on(admin_cmd(pattern="cmdhelp"))
async def handler(event):
    hndlr = Config.COMMAND_HAND_LER

    sudohndlr = Config.SUDO_COMMAND_HAND_LER
    await edit_or_reply(event, f"Command Handler - {hndlr}\nSudo Handler - {sudohndlr}")


@bot.on(admin_cmd(pattern="addsudo"))
async def tb(event):
    ok = await edit_or_reply(event, "Menambahkan sudo...")
    petercord = "SUDO_USERS"
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        target = await get_user(event)
    except Exception:
        await ok.edit(f"Reply to a user.")
    if sudousers:
        newsudo = f"{sudousers} {target}"
    else:
        newsudo = f"{target}"
    await ok.edit(f"Added `{target}` Sudo telah aktif mohon. Restarting.. tunggu beberapa minute...")
    heroku_var[petercord] = newsudo


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
