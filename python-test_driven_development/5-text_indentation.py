#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = 0
    while char < len(text) and text[char] == " ":
        char += 1
    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("")
                print("")
                char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
