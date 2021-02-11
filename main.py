from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 2942575
api_hash = '742735ff0f8b0e6c3e6153ab4bcd2bb3'
# 1625942892:AAHa52g-krqaqkiIxLNv9UV_ZZNdjeRZwNY
client = TelegramClient(StringSession("1ApWapzMBu6oZjd2igalo0i3TiJbKqa-L01W9FgNSSo9yuhP5sXLdAF62XfxTcuAxjke3nm6cngPcDTiZ9YMx81gjPVO5MlVfgfpT1_aAV4Ef3KyZ1Fd6TiUwQblWdrj-AvFd9luZRxMRsK5Q1paFv-4snWaS_4LC8JhLcCCw74KN9eGuKQvOWvyoiOOzrQlSdOeMoVsd2p2dmRieUOP_SqHsX2eDEN4DBZ-gPleT7WTJI3AMt4Pb7_oaMX7Fv5csOETXKsfcFOx7ur4lxILz0y8n_9acZPv2_ceFXuZuYXEvfOkOxM6aR9lUgo6u4LYn7wh17C5Z-87aAJQehRGRURw8WRD_eVg="), api_id, api_hash)
client.start()    
print(client.session.save())
#+970569937656
# client.run_until_disconnected()
# async def main():
#     # You can print the message history of any chat:
#     async for message in client.iter_messages('utsavstha'):
#         if message.text is None:
#             continue 
#         elif "profit" in message.text:
#CPLleaks
#                 print(message.sender.username, message.text)


@client.on(events.NewMessage(chats="shehabtelegram"))
async def my_event_handler(event):
    print("new event")
    if "حماس" in event.raw_text or "غزة" in event.raw_text or "فلسطين" in event.raw_text or "فلسطيني" in event.raw_text or "فلسطينيين" in event.raw_text or "فلسطينيون" in event.raw_text or "الموطن الفلسطيني" in event.raw_text or "وطنية" in event.raw_text or "قطاع غزة" in event.raw_text or "أزمة" in event.raw_text or "حصار" in event.raw_text or "جهاد" in event.raw_text or "جهاد اسلامي فلسطيني" in event.raw_text or "اسلام" in event.raw_text:
            print("Posted from shehabtelegram")
            await client.send_message('alshabakia', event.raw_text)
            await client.send_message('CPLleaks', event.raw_text)

@client.on(events.NewMessage(chats="gazanewsnow"))
async def my_event_handler(event):
    print("new event")
    if "حماس" in event.raw_text or "غزة" in event.raw_text or "فلسطين" in event.raw_text or "فلسطيني" in event.raw_text or "فلسطينيين" in event.raw_text or "فلسطينيون" in event.raw_text or "الموطن الفلسطيني" in event.raw_text or "وطنية" in event.raw_text or "قطاع غزة" in event.raw_text or "أزمة" in event.raw_text or "حصار" in event.raw_text or "جهاد" in event.raw_text or "جهاد اسلامي فلسطيني" in event.raw_text or "اسلام" in event.raw_text:
            print("Posted from gazanewsnow")
            await client.send_message('alshabakia', event.raw_text)
            await client.send_message('CPLleaks', event.raw_text)

@client.on(events.NewMessage(chats="khnmedia"))
async def my_event_handler(event):
    print("new event")
    if "حماس" in event.raw_text or "غزة" in event.raw_text or "فلسطين" in event.raw_text or "فلسطيني" in event.raw_text or "فلسطينيين" in event.raw_text or "فلسطينيون" in event.raw_text or "الموطن الفلسطيني" in event.raw_text or "وطنية" in event.raw_text or "قطاع غزة" in event.raw_text or "أزمة" in event.raw_text or "حصار" in event.raw_text or "جهاد" in event.raw_text or "جهاد اسلامي فلسطيني" in event.raw_text or "اسلام" in event.raw_text:
            print("Posted from khnmedia")
            await client.send_message('alshabakia', event.raw_text)
            await client.send_message('CPLleaks', event.raw_text)

@client.on(events.NewMessage(chats="ajanews"))
async def my_event_handler(event):
    print("new event")
    if "حماس" in event.raw_text or "غزة" in event.raw_text or "فلسطين" in event.raw_text or "فلسطيني" in event.raw_text or "فلسطينيين" in event.raw_text or "فلسطينيون" in event.raw_text or "الموطن الفلسطيني" in event.raw_text or "وطنية" in event.raw_text or "قطاع غزة" in event.raw_text or "أزمة" in event.raw_text or "حصار" in event.raw_text or "جهاد" in event.raw_text or "جهاد اسلامي فلسطيني" in event.raw_text or "اسلام" in event.raw_text:
            print("Posted from ajanews")
            await client.send_message('alshabakia', event.raw_text)
            await client.send_message('CPLleaks', event.raw_text)

@client.on(events.NewMessage(chats="gazaalannet"))
async def my_event_handler(event):
    print("new event")
    if "حماس" in event.raw_text or "غزة" in event.raw_text or "فلسطين" in event.raw_text or "فلسطيني" in event.raw_text or "فلسطينيين" in event.raw_text or "فلسطينيون" in event.raw_text or "الموطن الفلسطيني" in event.raw_text or "وطنية" in event.raw_text or "قطاع غزة" in event.raw_text or "أزمة" in event.raw_text or "حصار" in event.raw_text or "جهاد" in event.raw_text or "جهاد اسلامي فلسطيني" in event.raw_text or "اسلام" in event.raw_text:
            print("Posted from gazaalannet")
            await client.send_message('alshabakia', event.raw_text)
            await client.send_message('CPLleaks', event.raw_text)


with client:
    client.run_until_disconnected()


