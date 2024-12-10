# Nested Dictionaries

info = {
    'Person' : {
    'Name' : 'jhon',
    'age' : 30,
    'Address' : {
        'Street' : '123 Elm St',
        'City' : 'Boston'
    }
    }
}

print(info['Person']['Address']['City'])



info['Person']['Address']['Phone'] = '123-456-7890'
print(info)



info['Person'].pop('Address')
print(info)



for key, value in info.items():
    print(key)
    for i,j in value.items():
        print(i,j)