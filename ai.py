import pyttsx3
import time
import speech_recognition as sr
class AI():
    __name=""
    __skill=[]

    def __init__(self,name=None):
        self.engine=pyttsx3.init()      #output text-to-speech
        self.engine.setProperty('rate',150)
        self.engine.setProperty('volume',0.9)
        voice=self.engine.getProperty('voices')
        self.engine.setProperty("voice",voice[25].id)
        self.r=sr.Recognizer()          #used for filtering input
        self.m=sr.Microphone()             #input
        if name is not None:
            self.__name=name

        print("LISTENING")
        with self.m as source:                          #use microphone object to get input voice
            self.r.adjust_for_ambient_noise(source)     #use recogniser to filter out bg noise
        
    @property                   #for creating getter and setter for our secret variable
    def name(self):             #returns name if called upon
        return self.__name
    @name.setter
    def name(self,name_val):        #overrides name if the name parameter is passed explicitly
        self.__name=name_val
        self.engine.say("Hello, I am",self.__name,"How can I assist you today")
        self.engine.runAndWait()

    def speak(self,output:str):
        time.sleep(0.2)
        self.engine.setProperty("rate",150)
        self.engine.say(output)
        self.engine.runAndWait()
        time.sleep(0.5)

    def just_listen(self)->str:
        print("listenin")
        with self.m as source:
            audio=self.r.listen(source,phrase_time_limit=6)
        print("audio input recived")


        try:
            inp_understood:str
            inp_understood=self.r.recognize_google(audio)
            #self.engine.say("got you said "+inp_understood)   # comment this later  only for testing phase
            #self.engine.runAndWait()
            print("you said:"+inp_understood.lower())
            return inp_understood.lower()
        
        except sr.UnknownValueError:
            #out="sorry did not understand that"
            #self.engine.say(out)
            #self.engine.runAndWait()
            #print(e)
            print("unidentified")
            return "unidentified"
        except sr.RequestError:
            print("Request error")
            return "request error"
        except Exception as e:
            print(e)
            return "some exception"
    

    def listen(self)->str:
        print("listenin")
        
        with self.m as source:
            self.r.adjust_for_ambient_noise(source,duration=1)
            audio=self.r.listen(source,timeout=10)
        print("audio input recived")


        try:
            inp_understood:str
            inp_understood=self.r.recognize_google(audio,language="en-IN")
            self.engine.say("got you said "+inp_understood)   # comment this later  only for testing phase
            self.engine.runAndWait()
            print("you said:"+inp_understood.lower())
            return inp_understood.lower()
        
        except sr.UnknownValueError:
            out="sorry did not understand that"
            self.engine.say(out)
            self.engine.runAndWait()
            #print(e)
        except sr.RequestError:
            print("Request error")
        except Exception as e:
            print(e)
        return "sorry did not understand"
        


