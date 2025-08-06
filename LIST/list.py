# an empty list
my_list = []

# append element into the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert 15 at index 1
my_list.insert(1, 15)

# extend the list by this cawith with 50, 60, and 70
my_list.extend([50, 60, 70])

#remove the last element
my_list.pop()

# sorting the list in ascending order
my_list.sort()  

# find and print index of value 30
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")
