import os
from pydub import AudioSegment

# files
src = os.path.dirname(os.path.abspath(__file__)) + "\\audio.mp3"
dst = os.path.dirname(os.path.abspath(__file__)) + "a.wav"

print(os.getcwd())
# convert mp3 to wav
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


# import subprocess
# subprocess.call(['ffmpeg', '-i', 'audio.mp3',
#                    'audio.wav'])