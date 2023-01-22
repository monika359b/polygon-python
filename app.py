import asyncio
from telethon import TelegramClient, events

async def main():
    event = asyncio.Event()
    bot_token = '5846295132:AAELVqVfmejscqruRH3jKl88i3gmc2mFw0k'
    client = TelegramClient('Bot', "7243983", "e1bd137a37da9f95ecd2b206a8c8be48")
    await client.start(bot_token=bot_token)
    bot_chat_id = 5846295132

    @client.on(events.NewMessage(chats=bot_chat_id))
    async def my_event_handler(event):
        if event.message.from_id.user_id == 5846295132:
               if '#AD' in event.message.message or '#paidAD' in event.message.message or 'sponsored' in event.message.message:
                print(event)
                await client.delete_messages(event.message.peer_id.user_id, event.message.id)
                print('message deleted successfully')
               else:
                    print('failed')
                    pass
    client.add_event_handler(my_event_handler)
    while True:
        await event.wait()
        event.clear()

if __name__ == '__main__':
    asyncio.run(main())



