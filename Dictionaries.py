# In simple language, a dictionary in Python is like a real-life
# dictionary that contains words and their meanings. In programming,
# a dictionary is a collection of key-value pairs. The key
# acts as the word, and the value represents its meaning.
# For example, imagine you have a dictionary for storing information
# about a person. The keys could be things like "name," "age," and
# "city," and the values would be the specific information associated
# with each key. You can access the values by using the
# corresponding keys.

# Overall, dictionaries provide a convenient way to organize and
# access data using meaningful keys, just like a dictionary helps
# you find the meaning of words.

dict # stands for Dictionary in Python

dictionary = {
    "a": 1,
    "b": 2 
}

print(dictionary["b"])

dictionary_2 = {
    "a": [1,2,3],
    "b": "Hello",
    "c": True 
}

print(dictionary_2["a"])
print(dictionary_2["a"][1])

my_list = [
    {
    "a": [1,2,3],
    "b": "Hello",
    "c": True 
},
     {
    "a": [1,2,3],
    "b": "Hello",
    "c": True 
}
]

print(my_list[0]["a"][2])