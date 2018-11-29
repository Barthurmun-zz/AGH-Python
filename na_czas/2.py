import re

str = "haababas 764-124-632 gagarvsesges 765-254-875 fafasf"
pattern = "\d{3}-\d{3}-\d{3}"

pat = re.findall(r'\d{3}-\d{3}-\d{3}',str)

print(pat)