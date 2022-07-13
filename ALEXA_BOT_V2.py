#!/usr/bin/env python
# coding: utf-8

# In[7]:


from time import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


# In[8]:


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)


# In[9]:


def talk(text):
    engine.say(text)
    engine.runAndWait()


# In[10]:


def take_command():
    try: 
         with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


# In[11]:


def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
    


# In[12]:


while True:
    run_alexa()

run_alexa()


# In[ ]:





# In[ ]:





# In[ ]:




