import os
from google import genai
from ollama import chat
import mlx_whisper
import sounddevice as sd
import time
import numpy as np
import wave
from google import genai
from dotenv import load_dotenv

import base64
load_dotenv()


stream = sd.InputStream(samplerate = 16000, blocksize=2048, channels=1)
def calc_rms(audio):
        return np.sqrt(np.mean(audio ** 2))

fs = 16000
duration = 10.5  # seconds
global text
global running
audio_matrix = []

def pass_voice_input(text):
        ai_text = ""
        stream = chat(
        model='qwen3:8b',
        messages=[{'role': 'user', 'content': text}],
        stream=True,
        think=False
    )

        for chunk in stream:
                content = chunk['message']['content']
                print(content, end='', flush=True)
                ai_text += content
        return ai_text

def stop_running(text):
        if text == "stop":
                running = False
        if text == "restart":
               running = True
def jarvis_ai():
        input_matrix = []
        stream.start()
        silence_duration = 0
        running = True
        ai_enabled = True
        while running:
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
                                def start_stop(text):
                                       nonlocal ai_enabled
                                       if text.strip().lower().rstrip(".!") == "stop":
                                              ai_enabled = False
                                       if text.strip().lower().rstrip(".!?") == "listen":
                                              ai_enabled = True
                                       if ai_enabled == True and text.strip() != "":
                                              ai_text = pass_voice_input(text)

                                              try:
                                                        text_to_speech(ai_text)
                                              except Exception as e:
                                                        print(type(e).__name__, e)
                                start_stop(text)
                                input_matrix = []

                                
def text_to_speech(ai_text):
        client = genai.Client()
        byte_array = []
        stream = client.interactions.create(
        model="gemini-3.1-flash-tts-preview",
        input=ai_text,
        response_format={"type": "audio"},
        generation_config={
                "speech_config": [
                {"voice": "Zubenelgenubi"}
                ]
        },
        stream=True
        )
        print("GEMINI STREAM CREATED")
        speaker = sd.RawOutputStream(samplerate=24000, channels=1, dtype="int16")
        speaker.start()
        for event in stream:
                if event.event_type == "step.delta":
                        if event.delta.type == "audio":
                                audio_data = base64.b64decode(event.delta.data)

                                print("audio chunk received")
                                speaker.write(audio_data)
                                
        speaker.stop()
        speaker.close()
                                

jarvis_ai()
