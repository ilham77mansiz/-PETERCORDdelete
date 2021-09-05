#Ilham mansiez
#PetercordBot

from math import ceil
from re import compile
import asyncio

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from PETERCORDBOT.utils import *
from userbot.Config import Config

PETERCORD_row = Config.BUTTONS_IN_HELP
PETERCORD_emoji = Config.EMOJI_IN_HELP
# Petercord
# PETERCORD

def button(page, modules):
    Row = PETERCORD_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"💐 " + pair, data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"◀", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"𝗖𝗟𝗢𝗦𝗘", data="close"
            ),
            custom.Button.inline(
               f"▶", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in PETERCORDBOT channel to get this module work...

    modules = CMD_HELP
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@TEAMSquadUserbotSupport":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            result = await builder.article(
                f"Hey! Only use .help please",
                text=f"**𝐌𝐔𝐋𝐀𝐈 𝐏𝐄𝐓𝐄𝐑𝐂𝐎𝐑𝐃**\n\n 𝐉𝐔𝐌𝐋𝐀𝐇 𝐏𝐋𝐔𝐆𝐈𝐍𝐒 𝐓𝐄𝐑𝐒𝐄𝐃𝐈𝐀 :`{len(CMD_HELP)}`\n**𝗛𝗔𝗟𝗔𝗠𝗔𝗡:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        elif event.text=='':
            result = builder.article(
                "@TEAMSquadUserbotSupport",
                text="""**Hey! This is [PETERCORDBOT.](https://t.me/TEAMSquadUserbotSupport) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CHANNEL 🔥", "https://t.me/TEAMSquadUserbotSupport"),
                        custom.Button.url(
                            "⚡ GROUP ⚡", "https://t.me/TEAMSquadUserbotSupport"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "✨ REPO ✨", "https://github.com/IlhamMansiez/PETERCORDBOT"),
                        custom.Button.url
                    (
                            "🔰 TUTORIAL 🔰", ""
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN PETERCORDBOT AND USE. © PETERCORDBOT ™",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        await event.edit(
            f"**𝗣𝗘𝗧𝗘𝗥𝗖𝗢𝗥𝗗 𝗨𝗦𝗘𝗥𝗕𝗢𝗧\n\n┏━━━━━━━━━━━━━━━━━━━\n┗━━━━━━━━━━━━━━━━━━━ \n\n𝐑𝐄𝐏𝐎 𝗣𝗘𝗧𝗘𝗥𝗖𝗢𝗥𝗗 𝗣𝗟𝗨𝗚𝗜𝗡𝗦**\n[𝗦𝗨𝗣𝗣𝗢𝗥𝗧](https://t.me/TEAMSquadUserbotSupport)\n𝗕𝗘𝗥𝗝𝗔𝗟𝗔𝗡\n\n**𝗝𝗨𝗠𝗟𝗔𝗛 𝗣𝗟𝗨𝗚𝗜𝗡𝗦 𝗧𝗘𝗥𝗦𝗘𝗗𝗜𝗔 :** `{len(CMD_HELP)}`\n**𝗛𝗔𝗟𝗔𝗠𝗔𝗡:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )
        
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
              "💐PETERCORDBOT Menu Provider Is now Closed💐\n\n         **[© PETERCORDBOT ™](https://t.me/TEAMSquadUserbotSupport)**", 5, link_preview=False
            )
        else:
            PETERCORD_alert = "HELLO THERE. PLEASE MAKE YOUR OWN PETERCORDBOT AND USE. © PETERCORDBOT ™"
            await event.answer(PETERCORD_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN PETERCORDBOT AND USE. © PETERCORDBOT ™",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "⚡ " + cmd[0], data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("◀", data=f"page({page})")])
        await event.edit(
            f"**┏━━━━━━━━━━━━━━━━━**\n File:** `{commands}`\n**┗━━━━━━━━━━━━━━━━━**\n\n**┏━━━━━━━━━━━━━━━━━**\n Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`\n┗━━━━━━━━━━━━━━━━━",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "HELLO THERE. PLEASE MAKE YOUR OWN PETERCORDBOT AND USE. © PETERCORDBOT ™",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**┏━━━━━━━━━━━━━━━━━\n File:** `{cmd}`\n┗━━━━━━━━━━━━━━━━━\n\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**┏━━━━━━━━━━━━━━━━━\n Terdata:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n┗━━━━━━━━━━━━━━━━━\n"
                result += f"**❌ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**┏━━━━━━━━━━━━━━━━━\n Terdata:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n┗━━━━━━━━━━━━━━━━━\n"
        else:
            result += f"**┏━━━━━━━━━━━━━━━━━\n Terdata:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n┗━━━━━━━━━━━━━━━━━\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**❌ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ🎖 Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**┏━━━━━━━━━━━━━━━━━**\n Commands: `{COMMAND_HAND_LER[:1]}{command['command']}`\n┗━━━━━━━━━━━━━━━━━\n"
        else:
            result += f"**┏━━━━━━━━━━━━━━━━━**\n Commands: `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n┗━━━━━━━━━━━━━━━━━\n"

        if command["example"] is None:
            result += f"**┏━━━━━━━━━━━━━━━━━\n Explanation:** `{command['usage']}`\n┗━━━━━━━━━━━━━━━━━\n"
        else:
            result += f"**┏━━━━━━━━━━━━━━━━━\n Explanation:** `{command['usage']}`\n┗━━━━━━━━━━━━━━━━━\n"
            result += f"**┏━━━━━━━━━━━━━━━━━\n For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n┗━━━━━━━━━━━━━━━━━\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("◀", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )


# Ask owner before using it in your codes
# Kangers like LB stay away...
#TENTANG AKU DAN DIA
