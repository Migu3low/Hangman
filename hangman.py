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

    

    verify = list(Logic.dict.values())
    while verify.count("") != 0:
        print(verify)
        Start.letter = input("Ingresa una letra: ")
        Start.letter = Start.letter.upper()

        key = 0
        for x in Read.word_dict.values():
            verify = list(Logic.dict.values())
            if x in Start.letter:
                Logic.dict[key] = x
                key += 1
            else:
                key += 1
        
    else:
        print(verify)



