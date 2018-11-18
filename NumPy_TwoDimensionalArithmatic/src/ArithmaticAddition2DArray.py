import numpy as np

np_mat = np.array([[1, 2], [3, 4],[5, 6]])

print(np_mat * 2)
print("\n##################\n")
print(np_mat + np.array([10, 10]))
print("\n##################\n")
result = np_mat + np_mat

print(result)

#Calculating Mean from a given array using numpy
array_data = [1,4,8,10,12]
np_mean = np.mean(array_data)
np_meadian = np.median(array_data)
print("Mean from the array np_mean = ")
print(np_mean)
print(np_meadian)