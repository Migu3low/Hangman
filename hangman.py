import random
import os

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

class Logic:

    os.system("clear")
    list1 = []
    letter = "_"
    for i in Read.word:
        if i == letter:
            list1.append(i)
        else:
            list1.append("_")
    dict = dict(enumerate(list1))
    verify = list(dict.values())

    while verify.count("_") != 0:
        os.system("clear")
        
        print("Adivina la palabra")
        for line in verify:
            print(line + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ")
        assert letter.isalpha(), "Solo puedes ingresar letras"
        letter = letter.upper()
        
        key = 0
        for x in Read.word_dict.values():
            verify = list(dict.values())
            if x in letter:
                dict[key] = x
                key += 1
            else:
                key += 1
        
    else:
        os.system("clear")
        print(f"""¡Lo Lograste! La palabra era:
         
        {Read.word.upper()}
        
        """)

    def __init__(self, list):

        self.list = list


if __name__=='__main__':
    Read
    Logic

    
