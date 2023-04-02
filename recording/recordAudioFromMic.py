import pyaudio
import wave

SOUND_PATH = "FILEPATH"

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, output=True, frames_per_buffer=2048)
stream.start_stream()

frames = []

def recordAudioFromMic():
    try:
        while True:
            data = stream.read(2048)
            frames.append(data)

    except KeyboardInterrupt:
        stream.stop_stream()
        stream.close()
        mic.terminate()

        wf = wave.open(SOUND_PATH, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(mic.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()
