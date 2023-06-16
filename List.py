# In Python, lists are a versatile and commonly used
# data structure that allows you to store and manipulate
# a collection of items. Lists are ordered, mutable,
# and can contain elements of different data types

li = [1,2,3,4,5]
li2 = ["a", "b", "c"]
li3 = [1,2,"a", True]

# Data Structure
# In Python, a data structure is a way of organizing and storing data
# in a structured manner, allowing for efficient manipulation and retrieval
# of the data. Python provides several built-in data structures, including
# lists, tuples, sets, dictionaries, Arrays, Linked Lists, Stacks, Ques etc.
# Additionally, Python offers the flexibility to create custom data
# structures using classes and objects.

# Lists can be used in as an amazon shoppin cart such as follows

amazon_cart = ["Notebooks", "Sunglasses", "Anime Figures", "Ps5"]
print(amazon_cart[2])

# List Slicing
# List slicing is a technique in Python that allows you to extract
# a portion of a list by specifying a range of indices. It provides
# a convenient way to access multiple elements from a list at once.

# print(amazon_cart[0:4:2])

# List are immutable

amazon_cart[0] = "Laptop"
# new_amazon_cart = amazon_cart[0:3]
# new_amazon_cart[0] = "Tokyo Ghoul Mask" # With this we have modified the list

# print([new_amazon_cart])
# print(amazon_cart)

new_amazon_cart = amazon_cart[:] # With this we have copied the lsit
new_amazon_cart[0] = "Tokyo Ghoul Mask"
print(new_amazon_cart)
print(amazon_cart)