basket = [1,2,3,4,5]

# Adding
basket.append(100)
print(basket)

basket.insert(3, 200)
print(basket)

basket.extend([400,500,600])
print(basket)

# Removing
basket.pop()
basket.pop(0) 
print(basket)
basket.remove(100)
print(basket)

# pop returns the value in itstelf
new_basket = basket.pop(4)
print(new_basket)

basket.clear()
print(basket)