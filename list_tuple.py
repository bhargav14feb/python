# list is a data type which can contain multiple data types in it 
list= ["hello", 494, 399, "hello world"]
# list can also be sliced like strings
print(list[1:4])
list.append("hello")
list.count("hello")
list.index("hello")
list.pop(3)
list.remove(494)
list.insert(2, "inserted")
# list.sort()  # This will sort the list, but it will raise an error because of mixed types
# list.reverse()  # This will reverse the list, but it will raise an error because of mixed types
print(list)

# tuple is also a data type which can contain different datatype and it is immuatable 
tuple = ("hello world", 848, 990.33, "pound")
print(tuple.count("hello world"))
print(tuple.index("hello world"))
