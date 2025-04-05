import json
import os
class user2():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        
    def to_dict(self):
        return {
            'name':self.name,
            'age':self.age,
            'city':self.place
        }
#sample data
#usra=user2(name="Antony",age=20,place='india')
#usrt=user2(name='Trishaa Raj',age=21,place='india')
#usr_lst=[usra,usrt]
usr_lst=[]
def write_to_usersdert(item:user2):
    usr_lst.append(item)
    usr_dict=[i.to_dict() for i in usr_lst]
    path='/home/antony/Desktop/ai_project/ai_proj/jerry_bot/usersdert.json'
    if os.path.exists(path):
        with open(path,'w') as file:
            json.dump(usr_dict,file,indent=4)
