"""
phrasetweet.py
em folsom, 2019, copyleft 
a really ugly way of making tweets that form a "phrase bowtie"
"""
import sys
str1 = ""
str2 = ""
pivotLetter = "" #shared letter at the start of str1 and str2


def validate(str1, str2):
    """
    Takes str1 and str2, determines whether they start with the same letter.
    Raises a ValueError if not true, which is handled in main().
    """
    if str1[0] == str2 [0]:
        pivotLetter = str1[0]
    else:
        raise ValueError("Phrases do not share common letter")

def trimLast(phrase):
    """
    Given a phrase, prints the phrase repeatedly on the terminal, with 
    the last char characters removed.
    """
    for char in range(len(phrase)):
        if char == 0: #Makes sure to print the full phrase first.
            print(phrase)
        else:
            print(phrase[:-char-1])

def trimFirst(phrase):
    """
    Given a phrase, prints the prhase repeatedly, starting with the first 
    character, then adding characters char+1 at a time.
    """
    for char in range(len(phrase)):
        if phrase[char] == " ":
            pass
        else:
            print(phrase[:char+1])

def main(str1, str2):
    """
    Given two strings, prints the result of trimLast() on str1 and trimFirst()
    on str2. Handles ValueError raised by validate().
    """
    try:
        validate(str1, str2)
    except ValueError:
        print("Strings do not share a first letter, proceed? (Y/N): ")
        option = input()
        if option.capitalize == "Y":
            pass
        elif option.capitalize == "N":
            sys.exit(0)
        else:
            validate(str1, str2)
    trimLast(str1)
    trimFirst(str2)

# generate output from command line args 
main(sys.argv[1], sys.argv[2])