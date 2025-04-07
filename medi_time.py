from datetime import time
class medi_time:
    def __init__(self):
        self.morning_time=time(hour=9,minute=0)
        self.morning_list=[]
        self.noon_time=time(hour=13,minute=1)
        self.noon_list=[]
        self.night_time=time(hour=9,minute=0)
        self.night_list=[]

    