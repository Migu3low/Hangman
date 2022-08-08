import random

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

    def __init__(self, words, word):
        self.words = words
        self.word = word
        