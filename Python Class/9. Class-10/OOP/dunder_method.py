# dunder mean double underscore and which method begin and end with double underscore called dunder and define behaviour of object 

# __str__
# use for sring representation return only string

# class Book:
#     def __init__(self,title,author,year):
#         self.author = author
#         self.year = year
#         self.title = title
#     def __str__(self):
#         return f"{self.title} by {self.author} in {self.year}"
# book = Book("1978","Georage",2000)
# print(book)

# __getitem__ __setitem__ __deleteitem__
#  allow you to define custom behavior for accessing, setting, and deleting items in your objects using the indexing syntax. These methods make your objects behave like sequences
class CustomList:
    def __init__(self,*args):
        self.items = list(args)
    def __getitem__(self,index):
        return self.items[index]
    def __setitem__(self,index,value):
        self.items[index] = value
    def __delitem__(self,index):
        del self.items[index]
    def __str__(self):
        return str(self.items)
obj = CustomList(1,2,3,4,5,6)
del obj[1]
print(obj)
print(obj[2])
obj[3] = 9
print(obj)
