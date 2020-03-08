import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import pyttsx3
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize    
#import pandas
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.8
        r.energy_threshold=300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        query= ""
    return query
if __name__ == "__main__":
    f=open('a.txt','a+')
    while True:
        query = takeCommand().lower()
        if 'quit' in query:
            break
        if query=='':
            continue
         #results = wikipedia.summary(query, sentences=2)
        #print(results)
        f.write(query +'\n')
        #f.write(results+'\n')
    f.seek(0)
    for line in f:
        speak(line)
    f.close()
    k=[]
    f=open('a.txt','r')
    contents=f.read()
    l=contents.split()
    stop_words = set(stopwords.words("english"))
    ##Creating a list of custom stopwords
    new_words = ["using", "show", "result", "large", "also", "iv", "one", "two", "new", "previously", "shown",'boys','girl','girls']
    stop_words = stop_words.union(new_words)
    for i in l:
        if i not in stop_words:
            k.append(i)
    k=list(set(k))
    #print(k)
    f.close()
    p=open('p.txt','r')
    t=p.read()
    notes=open('notes.txt','a')

    for i in k: #speech to text preprocessed

        ps = PorterStemmer() 
  
# choose some words to be stemmed   
        y=ps.stem(i)

        if i in t or y in t :
           results= wikipedia.summary(i,sentences=2)
           notes.write(i+':-\n')
           notes.write(results+'\n')
    notes.close()
    p.close()
