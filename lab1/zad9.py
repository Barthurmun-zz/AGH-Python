#!/usr/bin/python3

import re

list_of_files = []
filename = input("Write your file names :")


with open(filename,'r') as f:
    r_file = f.read()

new_content = re.sub(r'\s(się|i|oraz|nigdy|dlaczego)','',r_file)
with open(filename,'w') as f:
    f.write(new_content)




