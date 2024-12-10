# Advanced Dictionary Usage

dict1 = {'a': 1, 'b': 2}  
dict2 = {'c': 3, 'd': 4} 



dict3 = {}
for key, value in dict1.items():
    dict3[key] = value
for key, value in dict2.items():
    dict3[key] = value
print(dict3)



list_of_tuple = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]
print(dict(list_of_tuple))



unsorted = {'z': 1, 'a': 2, 'c': 3}
print((sorted(unsorted.items())))



original_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict = {}
for key, value in original_dict.items():
    reverse_dict[value] = key
print(reverse_dict)




def dict_identity(dic1,dic2):
    return dic1 == dic2
print(dict_identity({'a':1,'b':2},{'c':3,'d':4}))