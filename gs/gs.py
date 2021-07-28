from telethon import TelegramClient
import os

api_id = '7971874'
api_hash = '81d83418ba9b855bcb065ff9620e21f7'

arr = os.listdir()
i = 0

while i < len(arr):
	with TelegramClient('anon2', api_id, api_hash) as client:
		client.loop.run_until_complete(client.send_file('alina_thorns', str(arr[i]), voice_note=True))
	i += 1
	print('otpravil')
	time.sleep(10)
	break
