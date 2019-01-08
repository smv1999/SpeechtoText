import speech_recognition as sr 
import tkinter
from textblob import TextBlob
import re
AUDIO_FILE = open("neyg9-85vcs.wav",'rb') 
  
r = sr.Recognizer() 
  
with sr.AudioFile(AUDIO_FILE) as source: 
    
    audio = r.record(source)   


 
try: 
    print("The audio file contains: " + r.recognize_google(audio))
    #string=r.recognize_google(audio)
    #string="Hello"
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

string=r.recognize_google(audio)

'''if("stupid" or "much" in string):
    r=tkinter.Tk()
    r.title("Happy!")
    #print("Wooow!")'''

analysis = TextBlob(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", string).split())) 
if analysis.sentiment.polarity > 0: 
    sent= 'positive'
elif analysis.sentiment.polarity == 0: 
    sent= 'neutral'
else: 
    sent= 'negative'
    
print(sent)  
