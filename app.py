import json
from concurrent.futures import ThreadPoolExecutor
import time
from telethon import TelegramClient, events
import telethon
import asyncio

async def main():
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    for token in tokens:
        bot_token = token["token"]
        chat_id = int(bot_token.split(':')[0])
        asyncio.create_task(run_client(bot_token, chat_id))
    while True:
        await asyncio.sleep(10)

async def run_client(bot_token, chat_id):
    while True:
        try:
            client = TelegramClient('Sot', "7243983", "e1bd137a37da9f95ecd2b206a8c8be48")
            await client.start(bot_token=bot_token)

            @client.on(events.NewMessage(chats=chat_id))
            async def my_event_handler(event):
                if event.message.from_id.user_id == chat_id:
                    if '#AD' in event.message.message or '#paidAD' in event.message.message or 'sponsored' in event.message.message:
                        print(event)
                        await client.delete_messages(event.message.peer_id.user_id, event.message.id)
                        print('message deleted successfully')
                    else:
                        print('failed')
                        pass
            client.add_event_handler(my_event_handler)
            await client.run_until_disconnected()
        except Exception as e:
            print(e)
            await asyncio.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())
