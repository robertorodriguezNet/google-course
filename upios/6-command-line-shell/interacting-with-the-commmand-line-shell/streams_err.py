#!/usr/bin/env python3
 
data = input("This will come from STDIN: ")
print("Now we write it to STDOU: " + data)
raise ValueError("Now we generate an error to STDERR")