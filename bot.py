# BABAS #

# REPONU ƏKƏN ŞƏRƏFSİZDİ OĞRAŞDI #

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# start the bot
print("Başlanılır...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    FRWD_CHANNEL = config("FRWD_CHANNEL", cast=int)
    BotzHub = TelegramClient('BotzHub', apiid, apihash).start(bot_token=bottoken)
except:
    print("Ləvazımatlar tam deyil!")
    print("Bot söndürülür...")
    exit()

@BotzHub.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"Salam {ok.user.first_name}! \nMən **Canlı Söhbət** botuyam.\nMənə bir mesaj göndər və məndə o mesajı saniyəsində aşağıdakı Kanal'a göndərəcəm!!",
                    buttons=[
                        [Button.url("🤖 Sahibim", url="https://t.me/c9ala"),
                        Button.url("🗣️ Kanal", url="https://t.me/sohbetcanli")]
                    ])

@BotzHub.on(events.NewMessage(pattern="/help", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"{ok.user.first_name} kömək menyusuna xoş gəldin!\n\n🤖 Bot haqqında qısaca məlumat:\nSən mənə istədiyin bir mesajı yazırsan məndə həmin saniyə o mesajı @SohbetCanli kanalına yönləndirirəm! Sənin mesajını görən insanlarda bot vaistəsi ilə sənə cavab verəcək.\n\nTəklif və Şikayətlər üçün /feedback yaza bilərsiz.",
                    buttons=[
                        Button.url("🗣️ Kanal", url="https://t.me/sohbetcanli")
                    ])

@BotzHub.on(events.NewMessage(pattern="/feedback", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"Təklif və Şikayətlər üçün aşağıdakı bot butona basıb mənə yaza bilərsiz.",
                    buttons=[
                        Button.url("🤖 Sahib", url="https://t.me/c9ala")
                    ])

@BotzHub.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def countit(event):
    if event.text.startswith('/'):
        return
    x = await event.forward_to(FRWD_CHANNEL)
    await x.forward_to(event.chat_id)

print("bot başladı")
BotzHub.run_until_disconnected()
