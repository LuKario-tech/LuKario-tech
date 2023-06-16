basket = ["a", "b", "c", "d", "e", "d", "w", "y"]

# Index
a = basket.index("e", 0, 5)
print(a)
print("a" in basket)
print("x" in basket)
print('H' in "KAMEHAMEHA")
print('h' in "KAMEHAMEHA")

# Count
print(basket.count("d"))

# Sort
basket.sort()
print(basket)
print(sorted(basket)) # It does not modify the original list
print(basket)

# Copy
n = basket.copy()
print(n)

# Reverse
basket.reverse()
print(basket)