import telethon
import asyncio
import json
from telethon import TelegramClient, events

async def start_event_handler(client,bot_token,chat_id):
    try:
        await client.start(bot_token=bot_token)
        @client.on(events.NewMessage(chats=chat_id))
        async def my_event_handler(event):
            if event.message.from_id.user_id == chat_id:
                if '#AD' in event.message.message or '#paidAD' in event.message.message or 'sponsored' in event.message.message:
                    await client.delete_messages(event.message.peer_id, event.message.id)
                    print('message deleted successfully')
                else:
                    print('failed')
                    pass
        client.add_event_handler(my_event_handler)
    except telethon.errors.rpcerrorlist.AccessTokenInvalidError:
        print("Invalid token, skipping")
        return

async def main():
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    tasks = []
    for token in tokens:
        bot_token = token["token"]
        chat_id = int(bot_token.split(':')[0])
        client = TelegramClient("Bot"+bot_token, "7243983", "e1bd137a37da9f95ecd2b206a8c8be48")
        tasks.append(start_event_handler(client,bot_token,chat_id))
    await asyncio.gather(*tasks)
    while True:
        await asyncio.sleep(0.01) # sleep for 30 seconds before checking for new

if __name__ == '__main__':
    asyncio.run(main())
