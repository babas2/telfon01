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
    await event.reply(f"Salam {ok.user.first_name} ! Mən Elan botuyam. Mənə satmaq istədiyin şeyin şəklini (qrup, kanal, əşya və s.) göndər məndə onu avtomatik aşağıdakı kanala yönləndirəcəm. **BAŞLAMADAN ƏVVƏL MÜTLƏQ /help YAZ** !",
                    buttons=[
                        [Button.url("🤖 Sahibim", url="https://t.me/c9ala"),
                        Button.url("🗣️ Kanal", url="https://t.me/elanver")
                    ])

@BotzHub.on(events.NewMessage(pattern="/help", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"{ok.user.first_name} kömək menyusuna xoş gəldin!\n\n🤖 Bot haqqında qısaca məlumat:\nSən mənə satmaq istədiyin şeyin şəklini (qrup, kanal, əşya və s.) göndərirsən və məndə onu avtomatik @ElanVer kanalına yönləndirirəm.\n\n**VACİB**:\n1 - Elanını paylaşarkən onun haqqında tam məlumat verməyi unutma (ünvan, qiymət, əlaqə və s.)\n2 - 18+ ,qanunsuz, qeyri-etik elanlar paylaşmaq qadağandır.\n\n✍️ Qeyd: Elan paylaşılarkən kim tərəfindən göndərildiyi kanalda göstərilir, yəniki nələr paylaşdığın sənin "tərbiyyəndən" aslıdır :)",
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
