import re


def is_isogram(string):
    string = re.sub("[^A-Za-z]", "", string)
    string = string.lower()
    return len(set(string)) == len(string)
