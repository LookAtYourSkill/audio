from gtts import gTTS
import os

PATH = "FILEPATH"

tts = input('What do you want to be said in Text to Speech? ?\n')
text = str(tts)

language: str = input('What language you want? \nde = german/en = english\n')
if language == 'en':
    language = 'en'
else:
    language = 'de'

name: str = input('What name should the file have?\n')

speech = gTTS(text=text, lang=language, slow=False)
speech.save(PATH + 'T2S' + name + '.mp3')
os.system(f'start {PATH}T2S{name}.mp3')