import re

string  =  "Man a plan a canal; @ 1 panama panama panama"

vowels = re.findall(r'[aeiou]', string, re.IGNORECASE)
print("Vowels found:", vowels)

if string == string[::-1]:
    print(string)

replace = re.sub(r'[aeiou]', '*', string)

match = re.search(r'panama|canal', string, re.IGNORECASE)

matchs = re.findall(r'panama|canal', string, re.IGNORECASE)

if match:
    print("Match found:", matchs)


print(replace)
print(string.replace('@1',''))
print(string.isalpha())
print(string.isalnum())
print(string.lower())


list=[1,1,1,0,1,1]
max=[]
current_max=0
previous=list[0]

for value in list:
    if previous == value:
        current_max += 1
    else:
        max.append(current_max)
        current_max=0
        previous=value
max.sort(reverse=True)
print(max[0])

string ="hello"

left = vowels[0]
right = vowels[-1]
vowels= ""
if left == right:
    vowels


