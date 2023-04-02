import soundcard as sc
import soundfile as sf

# file name.
SOUND_PATH = "FILPATH"
# [Hz] sampling rate.
# ! SAMPLE_RATE = 48000
SAMPLE_RATE = 44100
# [sec] duration recording audio.
RECORD_SEC = 5

def recordPCAudio():
    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
        
        # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
        sf.write(file=SOUND_PATH, data=data[:, 0], samplerate=SAMPLE_RATE)
