#!/usr/bin/env python3

import re

# Fill the code to check if the text passed contains punctuation
# symbols: commas, periods, colons, semicolons, question marks 
# and exclamation points.

def check_punctuation(text):
    resutl =  re.search(r"[,;.?!]",text)
    return resutl != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressons awesome?")) # True
print(check_punctuation("Wow! we're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
