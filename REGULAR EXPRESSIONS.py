text="From abdtariq78@gmail.com sat jan 5 09:14:16 2008"
import re
data=re.findall('@([^ ]*)',text)
print(data)
data=re.findall('[0-9]+',text)
print(data)
data=re.findall('^From ([^ ]+)',text)
print(data)