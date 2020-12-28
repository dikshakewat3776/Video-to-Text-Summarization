import os


class Config:
    class Directories:
        app_dir = "D:\\VideotoTextSummarization\\VideotoTextSummarization\\app\\"

        vid_change_path = app_dir + "videos"
        os.chdir(vid_change_path)

        VID_PATH = os.path.join(vid_change_path, "SouthAfricavsNewZealand20071stODIDurbanFullHighlights.mp4")

        audio_change_path = app_dir + "audio"
        os.chdir(audio_change_path)

        AUDIO_PATH = os.path.join(audio_change_path, "audio.mp3")

        WAV_AUDIO_PATH = os.path.join(audio_change_path, "audio.wav")

        SAVE_FRAMES_DIRECTORY = './frames/frame'

        SAVE_AUDIO_DIRECTORY = './audio/audio.mp3'

        SAVE_AUDIO_TEXT_DIRECTORY = './audio_text/audio_text.txt'


