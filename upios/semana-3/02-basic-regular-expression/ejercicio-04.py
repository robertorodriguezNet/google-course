#!/usr/bin/env python3

import re

# The code to check if the text passed has at least 2
# groups of alphanumeric characters separated by one 
# or more whitespace characters.
def check_character_groups(text):
    resutl = re.search(r'\w\s\w',text)
    return resutl != None

print(check_character_groups('One')) # False
print(check_character_groups('123 Ready Set Go')) # True
print(check_character_groups('username user 01')) # True
print(check_character_groups('Shopping_list: milk, bread, egs.')) # False