import json
from Function.functions import getDef
from os import system

system("clear")
words = json.load(open("/home/tango/Documents/Python/DictionaryApp/Main/data.json"))


woord = input("Enter a word: ")
getDef(woord, words)
