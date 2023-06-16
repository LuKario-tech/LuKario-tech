name = "Johnny"
age = 55
print("Hi " + name +'. You are ' + str(age) + ' years old.')

# Instead of doing the above we can use formatted strings in order make our code easy to understand.

print(f"Hi {name}. You are {age} years old.")

# Before python 3 we had some different to accomplish this.

print("Hi {}. You are {} years old.".format("Johnny", "55"))
print("Hi {}. You are {} years old.".format(name, age))

# To change the order of format we can use this.
print("Hi {1}. You are {0} years old.".format(name, age))

# We can also create new variables while formatting our code.
print("Hi {new_name}. You are {age} years old.".format(new_name = "Sally", age = 100))