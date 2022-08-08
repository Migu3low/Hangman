import random
import os

class Start:
    print("Adivina la palabra")
    letter = input("Ingresa una letra: ")
    letter = letter.upper()

    def __init__(self, letter):
        self.letter = letter    


class Read:
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.upper()
            words.append(line)
    ind = random.randrange(0,172)
    word =""
    word = words[ind]
    word_dict = dict(enumerate(word))

    def __init__(self, words, word, word_dict):
        self.words = words
        self.word = word
        self.word_dict = word_dict

class Entry:
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

class Logic:
    verify = list(Entry.dict.values())
    while verify.count("") != 0:
        print(verify)
        Start.letter = input("Ingresa una letra: ")
        Start.letter = Start.letter.upper()

        key = 0
        for x in Read.word_dict.values():
            verify = list(Entry.dict.values())
            if x in Start.letter:
                Entry.dict[key] = x
                key += 1
            else:
                key += 1
        
    else:
        print(verify)

    def __init__(self, verify):
        self.verify = verify


if __name__=='__main__':
    Read
    Start
    Entry
    Logic

    
