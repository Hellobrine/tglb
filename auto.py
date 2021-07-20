from telethon import TelegramClient
import time


api_id = '7971874'
api_hash = '81d83418ba9b855bcb065ff9620e21f7'

def send():
	with TelegramClient('anon', api_id, api_hash) as client:
		client.loop.run_until_complete(client.send_message('https://t.me/joinchat/4Xef62yqUDFmOTAy', 'Бой'))

while True:
	send()
	time.sleep(60)
