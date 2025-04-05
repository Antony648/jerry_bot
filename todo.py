from datetime import date
from enum import Enum
from uuid import uuid4

class STATUS(Enum):
    NOT_STARTED=0
    IN_PROGRESS=1
    COMPLETED=2

class Priority(Enum):
    LOW=0
    MEDIUM=1
    HIGH=2

class Item():
    __creation_date=date.today()
    __title="empty"
    __status=STATUS.NOT_STARTED
    __priority=Priority.LOW
    __flag=False
    __due_date=date
    __state=False
    __notes=""
    __icon=""
    
    def __init__(self,title=None):
        if title is not None:
            self.__title=title
        self.__id=str(uuid4())

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,title_val):
        self.__title=title_val

    @property
    def  priority(self):
        return self.__priority
    @priority.setter
    def priority(self,val):
        self.__priority=val

    @property
    def creation_date(self):
        return self.__creation_date
    @creation_date.setter
    def creation_date(self,val):
        self.__creation_date=val

    @property
    def due_date(self):
        return self.__due_date
    @due_date.setter
    def due_date(self,val):
        self.__due_date=val
    
    @property
    def notes(self):
        return self.__notes
    @notes.setter
    def notes(self,val):
        self.__notes=val

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,val):
        self.__status=val

    @property
    def flags(self):
        return self.__flags
    @flags.setter
    def flags(self,val):
        self.__flags=val

    @property
    def age(self):
        return self.__creation_date -date.today()

class Todo():
    __todos=[]
    def __init__(self):
        print("New todo list")
        self._current=-1

    def __iter__(self):
        return self
    def __next__(self):
        if self._current <len(self.__todos)-1:
            self._current+=1
            print("inside todos:",self.__todos[self._current].title)
            return self.__todos[self._current]
        else:
            self._current=-1
        raise StopIteration
    
    def __len__(self):
        return len(self.__todos)

    def new_item(self,item:Item):
        self.__todos.append(item)
        print("added "+item.title+"succesfully")

    @property
    def items(self)->list:
        return self.__todos
    
    def show(self):
        print("*"*80)
        for item in self.__todos:
            print(item.title,item.status,item.priority)

    def remove_item(self,title:str=None,uuid:str=None):
        if title == None and uuid==None:
            print("please specify th item properly.")
        for item in self.__todos:
            if title==item.title or uuid==item.uuid:
                print("item removed"+item.title+"successfully")
                self.__todos.remove(item)
                return True
        print("Item not found!")
        return False

'''i=Item("Get shopping")
l=Todo()
l.new_item(i)
l.show()
l.remove_item(title="Get shopping")
l.show()'''
