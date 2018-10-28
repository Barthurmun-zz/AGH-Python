#!/usr/bin/python3

import re

swap_list = {"i":"oraz", "oraz":"i", "nigdy":"prawie nigdy", "dlaczego":"czemu"}

filename = input("Write your file names :")
with open(filename,'r') as f:
    r_file = f.read()

doc = r_file.split(" ")

for count,word in enumerate(doc):
    for item in swap_list:
        if word == item:
            doc[count] = swap_list[item]
    
new_content = " ".join(doc)
with open(filename,'w') as f:
    f.write(new_content)
