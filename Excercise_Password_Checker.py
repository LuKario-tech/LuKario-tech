# Make a program for password checker.

# print('@' * 10) You can do this for any piece of string

user_name = input("What is your username? ")
password = input("What is your password? ")
length = len(password)
secret = length * "*"

print(f"Hi {user_name}. Your password {secret} is {length} letters long.")
