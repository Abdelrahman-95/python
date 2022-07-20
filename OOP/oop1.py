names = ["abdelrahman","mohamed","mahmoud"]

# def mytitle(names:str)->str:
#     new_names = []
#     for name in names:
#         new_names.append(name.title())
#     print(new_names)

# mytitle(names)
# ==============================================

import functools 

# def mytitle(names:str)->str:
#     return names.title()

# new_names = map(mytitle, names)
# new_names = map(lambda x:x.title(),names)

# print(list(new_names))



# ===============================================

# List = [10,55,99,44,33,74,62,31]

# def bigger(List:list)->list:
#     if List > 50:
#         return True
#     elif List < 50:
#         return True

# new_List = filter(bigger, List)
# print(list(new_List))

# ================================================

# from functools import reduce

# number = [22,333,44,55]
# def sum(x:list,y:list)->int:
#     return x+y

# summ = reduce(sum,number)
# print(summ)