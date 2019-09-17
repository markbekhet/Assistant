import speech_recognition as sr
import winsound as ws
import pyaudio as pa
import wave
import win32com.client as wincl


 
import math 

recognizer= sr.Recognizer()
harvard = "harvard.wav"
recorder = pa.PyAudio()

filename = "greeting.wav"

with sr.Microphone() as source:
    print("say something")
    audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        file = wave.open(filename, "wb")
        file.writeframesraw(audio)
        ws.PlaySound(filename,True)

                
    except:
        text_adjusted= recognizer.adjust_for_ambient_noise(audio)
        print(text_adjusted)
        print("sorry I didn't recognize your voice")




    
