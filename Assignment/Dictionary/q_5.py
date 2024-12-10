# Applications of Dictionaries

s = "hello world hello python world"
dic1 = {}

for word in s.split():
    if word in dic1:
        dic1[word] += 1
    else:
        dic1[word] = 1
print(dic1)


dic2 = {'a': 10, 'b': 15, 'c': 7}
max_value = 0
max_key = None
for key,value in dic2.items():
    if  value > max_value:
        max_value = value
        max_key = key
print(max_key)


dic3 = {}
for x in range(1,6):
    dic3[x] = x ** 2
print(dic3)


dic4 = {'a': 10, 'b': 15, 'c': 10, 'd': 15}
unique_dic = {}
for key,value in dic4.items():
    if value not in unique_dic:
        unique_dic[key] = value
print(unique_dic)


def find_key(dic,key):
    if key in dic:
        return dic[key]
    return "Key not found"
print(find_key({'a':1,'b':2},'b'))
