#!/usr/bin/env python3

import re

# The repeating_letter_a function checks if the text passed includes 
# the letter "a" (lowercase or uppercase) at least twice.
def repeating_letter_a(text):
    result = re.search(r"a.*a+",text,re.IGNORECASE)
    return result != None

print(repeating_letter_a('banana')) # True
print(repeating_letter_a('pinnaple')) # False
print(repeating_letter_a('Animal Kingdom')) # True
print(repeating_letter_a('A is for apple')) # True
       