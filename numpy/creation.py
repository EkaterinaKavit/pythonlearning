import numpy as np

my_numpy = np.array((1, 2, 3))
my_numpy1 = np.array([[1, 2],[3, 4],[5, 6]])
my_numpy_3mer = np.array([[[1, 2],[3, 4]],
                             [[5, 6],[7, 8]],
                             [[9, 10],[11, 12]]])

numpy_null_10 = np.array([0]*10)
print(numpy_null_10)

numpy_number_1 = np.array([1]*15)
print(numpy_number_1)

numpy_random = np.array([x for x in range(10)])
print(numpy_random)
# print(my_numpy_3mer.shape)
# print(my_numpy_3mer[0,0,0])
# print(my_numpy_3mer[1,1])
# print(my_numpy1)
my_numpy[0] = 5
# print(my_numpy[[1,1,1]])



print(np.empty(10, dtype = 'int16')) # массив без определенных размеров заданного размера

print(np.empty((3,2), dtype = 'int16')) # массив без определенных размеров заданного размера

print(np.eye(4)) # создает матрицу с единицами по диагонали, остальные элементы нули


