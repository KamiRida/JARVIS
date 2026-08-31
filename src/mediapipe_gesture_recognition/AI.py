
from ollama import chat
import mlx_whisper
import sounddevice as sd
import time
import numpy as np


stream = sd.InputStream(samplerate = 16000, blocksize=2048, channels=1)
def calc_rms(audio):
        return np.sqrt(np.mean(audio ** 2))

fs = 16000
duration = 10.5  # seconds
global text
audio_matrix = []
def pass_voice_input(text):
  
    stream = chat(
        model='qwen3:8b',
        messages=[{'role': 'user', 'content': text}],
        stream=True,
        think=False
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)


def speech_to_text():
        input_matrix = []
        stream.start()
        silence_duration = 0
        while True:
                myrecordingA = (stream.read(2048)[0])
                myrecordingA = myrecordingA[:, 0]
                rms = calc_rms(myrecordingA)
                if rms > 0.01:
                        input_matrix.append(myrecordingA)
                        silence_duration = 0
                        while True:
                                myrecording = (stream.read(2048)[0])
                                myrecording = myrecording[:, 0]
                                rms = calc_rms(myrecording)
                                input_matrix.append(myrecording)
                                if rms < 0.01:
                                        silence_duration += 2048/ 16000
                                else:
                                        silence_duration = 0
                                if silence_duration >= 0.7:
                                        break
                        if input_matrix != []:
                                full_audio = np.concatenate(input_matrix)
                                text = mlx_whisper.transcribe(full_audio, language="en")["text"]
                                input_matrix = []
                                if text.strip() != "":
                                        pass_voice_input(text)
speech_to_text()
                        


#sound device 
#[0.4, 0.3, 0.5, 0.02, 0.03, 0.04]
