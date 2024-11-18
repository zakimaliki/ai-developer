# perberdaan list dan numpy array

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# print(a*b)

import numpy as np  # type: ignore

a = np.array([1, 2, 3, 4, 5]) 
b = np.array([6,7,8,9,10])
print(a*b)
print(a)
print(b)


# membuat array 2D

Array2D = np.array([
    [1, 2, 3, 4, 5 ],
    [6, 7, 8, 9, 10],
    [11,12,13,14,15]
])
print("Array 2D:")
print(Array2D)
print("Index array 2D:")
for i in range(Array2D.shape[0]):
    for j in range(Array2D.shape[1]):
        print(f"Index [{i}][{j}]: {Array2D[i][j]}")



# membuat array 3D
Array3D = np.array([
    [[1 ,2 ,3 ],[4 ,5 ,6 ]],
    [[7 ,8 ,9 ],[10,11,12]],
    [[13,14,15],[16,17,18]]
])
print(Array3D)
print("Index array 3D:")
for i in range(Array3D.shape[0]):
    for j in range(Array3D.shape[1]):
        for k in range(Array3D.shape[2]):
            print(f"Index [{i}][{j}][{k}]: {Array3D[i][j][k]}")

