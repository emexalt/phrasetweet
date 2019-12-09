"""
phrasetweet.py
em folsom, 2019, copyleft
a really ugly way of making tweets that form a "phrase bowtie"
eg: 
"""
from sys import exit
str1 = ""
str2 = ""
pivotLetter = ""


str1 = input("Please enter a string. ")
str2 = input("Enter a second string, starting with the same letter. ")


def validate(str1, str2):
    if str1[0] == str2 [0]:
        pivotLetter = str1[0]
    else:
        raise ValueError("Phrases do not share common letter")

def trimLast(phrase):
    for char in range(len(phrase)-1):
        if len(phrase) < 2 or len(phrase) == 0 or phrase[char] == " ":
            pass
        else:
            print(phrase[:-char])

def trimFirst(phrase):
    for char in range(len(phrase)):
        if phrase[char] == " ":
            pass
        else:
            print(phrase[:char])

def main(str1, str2):
    try:
        validate(str1, str2)
    except ValueError:
        print("Strings do not share a first letter, proceed? (Y/N): ")
        option = input()
        if option.capitalize == "Y":
            pass
        elif option.capitalize == "N":
            exit(0)
        else:
            validate(str1, str2)
    trimLast(str1)
    trimFirst(str2)

main(str1, str2)