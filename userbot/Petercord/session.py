from telethon.sessions import StringSession
from telethon import TelegramClient
from var import Var



if Var.STRING_SESSION:
    session_name = str(Var.STRING_SESSION)
    Petercord = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
else:
    session_name = "startup"
    Petercord = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
