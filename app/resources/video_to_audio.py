import moviepy.editor as me
import os
from VideotoTextSummarization.app.utils.config import Config


def video_to_audio(path):
    try:
        video = me.VideoFileClip(path)
        audio = video.audio
        try:
            if not os.path.exists('audio'):
                os.makedirs('audio')
        except OSError as e:
            print('Error: Creating directory of audio' + str(e))
        audio.write_audiofile(Config.Directories.SAVE_AUDIO_DIRECTORY)
        # os.rename(Config.Directories.AUDIO_PATH, Config.Directories.WAV_AUDIO_PATH) # mp3 to wav
    except Exception as e:
        print('Error: Converting video to audio' + str(e))


if __name__ == "__main__":
    video_to_audio(path=Config.Directories.VID_PATH)
