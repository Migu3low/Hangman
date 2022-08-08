from random import randrange
import os, platform
RUTA_DATA ="./data.txt"
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def play_again():
    print("1. Volver a Jugar")
    print("2. Salir")
    while(True):
        opcion = input("Desea volver a jugar (1=SI , 2=NO): ")
        if(opcion == "1"):
            return True
        elif(opcion=="2"):
            return False
        else:
            print("Ingrese una opción válida (1 o 2):")


def ganaste(word=""):
    print("""
    ▄████  ▄▄▄       ███▄    █  ▄▄▄        ██████ ▄▄▄█████▓▓█████ 
    ██▒ ▀█▒▒████▄     ██ ▀█   █ ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ 
    ▒██░▄▄▄░▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒███   
    ░▓█  ██▓░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ 
    ░▒▓███▀▒ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ░▒████▒
    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░
    ░   ░   ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░    ░     ░ ░  ░
    ░ ░   ░   ░   ▒      ░   ░ ░   ░   ▒   ░  ░  ░    ░         ░   
        ░       ░  ░         ░       ░  ░      ░              ░  ░
    """)
    return play_again()
def perdiste(word):
    print(HANGMANPICS[6])
    print("La palabra era: "+word)
    print("""
        ██▓███  ▓█████  ██▀███  ▓█████▄  ██▓  ██████ ▄▄▄█████▓▓█████ 
        ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▓██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ 
        ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   
        ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ 
        ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓ ░██░▒██████▒▒  ▒██▒ ░ ░▒████▒
        ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░
        ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒  ▒ ░░ ░▒  ░ ░    ░     ░ ░  ░
        ░░          ░     ░░   ░  ░ ░  ░  ▒ ░░  ░  ░    ░         ░   
                    ░  ░   ░        ░     ░        ░              ░  ░
                                ░                                   
    """)
    return play_again()

def cls():
    if(platform.system()=="Windows"):
        os.system("cls")
    elif(platform.system()=="Linux"):
        os.system("clear")

def remove_accents(word):
    no_accent = ""
    for letter in word:
        if(letter=="á"):
            no_accent = no_accent + "a"
        elif(letter=="é"):
            no_accent = no_accent + "e"
        elif(letter=="í"):
            no_accent = no_accent + "i"
        elif(letter=="ó"):
            no_accent = no_accent + "o"
        elif(letter=="ú"):
            no_accent = no_accent + "u"
        else:
            no_accent = no_accent + letter
    return no_accent
    
def random_word():
    with open(RUTA_DATA,"r",encoding="utf-8") as f:
        try: 
            data = f.readlines()
            if(data is not None or len(data)>0):
                random_word = data[randrange(0, len(data))].strip()
                #word_dict = {"word": random_word} | {index:False for index in range(len(random_word))}

                # #OlD PYTHON DICT MERGE (the old way)
                word_dict = {**{"word": random_word},**{index:False for index in range(len(random_word))}} 
                print(word_dict, "word_dict")
                return word_dict
        except FileNotFoundError as fe:
            print("No existe el archivo de datos [data.txt] > {}".format(RUTA_DATA))
        except Exception as error:
            print("Ocurrió un problema > {}".format(error))

def no_winner(word_dict):
    actual_word = word_dict["word"]

    for i in range(len(actual_word)):
        if(word_dict[i]==False):
            return True
    if(len(actual_word)>0):
        return False


def print_screen(word_dict, lives=6):
    print("""
        __    __       ___       _______ .__   __. .___  ___.      ___      .__   __. 
        |  |  |  |     /   \     /  _____||  \ |  | |   \/   |     /   \     |  \ |  | 
        |  |__|  |    /  ^  \   |  |  __  |   \|  | |  \  /  |    /  ^  \    |   \|  | 
        |   __   |   /  /_\  \  |  | |_ | |  . `  | |  |\/|  |   /  /_\  \   |  . `  | 
        |  |  |  |  /  _____  \ |  |__| | |  |\   | |  |  |  |  /  _____  \  |  |\   | 
        |__|  |__| /__/     \__\ \______| |__| \__| |__|  |__| /__/     \__\ |__| \__| 
        """)   
    hang = {7-i:HANGMANPICS[i] for i in range(len(HANGMANPICS))}
    if(lives>0):
        print(hang[lives+1]) 
    print("Adivina la palabra: ",end=" ")
    letters_count = len(word_dict["word"])

    for i in range(letters_count):
        if(word_dict[i]==True):
            print("   {}   ".format(word_dict["word"][i]), end="")
            pass
        else:
            print("  ___  ", end="")
    print()


def guess_letter(letter, word_dict):
    letter = letter.lower()
    
    actual_word = word_dict["word"]
    if(letter in remove_accents(actual_word)):
        for i in range(len(actual_word)):
            if( remove_accents(actual_word[i])==letter):
                word_dict[i]=True
        return True
    else:
        print("La letra {} NO está en la palabra".format(letter))
        return False

    # print_screen(word_dict)

def play(word_dict,lives=6):
    print_screen(word_dict, lives)

    keep_playing=True
    while(keep_playing):
        print("Tienes "+str(lives)+" vidas")

        try: 
            letter = input("Ingresa una letra: ")
            if(not letter.isalpha() or len(letter)!=1):
                raise ValueError("Debe ingresar una sola letra (no más ni menos)")
            if(not guess_letter(letter, word_dict)):
                lives-=1
            cls()
            print_screen(word_dict, lives)
            print(word_dict) #ESTA LINEA DEBERIA BORRARSE PARA NO VER LA RESPUESTA
        
        except ValueError as ve:
            print(ve)

        keep_playing = no_winner(word_dict)
        if(lives==0):
            keep_playing=False
    cls()

    if(lives>0):
        print("Descubriste la palabra: "+ word_dict["word"])
        keep_playing = ganaste()
    else:
        keep_playing = perdiste(word_dict["word"])


    if(keep_playing):
        cls()
        play(random_word())

def run():
    play(random_word())

if __name__ == "__main__":
    run()