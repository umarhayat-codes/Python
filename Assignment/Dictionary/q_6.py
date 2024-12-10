# Challenging Problems

dict1 = {'a': 5, 'b': 10} 
dict2 = {'a': 3, 'b': 7,'b' : 5}
dict3 ={}
for key,value in dict1.items():
    if key in dict2:
        dict3[key] = value + dict2[key]
print(dict3)



n = int(input("Enter the number:"))
dic = {}
for i in range(1,n+.1):
    dic[i] = i ** 3
print(dic)



nested_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
flatted = {}
for key,value in nested_dict.items():
    for subkey,subvalue in value.items():
        flatted[f'{key} . {subkey}'] = subvalue
print(flatted)



dic4 = {'a' : 1,'b': 2,'c': 3}
even_dic = {}
odd_dic = {}
for key, val in dic4.items():
    if val % 2 == 0:
        even_dic[key] = val
    else:
        odd_dic[key] = val
print(even_dic)
print(odd_dic)



dic5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filter_dic = {}
for key, val in dic5.items():
    if val < 3:
        filter_dic[key] = val
print(filter_dic)