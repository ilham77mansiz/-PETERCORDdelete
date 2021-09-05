from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from PETERCORDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

from asyncio.exceptions import TimeoutError


@bot.on(admin_cmd(pattern="sa(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="sa(?: |$)(.*)", allow_sudo=True))
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Mohon Balas Ke Pesan Pengguna Petercord.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```Balas Ke Pesan Pengguna Yang Sebenarnya.```")
        return
    await steal.edit("```Petercord Memerintahku Mengambil Informasi Riwayat Pergantian Nama Orang Ini ツ```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Petercord Mohon Unblock @sangmatainfo_bot Dan Coba Lagi```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"`{r.message}`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("```Saya Tidak Menemukan Informasi Pergantian Nama, Petercord Orang Ini Belum Pernah Mengganti Namanya ツ```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"```{response.message}```")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Saya Sedang Sakit Petercord Maaf`")


CmdHelp("sangmata").add_command(
  'sa', 'balas ke pengguna', 'Menemukan riwayat nama pengguna.'
).add()
