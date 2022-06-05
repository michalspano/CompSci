#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Regex expressions in Python
"""

import re as regex
from random import randint

def main():

    # Generate a random text of words
    words: list = []
    for i in range(randint(5, 100)):
        word: str = ''.join([chr(randint(97, 122)) for _ in range(randint(3, 10))])
        words.append(word)
    
    text: str = ' '.join(words)
    print(text, '\n')
    
    # Compose a patter - find all words starting with <user's choice>
    p: str = input('Find words that start with: ')
    pattern = fr"\b{p}\w+"
   
    # Search for the pattern in the text
    match: str = ' '.join(match for match in regex.findall(pattern, text))
    print(f'Match: {match!r}')


if __name__ == '__main__':
    main()
