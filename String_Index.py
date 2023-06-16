# In Python, a string index refers
# to the position of an individual character within a string.
# Each character in a string is assigned an index number,
# starting from 0 for the first character and incrementing by 1 for
# each subsequent character.
# String indexing allows you to access or manipulate
# specific characters or subsequences within a string.

a = "Elephant"
#    01234567

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])

# There are many things under this string index such as [start:stop]

print(a[0:1])
print(a[0:2])
print(a[0:3])
print(a[0:4])
print(a[0:5])
print(a[0:6])
print(a[0:7])
print(a[0:8])

# There is one more thing that we can do which is called step over
# such as [start:stop:stepover]

print(a[0:8:1])
print(a[0:8:2])
print(a[0:])
print(a[:7])
print(a[::2])
print(a[-1])
print(a[::-2])
print(a[:])