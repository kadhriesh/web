# from collections import Counter
#
# from test.test import vowels
#
# num_list = [1, 3, 4, 2, 7, 12]
#
# data = [i for i in num_list if i % 2 == 0]
# print(data)
#
#
# list = ['onion', 'apple', 'banana', 'apple', 'grape','potato',]
# item_count = Counter(list)
#
# print(item_count)
# unique = set(list)
#
# fruit= ['apple', 'banana', 'orange', 'grape']
# vegitable = ['onion', 'potato']
#
# fruitlist = []
# for item in item_count.keys():
#     if item in fruit:
#         for i in range(0,item_count[item]):
#             fruitlist.append(item)
#
# print(fruitlist)

# -> ['e', 'o']

# 'hello' -> 'holle'
import re

string = 'hello'
output=[]
vowels_list = re.findall(r'[aeiou]', string)
vowels_list_length = len(vowels_list)-1

for char in string:
    if char in vowels_list:
        output.append(vowels_list[vowels_list_length])
        vowels_list_length -= 1
    else:
        output.append(char)

print(''.join(output))




