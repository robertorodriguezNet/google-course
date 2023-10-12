#!/usr/bin/env python3
import os

dir = 'website'
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    print(f"{fullname} is a directory" if(os.path.isdir(fullname)) else f"{fullname} is a file")