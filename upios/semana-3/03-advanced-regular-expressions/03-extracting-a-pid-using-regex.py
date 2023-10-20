#!/usr/bin/env python3

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# regex = r"\[(\d+)\]"
# result = re.search(regex, log)
# print(result) # match=['12345']
# print(result[1]) # 12345

# def extract_pid(log_line):
#     regex = r"\[(\d+)\]"
#     result = re.search(regex,log_line)
#     if result is None:
#         return ""
#     return result[1]

# print(extract_pid(log))

# Devuelve el mensaje en mayúsculas entre paréntesis 
# después de identificar el proceso
def extract_pid(log_line):
    regex = r"(\[(\d+)\]): ([A-Z]*)"
    result = re.search(regex,log_line)
    if result is None:
        return 'none'
    #return f"{result[1]} ({result[3]})"
    return "{} ({})".format(result[2], result[3])

print(extract_pid('July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade')) # (ERROR)
print(extract_pid('99 elephants in a [cage]')) # none
print(extract_pid('A string that alse has numbers [34567]but no uppercase message')) # none
print(extract_pid('July 31 07:51:48 mycomputer bad_process[12345]: RUNNING Performing package upgrade')) # (RUNNING)