car={
    'color':'red',
    'model':'honda',
    'seat':[1,2,3,4],
    'original':None,
    'good':None    
}
# print(car)                        # value can same but no key
#convert
# car=dict(color='red',model='honda',seat='4')
# print(car)

#Access

# a = car['color']
# print(a)
#get can return 
# print(car.get("color"))

# key
# x = car.keys()
# print(x)
# car["type"] = True
# print(x)


# print(car.values())
# car["price"] = "1234"
# car['color'] = "yellow"


# print(car.items())
# car["price"] = "1234"
# car['color'] = "yellow"
# print(car.items())

# print(car.items())
# car['color']='yellow'
# car['price']=2345
# print(car.items())

# add
# car['price']=3544
# car.update({'trye':True})
# print(car)

# update
# car['color']='yellow'
# car.update({'model':'toyota'})
# print(car)

# remove
# pop can return and argument as key
# a=car.pop("color")    
# print(a)
# popitem can return or no argument
# a=car.popitem()
# print(a," ",car)
# del car['color']
# print(car)
# clear no return
# a=car.clear()
# print(a,"  " ,car)



# output = car.pop("color")
# output = car.popitem()
# output = car.clear()
# del car['color']
# print(output,"car",car)


#Looping 
# for i in car:
#     print(i)
# for a in car.keys():
#     print(a)


# for a in car:
#     print(car[a])
# for i in car.values():
#     print(i)

# for a in car.items():
#     print(a)

# copy
# car1=car.copy()
# print(car1)


# for i in car:
#     print(i)


# for i in car:
#     print(car[i])

for i in car.values():
    print(i)

