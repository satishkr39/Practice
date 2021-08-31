import numpy as np

arr = np.arange(0,11)
bool_array = arr>5 # iterates over all value and prints True or False based on condition
print("OUR BOOLEAN ARRAY :\n", bool_array)

# using our bool_array to get items from parent arr
print(arr[bool_array])  # prints only those where True is met

# Another way
print(arr[arr>5])  # prints only those where item > 5

