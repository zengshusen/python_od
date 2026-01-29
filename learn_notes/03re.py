import re
data = "023"
pattern="[1]"
print(re.findall(pattern,data))
data="0123"
pattern="[1]"
print(re.findall(pattern,data))