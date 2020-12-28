# pip install SpeechRecognition
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
# from VideotoTextSummarization.app.utils.config import Config
import speech_recognition as sr


def audio_to_text(path):
    try:
        r = sr.Recognizer()
        print("Speech recognizer activated:::::::::::::")

        audio = AudioSegment.from_wav(path)
        print(audio)

        try:
            if not os.path.exists('audio_text'):
                os.makedirs('audio_text')
        except OSError as e:
            print('Error: Creating directory of audio text' + str(e))

            recognized = open("audio_text.txt", "w+")
            chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=-16)

            try:
                os.mkdir('audio_chunks')
            except FileExistsError as e:
                print('Error: Creating directory of audio chunks' + str(e))
                pass

            os.chdir('audio_chunks')

            i = 0
            for chunk in chunks:
                chunk_silent = AudioSegment.silent(duration=10)
                audio_chunk = chunk_silent + chunk + chunk_silent
                print("saving chunk{0}.wav".format(i))

                audio_chunk.export("./chunk{0}.wav".format(i), bitrate='192k', format="wav")
                filename = 'chunk' + str(i) + '.wav'
                print("Processing chunk " + str(i))

                file = filename
                with sr.AudioFile(file) as source:
                    r.adjust_for_ambient_noise(source)
                    audio_listened = r.listen(source)
                try:
                    rec = r.recognize_google(audio_listened)
                    recognized.write(rec + ". ")
                except sr.UnknownValueError as u:
                    print("Error: Could not understand audio" + str(u))
                except sr.RequestError as e:
                    print("Error: Could not request results. check your internet connection" + str(e))
                i += 1
            os.chdir('..')
    except Exception as e:
        print("Error: Converting audio to text" + str(e))

# def audio_to_text(path):
#     # transcribe audio file
#     AUDIO_FILE = path
#
#     # use the audio file as the audio source
#     r = sr.Recognizer()
#     with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source)  # read the entire audio file
#
#         print("Transcription: " + r.recognize_google(audio))


if __name__ == '__main__':
    # audio_to_text(path=Config.Directories.WAV_AUDIO_PATH)
    audio_to_text(path="audio.wav")
