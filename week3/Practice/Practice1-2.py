import sys

list2 = sys.argv[1:]
print(list2)

list1 = ["hello", 1, True]

list1.extend(list2)
print(list1)

list1 = ["hello", 1, True]
list1.append(list2)
print(list1)

new_list = [5, 10, "Armenia"]
print('new list = ',list1+new_list)