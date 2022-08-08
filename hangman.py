from re import L
from read import Read
from start import Start
import os

class Logic:
    list = []
    for i in Read.word:
        if i == Start.letter:
            list.append(i)
        else:
            list.append("")
    dict = dict(enumerate(list))

    print(f"""
    Adivina la palabra
    ******************
    {list}
    
    Ingresa una letra: 
    """)

    def __init__(self, dict):
        self.dict = dict


if __name__=='__main__':
    Read
    Start
    Logic

    word =  {0:"M", 1:"A", 2:"S", 3:"T", 4:"I", 5:"L"}
    letter =  "S"
    dict = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"L"}
    key = 0
    for x in word.values():
        if x in letter:
                dict[key] = x
                key += 1
        else:
                key += 1
	
	
print(dict)


