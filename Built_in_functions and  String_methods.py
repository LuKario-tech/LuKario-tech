print(len("KAMEHAMEHA BY GOKU"))
# This function shows length of a string.

a = "KAMEHAMEHA BY GOKU"
print(a[0:len(a)])

# Following are some string methods

b = "a bowl is useful when it is empty."

print(b.upper()) # upper() is used to make the string characters in capital.
print(b.capitalize()) # capatilize() is used to make first character of string in chapital
print(b.find("o")) # find() is used to find out at which index does the character is occured for the first time.
print(b.replace("useful", "useless")) # We use this letter in order to replace all the occurence of a specific character in a string.

print(b) # As you can see the string is still immutable even though we have done some changes in it.