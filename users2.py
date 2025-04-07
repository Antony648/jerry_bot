from datetime import date
import json
import os
from todo import Todo 
class user2():
    def __init__(self,name,age,place,passkey):
        self.name=name
        self.age=age
        self.__passkey=passkey
        self.place=place
        self.__gender=''
        self.__friends=[]
        self.__spousename=''

        self.__mytodo=Todo()
        self.__status=''
        #self.__bdate=date
        
    @property
    def passkey(self):
        return self.__passkey
    @passkey.setter
    def passkey(self,passk:str):
        self.__passkey=passk

    @property
    def todo(self):
        return self.__mytodo
    @todo.setter
    def todo(self,item:Todo):
        self.__mytodo=item

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,gen:str):
        self.__gender=gen

    @property
    def spousename(self):
        return self.__spousename
    @spousename.setter
    def spousename(self,nam:str):
        self.__spousename=nam

    @property
    def friends(self):
        return self.__friends
    @friends.setter
    def friends(self,item):
        self.__friends.append(item)

    '''@property
    def bdate(self):
        return self.__bdate
    @bdate.setter
    def bdate(self,ps:date):
        self.__bdate=ps'''

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,st:str):
        if st in ['commited','single']:
            self.__status=st

    def to_dict(self):
        return {
            'name':self.name,
            'passkey':self.passkey,
            'age':self.age,
            'place':self.place,
            'friends':self.__friends,
            'todo':self.__mytodo.todo_to_listdict(),
            'status':self.__status,
            'spousename':self.__spousename,
            'gender':self.__gender
            #'date':self.__bdate
        }
    
    def set_todo(self,item:Todo):
        self.todo=item
    

#sample data
usra=user2(name="Antony",age=20,place='india',passkey='wiplash')
usrt=user2(name='Trishaa Raj',age=21,place='india',passkey='trisha')
#usr_lst=[usra,usrt]

path='/home/antony/Desktop/ai_project/ai_proj/jerry_bot/usersdert.json'
usr_lst=[]
def write_first(item:user2):
    usr_dict=item.to_dict()
    usr_lst.append(usr_dict)
    print(usr_lst)
    if os.path.exists(path):
        with open(path,'w') as file:
            json.dump(usr_lst,file,indent=4)

def write_to_usersdert(item:user2):
    usr_lst=read_from_userdert()
    #print(usr_lst)
    
    usr_lst.append(item.to_dict())
    print(usr_lst)
    #usr_dict=[i.to_dict() for i in usr_lst]
    
    if os.path.exists(path):
        with open(path,'w') as file:
            json.dump(usr_lst,file,indent=4)

def read_from_userdert()->list:
    if os.path.exists(path):
        with open(path,'r') as file:
            data=json.load(file)
            print(data)
            return data
        
def convert_dict_item_to_user2(item:dict)->user2:
    us=user2(name=item.values('name'),age=item.values('age'),place=item.values('place'),passkey=item.values('passkey')):
    #us.friends=item.values('friends')
    #us.todo =item.values('todo')
    us.gender=item.values('gender')
    us.status=item.values('status')
    us.spousename=item.values('spousename')
    

#user3=user2(name="joshua",age=10,place="coorg",passkey='joshua')
#write_to_usersdert(user3)
read_from_userdert()
#write_first(usrt)