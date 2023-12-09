import asyncio
from telethon import TelegramClient, events
from telethon.utils import get_peer_id
from conf import conf
from arab_channels_username import arab_channels_usernames
from translate import translate_text


async def main():
    async with TelegramClient(conf['key_auth'], conf['api_id'], conf['api_hash']) as client:
        arab_entity = [await client.get_entity(username) for username in arab_channels_usernames]
        channels_title = {channel.id: translate_text(channel.title) for channel in arab_entity}
        translate_channel = await client.get_entity(conf['translate_channel'])

        @client.on(events.NewMessage(from_users=arab_entity))
        async def handle_new_message(event):
            id_channel = get_peer_id(event.message.peer_id, add_mark=False)
            translated_message = f'{translate_text(event.message.text)}\n({channels_title[id_channel]})'
            event.message.text = translated_message
            await client.send_message(translate_channel, event.message)

        await client.run_until_disconnected()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
