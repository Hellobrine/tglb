from telethon import TelegramClient
import os
import time

api_id = '7971874'
api_hash = '81d83418ba9b855bcb065ff9620e21f7'

arr = [x for x in os.listdir() if x.endswith(".ogg")]
i = 0

while i < len(arr):
	text = str(arr[i]).rpartition('.')
	
	with TelegramClient('anon2', api_id, api_hash) as client:
		client.loop.run_until_complete(client.send_message('me', text[0])
		client.loop.run_until_complete(client.send_file('me', str(arr[i]), voice_note=True))
	i += 1
	print('otpravil')
	time.sleep(3)
