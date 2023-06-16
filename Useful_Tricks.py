basket = ["a", "x ", "b", "c", "d", "e", "d"]

basket.sort()
basket.reverse()
print(basket[::-1])
print(basket)

# Range
a = range(1, 100)
print(a)

b = list(a)
print(b)

c = list(range(100))
print(c)

# Join
# Converts the elements of an iterable into a string

sentence = "@"
new_sentence = sentence.join(["Hi", "my", "name", "is", "Goku"])

print(new_sentence)

a = " ".join(["Hi", "my", "name", "is", "Goku"])
print(a)