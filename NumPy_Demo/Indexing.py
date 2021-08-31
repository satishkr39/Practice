import  numpy as np

arr = np.arange(0,11)
print(arr)

# indexing
print(arr[3])  # get index of 3rd item

# slice notation
print(arr[1:5])  # start from 1 and end before 5

print(arr[:6])  # from begin till 6

print(arr[5:]) # start from 5 end till last

# assigning const value to multiple index
arr[0:5] = 100  # this is called broadcasting, we are assigning value 100 to all index from 0 to 5
print("THE BROADCASTED ARRAY :: ", arr)
arr = np.arange(0,11)
print(arr)

# numpy tries to save memory and so when we perform = operator it assigns a reference instead of creating reference

# to create copy of array use copy()
arr_copy = arr.copy()
print("COPY OF MY ARR : ", arr_copy)

# getting item from 2D array
arr_2d = np.array([[5,10,15],[20,25,30],[45,40,45]])
print(arr_2d)
# getting 1st item
print(arr_2d[0][0])
print(arr_2d[0][1])  # getting 1st row 2nd column
print(arr_2d[1][1]) # get 2nd row 2nd column

# Another way to get items
print(arr_2d[1,2])  # 2nd row 3rd column

# slicing a sub-matrix
print("SLICED SUB-MATRIX ::\n ",arr_2d[:2,1:]) # get all rows till 2(0,1) and all columns from 1 till end
print(" GETTING THE ROWS : \n", arr_2d[:2])  # get two rows and all columns







