# Immutability, in the context of Python, means that once an object
# is created, it cannot be changed. It remains fixed or unchangeable.
# This applies specifically to certain data types, such as strings and tuples.

a = 200
# a[0] = "1"
# print(a)

# We cannot do the above function as variable a is immutable.
# In order to change the value of a we can do this by completely reassign
# the value.

a = "1"
print(a)