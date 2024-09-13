# Strings
string1 = "Hello"
string2 = "World"

# Strings Concatenation
string3 = string1 + " " + string2  


print("Concatenated String:", string3)

# Strings Indexing
print("First character of string1:", string1[0])

# Strings Slicing
print("Slice of string3:", string3[0:5])

# Strings Repetition
print("Repetition of string1:", string1 * 3)

# Lists
num = [1, 2, 3, 4, 5]
rainbow = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]


result_list = num + rainbow


# List Concatenation
print("Concatenated List:", result_list)


# List Indexing
print("First element of num:", num[0])

# List Slicing
print("Slice of result_list:", result_list[2:5])

# List Repetition
print("Repetition of rainbow:", rainbow * 2)


# Tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")

tuple3 = tuple1 + tuple2

# Concatenation
print("Concatenated Tuple:", tuple3)

# Indexing
print("First element of tuple1:", tuple1[0])

# Slicing
print("Slice of tuple3:", tuple3[1:4])

# Repetition
print("Repetition of tuple2:", tuple2 * 2)


# Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}


# Creation
dict3 = {**dict1, **dict2}  

# Concatenation
print("Concatenated Dictionary:", dict3)

# Indexing
print("Value for key 'a' in dict1:", dict1["a"])

# Sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Creation
set3 = set1.union(set2)

# Concatenation
print("Union of Sets:", set3)