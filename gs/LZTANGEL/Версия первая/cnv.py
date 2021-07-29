import subprocess
import os

arr = [x for x in os.listdir() if x.endswith(".mp3")]
i = 0

while i < len(arr):
	filename = arr[i]
	audio_path_ogg = filename + '.ogg'
	subprocess.run(["ffmpeg", '-i', arr[i], '-acodec', 'libopus', audio_path_ogg, '-y'])
	i += 1
print(‘done’)
