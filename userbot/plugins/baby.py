# 
# Tentang aku dan dia

import random, re
from PETERCORDBOT.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="sayang ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""HEYY Sayang, AKU SANGE MAU DING SEKALI AJA PLIS HIKS:) """)
        

