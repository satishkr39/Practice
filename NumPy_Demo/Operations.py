import  numpy as np

arr = np.arange(0,11)

# adding arr to itself
print("ADDING ARRAY TO ITSELF:\n",arr+arr)

# can perform similar operation wiht +,-, /, *

# adding 100 to each item
print("Adding 100 TO EACH ITEM: \n",arr+100)

print("DIVIDE BY ZERO GIVES WARNING: \n", arr/arr)

# multiply each item to power of 2
print("POWER OF 2: \n", arr ** 2)

# UNIVERSAL ARRAY FUNCTIONS

# taking sq root of each item
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))

# performing sum
print(np.sum(arr))
# performing sum along column
print(arr.reshape(2,5).sum(axis=0))