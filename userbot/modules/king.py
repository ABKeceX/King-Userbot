# import userbot by apis

from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern="^.king(?: |$)(.*)")
async def _(event):
    event.pattern_match.group(1)
    await event.edit(
        f"`Halo {ALIVE_NAME} Saya Adalah Bot Lord Yang Berada diAkun ini`"
        f"`Agar Terhindar Dari Orang Orang Random Di Telegram`"
        f"`Hai kakak manis, bolehkah mengirimkan pap tengktop xD`"
        f"\n---------------------------------------------------"
        f"\n\n**My King :** `{ALIVE_NAME}`")
        f"\n\n**My Lord :** `{ID} `")

CMD_HELP.update(
    {
        "king": "**✘ Plugin :** `King`\
        \n\n  •  **Perintah :** `.king`\
        \n  •  **Function : **Perkenalan Userbot King\
        \n\n  •  **Perintah :** `.sadboy`\
        \n  •  **Function : **Jadi sadboy:)\
        \n\n  •  **Perintah :** `.punten` | `.pantau`\
        \n  •  **Function : **Untuk punten dan pantau\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @PacarFerdilla Jika ingin mengidekan sesuatu yang menarik **\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @PacarFerdilla Jika ingin mengidekan sesuatu yang menarik **\
    "
    }
)
