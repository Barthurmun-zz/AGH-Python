#!/usr/bin/python3

a = [1,2,12,4]
b = [2,4,2,8]

result = 0
for count,item in enumerate(a):
    result = result + (item * b[count-1])

print(result)