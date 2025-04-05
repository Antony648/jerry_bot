import pyttsx3
import time
engine=pyttsx3.init()
voices=engine.getProperty('voices')
for i,voice in enumerate(voices):
    print(f"voice{i}:{voice.name}")

engine.setProperty('voice',voices[25].id)
engine.setProperty("rate",150)
time.sleep(0.2)
engine.say("this is a very long sentence that has to be said correclty"
"otherwise nazis will come back to power and destroy everyone and everything ")
engine.runAndWait()
time.sleep(0.9)