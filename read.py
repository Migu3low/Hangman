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
    word_dict = dict(enumerate(word))

    def __init__(self, words, word, word_dict):
        self.words = words
        self.word = word
        self.word_dict = word_dict
        