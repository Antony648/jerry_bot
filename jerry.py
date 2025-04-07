#thank you jesus for helping me
import wikipedia
import pyjokes
import time
from ai import AI
from todo import Todo,Item,STATUS
from datetime import date,timedelta
import datetime
import sys
from websearch import search_song
import keyboard
import psutil
import os
from users2 import user2
import users2
os.environ['DISPLAY']=":0"

jerry=AI()
default_user=user2()
todo=user2.todo()

def authenticate_user():
    jerry.speak("are your an existing user:")
    
    while True:
        user_inp=jerry.listen()
        if user_inp in ["positive","yes","i am ","i do"]:
            jerry.speak("say your name")
            while True:
                user_inp=jerry.listen()
                #dict_item:dict
                for dict_item in users2.read_from_userdert():
                    if user_inp==dict_item.values('name').lower():
                        count=1
                        while True:
                            jerry.speak(f' hello {user_inp}, say your passkey')
                            user_inp=jerry.listen()
                            if user_inp == dict_item.values('passkey'):
                                #codefor convert dict to user2
                                jerry.speak(f"you have successfully authenticated as{dict_item.values('name')}")
                                return
                            else:
                                jerry.speak('wrong passkey')
                                if count==3:
                                    jerry.speak('authentication failed you have reached 3 trials')
                                    return
                                count+=1
                        
                jerry.speak('couldnt find the name do you want to say a different name or you do you want to quit')
                user_inp=jerry.listen()
                if user_inp in ['no',"quit",'exit',"negative"]:
                    jerry.speak("exiting from user authentication sequence")
                    return
                else:
                    jerry.speak("say name again")       
        elif user_inp in ["negative","no","i am not"]:
            jerry.speak("do you want to become one")
            while True:
                user_inp=jerry.listen()
                if user_inp in ["yes","positive","proceed"]:
                    name:str
                    age:int
                    place:str
                    passkey:str

                    jerry.speak("please say your name")
                    while True:
                        name=jerry.listen()
                        jerry.speak(f"name input recived is {name} do you want to proceed")
                        user_inp=jerry.listen()
                        if user_inp in ["yes","proceed","positive"]:
                            break
                        else:
                            jerry.speak("say name again")

                    jerry.speak("please say your age")
                    while True:
                        age=int(jerry.listen())
                        jerry.speak(f"name input recived is {age} do you want to proceed")
                        user_inp=jerry.listen()
                        if user_inp in ["yes","proceed","positive"]:
                            break
                        else:
                            jerry.speak("say age  again")


                    jerry.speak("please say your place")
                    while True:
                        place=jerry.listen()
                        jerry.speak(f"name input recived is {place} do you want to proceed")
                        user_inp=jerry.listen()
                        if user_inp in ["yes","proceed","positive"]:
                            break
                        else:
                            jerry.speak("say place name again")


                    jerry.speak("please mention the passkey")
                    while True:
                        passkey=jerry.listen()
                        jerry.speak(f"name input recived is {passkey} do you want to proceed")
                        user_inp=jerry.listen()
                        if user_inp in ["yes","proceed","positive"]:
                            break
                        else:
                            jerry.speak("say passkey again")


                    default_user=user2(name=name,age=age,place=place,passkey=passkey)
                    users2.write_to_usersdert(default_user)
                    return
                elif user_inp in ['no','nien','negative']:
                    jerry.speak("exiting from user creation sequence")
                    return
                else:
                    jerry.speak("unable to understand it,please repeat if you want to be a new user or not")
            break
            
        else:
            jerry.speak("command unclear please say if you are a user or not")



def changeto_pending():
    jerry.speak("say the item you want to update status to pending")
    while True:
        usr_inp=jerry.listen()
        if user_inp=="sorry did not understand that":
            pass
        elif user_inp in ["nein","no","negative"]:
            jerry.speak("cancelling operation of changing item status to pending")
            return
        else:
            for item in todo:
                if user_inp==item.title:
                    jerry.speak("found")
                    item.status=0
                    break
            jerry.speak("item not found in list")
            
def changeto_progress():
    jerry.speak("say the item you want to update status to progess now")
    while True:
        usr_inp=jerry.listen()
        if user_inp=="sorry did not understand that":
            pass
        elif user_inp in ["no","nein","negative"]:
            jerry.speak('cancelling the operation of changing item status to progress')
            return
        else:
            for item in todo:
                if user_inp==item.title:
                    jerry.speak("found")
                    item.status=1
                    break
            jerry.speak("item not found in list do you want to update stat for another item")


def changeto_finished():
    jerry.speak("say the item you want to update status to finished")
    while True:
        usr_inp=jerry.listen()
        if user_inp=="sorry did not understand that":
            pass
        elif user_inp in ['no','negative','nein']:
            jerry.speak('cancelling the operation of changing item statuds to finished')
            return
        else:
            for item in todo:
                if user_inp==item.title:
                    jerry.speak("found")
                    item.status=2
                    break
            jerry.speak("item not found in list do you want to update stat for another item")


def get_pending():
    item_list=[]
    #current_date=datetime.datetime.now().date()
    for item in todo:
        if item.status==0:
            item_list.append(item.title)
    if len(item_list)!=0:
        jerry.speak("items that are pending include")
        for item in item_list:
            jerry.speak(item.title)
    else:
        jerry.speak('no pending items')

def get_progress():
    item_list=[]
    for  item in todo:
        if item.status==1:
            item_list.append(item)
    if len(item_list)!=0:
        jerry.speak("items that are in progress include")
        for item in item_list:
            jerry.speak(item.title)
    else:
        jerry.speak("no items in progress")

def get_finished():
    item_list=[]
    for item in todo:
        if item.status==2:
            item_list.append(item)
    if len(item_list)!=0:
        jerry.speak("finished contents of todo list are:")
        for item in item_list:
            jerry.speak(item.title)
    else:
        jerry.speak('no finished items in list')

def play_song_vedio(input:str):
    input=input.replace("play","")
    jerry.speak("going to play"+input)
    jerry.speak("should i proceed")
    user_inp=jerry.listen()
    while(True):
        if user_inp in ["proceed","positive","affirmitive","yes"]:
            search_song(input)
            break
        elif user_inp in ["no","negative","dont play","go back"]:
            jerry.speak("why did i get the name wrong,should i change the name")
            user_inp=jerry.listen()
            if user_inp in["proceed","positive","yes","affirmative"]:
                jerry.speak("say the new name:")
                input=jerry.listen()
            elif user_inp in ["no","nein","negative","dont"]:
                jerry.speak("okay not going to play"+user_inp)
                break
            elif user_inp in["dont change","donot change"]:
                search_song(input)
                break
            else:
                jerry.speak("i did not understand your command")
        elif user_inp in ['shutdown','exit']:
            sys.exit()



def get_date()->str:
    current_date=datetime.datetime.now()
    day=current_date.day
    month=current_date.strftime("%B")
    year=current_date.year

    if 10<= day <=20:
        suffix='th'
    else :
        suffix={1:"st",2:"nd",3:"rd"}.get(day%10,"th")
    formatted_date=f"{day}{suffix} {month} {year}"
    return formatted_date

def understand_date(item:Item,inp:str)->bool:
    if inp in ['cancel','stop','dont do']:
        return False
    if inp in ['today','this day','thisday','now']:
        item.due_date=datetime.datetime.now().date()
        jerry.speak("date set to today successfully")
        return True
    if inp in ['tommorrow','next day']:
        item.due_date=datetime.datetime.now().date()+timedelta(days=1)
        jerry.speak("date set to tommorow successfully")
        return True
    if inp in ['day after tommorow']:
        item.due_date=datetime.datetime.now().date()+timedelta(days=2)
        jerry.speak("date set to day after tommorow")
        return True
    dayi=0
    monthi=0
    l=[["31st","31"],["30th","30"],["29th","29"],["28th","28"],["27th","27"],["26th","26"],
       ["25th","25"],["24th","24"],["23th","23"],["22nd","22"],["21st","21"],
       ["20th","20"],["19th","19"],["18th","18"],["17th","17"],["16th","16"],["15th","15"],
       ["14th","14"],["13th","13"],["12th","12"],["11th","11"],["10th","10"],["9th","9"],
       ["8th","8"],["7th","7"],["6th","6"],["5th","5"],['4th','4'],['3rd','3'],['2nd','2'],
       ['1st','1']]
    
    for i  in range(len(l)):
        for k in l[i]:
            if k in inp:
                dayi=31-i
                print("day set to",dayi)
                break
        if dayi!=0:
            break

    z=["january","february","march","april","may","june","july","august","september","october",
       "november","december"]
    for i in range(len(z)):
        #print("checking ",z[i]," compared to ",inp)
        if z[i] in inp:
            monthi=i+1
            print("month successfully set to",monthi)
            break
    try:
        if dayi!=0 and monthi!=0:
            
            date_itre=date(2025,month=monthi,day=dayi)
            if (date_itre<datetime.datetime.now().date()):
                jerry.speak("that date is in the past ")
                jerry.speak("do you want to proceed")
                user_inp=jerry.listen()
                if user_inp in ["yes","positive","affirmative"]:
                    item.due_date=date_itre
                    return True
                else:
                    return False
            else :
                item.due_date=date_itre
                return True
        else:
            print("couldnt get month or date")
            return False
    except Exception as e:
        print("failed")

def updatedate():
    jerry.speak("please say the list item that you want to update")
    while True:
        user_inp=jerry.listen()
        if user_inp=="sorry did not understand that":
            jerry.speak('say item name again')
            pass
        elif user_inp in ["cancel","back"]:
            jerry.speak("canecelling date updation operation")
            return
        else:
            for item in todo:
                if user_inp==item.title:
                    jerry.speak("item found in list")
                    
                    
                    while True:
                        jerry.speak("please say the new date")
                        user_inp=jerry.listen()
                        if(understand_date(item,user_inp)):
                            jerry.speak("item date updated successfully")
                            return
                        else:
                            jerry.speak("do you want to say the date again")
                            if user_inp in["procced",'positive','goahead','yes']:
                                continue
                            else:
                                jerry.speak("cancelling date updation operation")
                                return
            jerry.speak("item you specified not in list,do want me find another item from list now")
            user_inp=jerry.listen()
            if user_inp in ["pass","positive","proceed"]:
                pass
            else:
                return
            

                    
def make_joke():
    joke=pyjokes.get_joke()
    jerry.speak(joke)
    print(joke)

def get_battery()->str:
    battery=psutil.sensors_battery()
    if battery:
        return f"battery is at {int(battery.percent)} percent"
    else:
        return "couldnt fetch battery status at currnet time"

def add_todo()->bool:
    item=Item()
    jerry.speak("what should i add to list")
    try:
        while(True):
            item.title=jerry.listen()
            if item.title=="sorry did not understand":
                jerry.speak("item name unclear please say again")
                continue
            jerry.speak(item.title+"is to be added to list")
            jerry.speak("do you want to add a date for the item specifid ")
            break

        k="please say the date"
        while True:
            reply=jerry.listen()
            if reply in["yes","yeah","okay","positive"]:
                jerry.speak(k)
                inp=jerry.listen()
                if inp in ["cancel","dont","stop","remove"]:
                    reply="no"
                else:
                    while(True):
                        if inp in ["exit","shutdown"]:
                            sys.exit()
                        if understand_date(item,inp):
                            print("date set successfully")
                            jerry.speak("date set to"+inp)
                            break
                    
                        
                        elif inp in ["no","negative","nein"]:
                            jerry.speak("okay then")
                            break
                        else:
                            jerry.speak("could you repeat the date,I couldnt get it")
                            inp=jerry.listen()
                    break
                    
            if reply in ["no","nien","nopes","cancel","negative"]:
                jerry.speak("okay then")
                break
            elif reply in ["stop","remove","cancel item"]:
                return False
            if reply in ["exit","shutdown"]:
                #sys.exit()
                quit()
            else:
                jerry.speak("command unclear")
        

        todo.new_item(item)
        jerry.speak("Item"+item.title+"added")
        return True
    except:
        print("Oops that was an error.")
        return False
def just_today():
    jerry.speak('displaying todays contents')  
    for item in todo:
        today_list=[]
        if item.due_date==datetime.datetime.now().date():
            today_list.append(item)
        if len(today_list)!=0:
            jerry.speak("todays list contents")
            for item in today_list:
                jerry.speak(item.title)

def just_tomorrow():
    jerry.speak('displaying todays contents')  
    for item in todo:
        today_list=[]
        if item.due_date==datetime.datetime.now().date()+timedelta(days=1):
            today_list.append(item)
        if len(today_list)!=0:
            jerry.speak("tomorrows list contents")
            for item in today_list:
                jerry.speak(item.title)

def todayandfuture():
    jerry.speak('displaying todays contents')  
    for item in todo:
        today_list=[]
        if item.due_date>=datetime.datetime.now().date():
            today_list.append(item)
        if len(today_list)!=0:
            jerry.speak("list contents from today onwards")
            for item in today_list:
                jerry.speak(item.title)



def list_todo():
    if len(todo)<0:
        print("todo list is empty")
    else:
        jerry.speak("do you want to display all the items in list")
        while True:
            user_inp=jerry.listen()
            if user_inp in["yes","positive","affirmative","process"]:
                jerry.speak("contents of todo lists are")
                #item:Item
                for item in todo:
                    print("from main"+item.title)
                    jerry.speak(str(item.title))
                break
            elif user_inp in ["no","nein","negative"]:
                jerry.speak("do you just want to see the contents for today")
                while True:
                    lis=jerry.listen()
                    if lis in ["yes","positive","affirmative","proceed"]:
                        for item in todo:
                            if item.due_date==datetime.datetime.now().date():
                                print("from main",item.title)
                                jerry.speak(item.title)
                        break
                    elif lis in ["no","nein","negative"]:
                        jerry.speak("do you want to see contents of tomorrow")
                        while True:
                            lis=jerry.listen()
                            if lis in ["affirmative","positive","yes"]:
                                tmrw=datetime.datetime.now().date()+timedelta(days=1)
                                for item in todo:
                                    if item.due_date==tmrw:
                                        print("main func",item.title)
                                        jerry.speak(item.title)
                                break
                            elif lis in ["no ","negative"]:
                                jerry.speak("i cannot access elements explicitly other than these two sets")
                                break
                            elif lis in ['exit','cuttoff','cancel']:
                                jerry.speak("not displaying list content command  cancelled")
                                return
                            else:
                                jerry.speak("i couldnt interpret command  whether to dislay tomorrows or not please say again now")
                        break
                    elif lis in ['exit','cuttoff','cancel']:
                        jerry.speak("not displaying list content command  cancelled")
                        return
                    else:
                        jerry.speak("couldnt interpret your command whether to display todays only or not please say again now")

                break
            elif user_inp in ['exit','cuttoff','cancel']:
                    jerry.speak("not displaying list content command  cancelled")
                    return
            else:
                jerry.speak("couldnt interpret your command  whether to display all or not please say again now")            
            

def remove_todo()->bool:
    jerry.speak("which one to remove")
    try:
        inp=jerry.listen()
        if todo.remove_item(title=inp):
            jerry.speak(inp+"removed from todo list")
        else:
            jerry.speak(inp+"not found!")
            return True
    except:
        jerry.speak("Oops somethig went wrong")
        return False
    
awake=False
jerry.speak("hi i am jerry how can i help you today?")
while True:
    
    user_inp=jerry.just_listen()
    command_given=False
    
    if user_inp in ["shutdown","exit","poweroff"]:
        jerry.speak("shutting myself off")
        sys.exit()
    elif any(item in user_inp for item  in ["hey jerry" ,"hey yo","hello",'hey','wakeup']):
        k=user_inp
        for i in ["hey jerry" ,"hey yo","hello",'hey','wakeup']:
            k=k.replace(i,'')
      # k=k.lstrip().rstrip()
        if k!='' :
            command_given=True
            print("actual command:"+k)
            jerry.speak(k)
            user_inp=k
        awake=True
#user_inp=""
    
    if   awake:
        if not command_given:
            jerry.speak('i am waiting for your command')
            user_inp=jerry.listen()
        if user_inp=="sorry did not understand":
            continue
        if user_inp in ["hello","hello jerry","hi jerry"]:
            jerry.speak("hi how can i help")
        elif user_inp in ["jerry sleep","sleep","goto sleep"]:
            jerry.speak("i am going to sleep for now")
            awake=False
        elif user_inp in ["shutdown","exit","power off"]:
            jerry.speak("shutting myself off for now")
            sys.exit()
        elif 'create' in user_inp and 'you' in user_inp:
            jerry.speak("someone who has a lot of free time")

        elif "time" in user_inp:
            if any(item in user_inp for item in ["time now","tell time","tell me the time","what is the time"]):
                jerry.speak("time is "+datetime.datetime.now().strftime("%H %M"))

        elif "date" in user_inp:
            if any(item in user_inp for item in["date now","today's date","tell me date"]):
                jerry.speak(get_date())

        elif "joke" in user_inp:
            if any(item in user_inp for item  in ["tell me a joke","make a joke","make me laugh","crack a joke","crack me a joke","joke"]):
                make_joke()
        elif "battery" in user_inp:
            if any(item in user_inp for item in ["get battery","battery percent","battery life"]):
                jerry.speak(get_battery())
        elif "who is " in user_inp:
                user_inp=user_inp.replace("who is ","").strip()
                try:
                    info=wikipedia.summary(user_inp,sentences=1)
                    jerry.speak(info)
                except wikipedia.DisambiguationError :
                    u="there are multiple individuals with that name please be specific"
                    print(u)
                    jerry.speak(u)
                except wikipedia.PageError:
                    u="could not find information about the person"
                    print(u)
                    jerry.speak(u)
        elif "what is " in user_inp:
                user_inp=user_inp.replace("what is ","").strip()
                try:
                    info=wikipedia.summary(user_inp,sentences=1)
                    jerry.speak(info)
                except wikipedia.DisambiguationError :
                    u="there are multiple references with that name please be specific"
                    print(u)
                    jerry.speak(u)
                except wikipedia.PageError:
                    u="could not find answer to that question"
                    print(u)
                    jerry.speak(u)
        
        elif "play"  in user_inp:
                play_song_vedio(user_inp)
        elif any(item in user_inp for item in ['set','add','fix','new']):
            if any(item in user_inp for item in ['new item',"add to todos","add an item to todos","add to todo list","add item","add event","add appoinment","fix appointment"]):
                add_todo()
        elif "list" in user_inp:
            if any(item in user_inp for item in ["list todos","list contents in todo","list item","list event"]):
                list_todo()
        elif any(item in user_inp for item in ["done","remove"]):
            if any(item in user_inp for item  in ["remove todos","mark done","remove item","remove to-dos"]):
                remove_todo()
        elif any(item in user_inp for item in ["change","update","date"]):
            if any(item in user_inp for item in ["update item date","change item date"]):
                updatedate()

        elif "finished" in user_inp:
            if any(item in user_inp for item in ["show finished items","finished items","done items"]):
                get_finished()
        elif "progress" in user_inp:
            if any(item in user_inp for item  in ["show items in progress","item in pogress","progressing items","progerss item "]):
                get_progress()
        elif "pending" in user_inp:
            if any(item in user_inp for item  in ["show items in pending","item in pending","pending item","pending items","item pending"]):
                get_pending()
        elif "today" in user_inp:
            if any(item in user_inp  for item in ["todays item","today item","only today"]):
                just_today()
        elif "tomorrow" in user_inp:
            if user_inp in ["only tomorrow","get tomorrow","tomorrow item","tomorow"]:
                just_tomorrow()
        elif user_inp in ["future events"]:
            todayandfuture()
        elif user_inp in["raise volume","cant hear","increase volume"]:
            try:
                keyboard.press_and_release("volume up")
                jerry.speak("raised volume")
            except ImportError:
                jerry.speak("you must have superuser privilleges for doing that")
        elif user_inp in ["lower volume","too loud","decrease volume"]:
            try:
                keyboard.press_and_release("volume down")
                jerry.speak("lowered volume")
            except ImportError:
                jerry.speak("you must have superuser privilleges for doing that")
        elif any(item in user_inp for item in ['am i']):
            jerry.speak("i cannot  assess humans")
        
        elif 'name' in user_inp and 'you' in user_inp:
            jerry.speak("i am jerry")
        else:
            jerry.speak("functionialihowty is currently out of my domain")
        awake=False
    #jerry.speak("bye I am going")
    
