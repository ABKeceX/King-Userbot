from time import sleep 
from userbot import CMD_HELP 
from userbot.events import register
import asyncio


@register(outgoing=True, pattern="^.team$")
async def team(e):
    await e.edit(
        "════════⚡𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════\n"
        "**Nama Creator Kami**\n"
        "╟◈🛠️ Developer : [Apis](t.me/PacarFerdilla) \n"
        "╟◈🛠️ Developer : [Abdul](t.me/lvufrvrbby) \n"
        "╟◈👤 Contributor : [Rimuru](t.me/imbakaaaaa) \n"
        "╰╼═══════════════════╾╯\n"
        "**Terimakasih Telah Menggunakan Project Userbot Kami 🙏 \n"
        "═════════⚡𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡═════════════\n"

CMD_HELP.update({ 'team'
`.team\n 
\nUsage: Santet Online Buat Bercanda Doang:).'})
