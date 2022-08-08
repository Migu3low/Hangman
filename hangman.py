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


    if Logic.list.count("") != 0:
        Start.letter = input("Ingresa una letra: ")
        Start.letter = Start.letter.upper()

        new_turn = {"Start.letter" for x in Logic.dict if x == "Start.letter"}
        print(new_turn)