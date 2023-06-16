# List unpacking, also known as iterable unpacking, is a feature
# in Python that allows you to assign the elements of a list
# (or any iterable) to multiple variables in a single line.
# It provides a convenient way to extract values from a list
# and assign them to separate variables.

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9,10]

print(a)
print(b)
print(c)
print(other)
print(d)