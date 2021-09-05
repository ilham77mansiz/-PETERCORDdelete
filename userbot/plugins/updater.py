import asyncio
import os
import sys

import git

from userbot.Config import Config
from PETERCORDBOT.utils import admin_cmd, sudo_cmd


"""
This module updates the userbot based on upstream revision
"""

from os import remove, execle, path, environ
import asyncio
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError



requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt')


async def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'•[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            ' '.join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if Config.HEROKU_API_KEY is not None:
        import heroku3
        heroku = heroku3.from_key(Config.HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if Config.HEROKU_APP_NAME is None:
            await event.edit(
                '`[HEROKU]: Harap Siapkan Variabel` **HEROKU_APP_NAME** `'
                ' untuk dapat deploy perubahan terbaru dari 🛡PETERCORD USERBOT🛡.`'
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == Config.HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(
                f'{txt}\n`Kredensial Heroku tidak valid untuk deploy 🛡PETERCORD USERBOT🛡 dyno.`'
            )
            return repo.__del__()
        await event.edit('`[HEROKU]:'
                         '\nDyno 🛡PETERCORD USERBOT🛡 Sedang Dalam Proses, Mohon Menunggu 7-8 Menit`'
                         )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + Config.HEROKU_API_KEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await event.edit(f'{txt}\n`Terjadi Kesalahan Di Log:\n{error}`')
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit(
                "`Build Gagal!\n" "Dibatalkan atau ada beberapa kesalahan...`"
            )
            await asyncio.sleep(5)
            return await event.delete()
        else:
            await event.edit("`🛡PETERCORD USERBOT🛡 Berhasil Di Deploy!\n" "Restarting, Mohon Menunggu Petercord.....`")
            await asyncio.sleep(15)
            await event.delete()

async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await event.edit('**🛡 PETERCORD USERBOT** `Berhasil Di Update!`')
    await asyncio.sleep(1)
    await event.edit('**🛡 PETERCORD USERBOT** `Di Restart....`')
    await asyncio.sleep(1)
    await event.edit('`Mohon Menunggu Beberapa Detik 🛡PETERCORD USERBOT🛡 ツ`')
    await asyncio.sleep(10)
    await event.delete()

args = [sys.executable, "-m", "userbot"]
    


@borg.on(admin_cmd("update(?: |$)(now|deploy)?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="update(?: |$)(now|deploy)?(.*)", allow_sudo=True))
async def upstream(event):
    "For .update command, check if the bot is up to date, update if specified"
    await event.edit("`Mengecek Pembaruan, Silakan Menunggu....`")
    conf = event.pattern_match.group(1)
    off_repo = Config.UPSTREAM_REPO_URL
    force_update = False
    try:
        txt = "`Maaf Petercord Pembaruan Tidak Dapat Di Lanjutkan Karna "
        txt += "Beberapa Masalah Terjadi`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f'{txt}\n`Directory {error} Tidak Dapat Di Temukan`')
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f'{txt}\n`Gagal Awal! {error}`')
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`Sayangnya, Directory {error} Tampaknya Bukan Dari Repo."
                "\nTapi Kita Bisa Memperbarui Paksa Userbot Menggunakan .update now.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != Config.UPSTREAM_REPO_BRANCH:
        await event.edit(
            '**[UPDATER]:**\n'
            f'`Looks like you are using your own custom branch ({ac_br}). '
            'in that case, Updater is unable to identify '
            'which branch is to be merged. '
            'please checkout to any official branch`')
        return repo.__del__()
    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f'HEAD..upstream/{ac_br}')

    if changelog == '' and force_update is False:
        await event.edit(
            f'\n**🛡 Petercord-Userbot Sudah Versi Terbaru**\n')
        await asyncio.sleep(15)
        await event.delete()
        return repo.__del__()

    if conf is None and force_update is False:
        changelog_str = f'**🛡 Pembaruan Untuk 🔮PETERCORD USERBOT🔮 [{ac_br}]:\n\n🛡 Pembaruan:**\n`{changelog}`'
        if len(changelog_str) > 4096:
            await event.edit("`Changelog Terlalu Besar, Lihat File Untuk Melihatnya.`")
            file = open("output.txt", "w+")
            file.write(changelog_str)
            file.close()
            await event.client.send_file(
                event.chat_id,
                "output.txt",
                reply_to=event.id,
            )
            remove("output.txt")
        else:
            await event.edit(changelog_str)
        return await event.respond('**Perintah Untuk Update 🛡Petercord Userbot🛡**\n >`.update now`\n >`.update deploy`\n\n__Untuk Meng Update Fitur Terbaru Dari Petercord Userbot.__')

    if force_update:
        await event.edit(
            '`Sinkronisasi Paksa Ke Kode Userbot Stabil Terbaru, Harap Tunggu .....`')
    else:
        await event.edit('`🔮 Proses Update Petercord-Userbot, Loading....1%`')
        await event.edit('`🎻 Proses Update Petercord-Userbot, Loading....20%`')
        await event.edit('`🎸 Proses Update Petercord-Userbot, Loading....35%`')
        await event.edit('`🥁 Proses Update Petercord-Userbot, Loading....77%`')
        await event.edit('`🎸 Proses Update Petercord-Userbot, Updating...90%`')
        await event.edit('`🔮 Proses Update Petercord-Userbot, Mohon Menunggu Petercord....100%`')
    if conf == "now":
        await update(event, repo, ups_rem, ac_br)
        await asyncio.sleep(10)
        await event.delete()
    elif conf == "deploy":
        await deploy(event, repo, ups_rem, ac_br, txt)
        await asyncio.sleep(10)
        await event.delete()
    return

