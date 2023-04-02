from gtts import gTTS
import os

PATH = "FILEPATH"

file = input('Which file would you like to have read to you? ? (Full Path where the file is)')
file_open = open(file, "r").read().replace("\n", " ")

language: str = input('What language you want? \nde = german/en = english\n')
if language == 'en':
    language = 'en'
else:
    language = 'de'

speech = gTTS(text=file_open, lang=language, slow=False)

name: str = input('What name should the file have?')
speech.save(PATH + 'F2S' + name + '.mp3')
os.system(f'start {PATH}F2S{str(name)}.mp3')