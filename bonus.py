from telethon import TelegramClient
import time


api_id = '7971874'
api_hash = '81d83418ba9b855bcb065ff9620e21f7'

def bonus():
	with TelegramClient('anon', api_id, api_hash) as client:
		client.loop.run_until_complete(client.send_message('https://t.me/joinchat/4Xef62yqUDFmOTAy', 'Бонус'))
	time.sleep(30)
	with TelegramClient('anon', api_id, api_hash) as client:
		client.loop.run_until_complete(client.send_message('https://t.me/joinchat/4Xef62yqUDFmOTAy', 'Бонус'))
def vipbonus():
	with TelegramClient('anon', api_id, api_hash) as client:
		client.loop.run_until_complete(client.send_message('https://t.me/joinchat/4Xef62yqUDFmOTAy', 'Вип бонус'))
	time.sleep(30)
	with TelegramClient('anon', api_id, api_hash) as client:
		client.loop.run_until_complete(client.send_message('https://t.me/joinchat/4Xef62yqUDFmOTAy', 'Вип бонус'))
while True:
	bonus()
	time.sleep(60)
	vipbonus()
	time.sleep(28801)
