from os import read
from random import randint
import os


def read_file():
    try:
        with open("./archivos/data.txt", "r", encoding="utf-8") as file:
            word_list = [word.strip("\n") for word in file]
        return word_list
    except FileNotFoundError as fnfe:
        print(fnfe)

def pick_secret_Word():
    word_list = read_file()
    rand_index = randint(0, len(word_list))

    return word_list[rand_index]

def print_guests(g):
    word = ""
    for letter in g:
        word += letter + " "
    print(word)

def guest_a_letter():
    keep_going = True
    while keep_going:
        letter_guest = input("\nIngresa una letra: ").lower()
        if not letter_guest.isalpha() or len(letter_guest) != 1:
            print("Por favor ingresa solo una letra!")
        else:
            keep_going = False
            return letter_guest

def get_indexes(sw ,lg):
    """This function gets the indexes of the letter_guest by the user in the secret word (sw=secret_word, lg=letter_guest) """
    
    res = [x for x, z in enumerate(list(sw)) if z == lg]
    return res

def run():
    
    secret_word = pick_secret_Word()
    guests = ["_" for i in range(len(secret_word))]
    # guests = {l: "_" for l in secret_word} 


    print(secret_word)

    #TODO: Problema al crear el diccionario guests cuando se imprime no imprime letras iguales

    while True:
        print("\n¡Adivina la palabra!")
        print_guests(guests)
        letter_guest = guest_a_letter()
        indexes_of_lg_in_sw = get_indexes(secret_word, letter_guest)

        for index in indexes_of_lg_in_sw:
            guests[index] = letter_guest
        
        os.system("clear")

        if "_" not in guests:
            print(f"Felicidades has ganado, la palabra secreta era: '{secret_word}'")
            return False

if __name__ == '__main__':
    run()