import speech_recognition as sr
import win32com.client as wincl
from defs import *

#Here I will initialize the speech recognition and the speak

recognizer= sr.Recognizer()
speak = wincl.Dispatch("SAPI.SpVoice")




def input_audio(question):
  recognizer= sr.Recognizer()
  speak = wincl.Dispatch("SAPI.SpVoice")
  speak.Speak(question)
  print(question)
  text = "None"
  while(text == "None"):
    with sr.Microphone() as source:
      
      #recognizer.adjust_for_ambient_noise(source)
      audio = recognizer.listen(source)
      
      
      try:
        text = recognizer.recognize_google(audio)
                  
      except:
        print(voice_error + question)
        speak.Speak(voice_error + question)
        text  = "None"

  print(text)
  return text
  
# I have to test the capacity of the langyage to convert a number
# This one will be tested tomorrow because i need Internet 
number = "How many links do you want to save ?"
number_ = input_audio(number)

