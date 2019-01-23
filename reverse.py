str1=str(raw_input())
str2=str1[::-1]
import re
print(re.sub("e|i|o|u|a|A|E|I|O|U","",str1))
