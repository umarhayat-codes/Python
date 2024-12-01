def flatten(lis):
    flatten_list = []
    for i in lis:
        if type(i) == list:
            for j in i:
                flatten_list.append(j)
        else:
            flatten_list.append(i)
    return flatten_list
lis = [[1,2],[3,4],[5,6]]
print(flatten(lis))