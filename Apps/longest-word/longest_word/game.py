# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random
import requests

class Game:
    '''
    Used to validate longest word from a string
    '''
    def __init__(self) -> list:
        '''Attribute a random grid to size 9'''
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        '''Return True if and only if the word is valid, given the Game's grid'''
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        is_english = self.__check_dictionary(word)
        return is_english


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']
