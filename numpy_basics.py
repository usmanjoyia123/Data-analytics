import numpy as np 

print("****** np.empty Usage ******\n")
a = np.empty(shape=[2,2], dtype=int)
print(a)
print("\n")


print("****** np.eye Usage ******\n")

# N is the number of rows
# M is the number of columns

b = np.eye(N=2, M=2, k=0, dtype=int)
print("For k=0\n")
print(b)
print("\n")

c = np.eye(N=2, M=2, k=1)
print("For k=1\n")
print(c)
print("\n")


print("****** np.identity Usage ******\n")

# n is the dimension of square numpy array

d = np.identity(n=2, dtype=float)

print(d)
print("\n")


print("****** np.linspace Usage ******\n")

e = np.linspace(start=1.0, stop=5.0, num=5)
print("Including the stop element\n")
print(e)
print("\n")

f = np.linspace(start=1.0, stop=5.0, num=5, endpoint=False)
print("Excluding the stop element\n")
print(f)
print("\n")

print("****** np.ones Usage ******\n")
g = np.ones(shape=(5,3), dtype=int)
print(g)
print("\n")

print("****** np.zeros Usage ******\n")

h = np.zeros(shape=(5,5), dtype=int)
print(h)
print("\n")


print("****** np.array_split Usage ******\n")
a = np.array([1,2,3,4,5,6,7,8,9,10])
print("Splitting {} as \n".format(a))
print(np.array_split(a, 3))
print("\n")

print("****** np.column_stack Usage ******\n")
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([7,8,9])
print("Stacking the 3 below \n")
print(x)
print(y)
print(z)
print("\n")
print("Result is \n")
print(np.column_stack((x,y,z)))
print("\n")

print("****** np.concatenate Usage ******\n")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print("Concatenating the 2 below along the column axis\n")
print(a)
print(b)
print("\n")
print("Result is \n")
print(np.concatenate((a, b), axis=0))
print("\n")

print("****** np.hsplit Usage ******\n")
x = np.arange(16.0).reshape(4, 4)
print("Making 2 Horizontal splits(column wise) of below array \n")
print(x)
print("\n")
print("Result is \n")
print(np.hsplit(x, 2))
print("\n")

print("****** np.hstack Usage ******\n")
a = np.array([[1],[2],[3]])
b = np.array([[2],[3],[4]])
print("Stacking the below 2 horizontally (column wise) \n")
print(a)
print(b)
print("\n")
print("Result is \n")
print(np.hstack((a,b)))
print("\n")


print("****** np.squeeze Usage ******\n")
x = np.array([[[0], [1], [2]]])
print("Before Squeezing \n")
print("x : {}\n".format(x))
print("Shape of x : {}".format(x.shape))
print("\n")
print("After squeezing \n")
print("x : {}\n".format(np.squeeze(x)))
print("Shape of x : {}".format(np.squeeze(x).shape))
print("\n")

print("****** np.vsplit Usage ******\n")
x = np.arange(16.0).reshape(4, 4)
print("Making 2 Vertical splits(row wise) of below array \n")
print(x)
print("\n")
print("Result is \n")
print(np.vsplit(x, 2))
print("\n")

print("****** np.vstack Usage ******\n")
a = np.array([[1],[2],[3]])
b = np.array([[2],[3],[4]])
print("Stacking the below 2 vertically (row wise) \n")
print(a)
print(b)
print("\n")
print("Result is \n")
print(np.vstack((a,b)))
print("\n")



a = np.arange(6).reshape(2,3) + 10
print("The numpy array is \n")
print(a)
print("\n")

print("****** np.argmax Usage ******\n")
print("The index of maximum value from the flattened version is \n")
print(np.argmax(a))
print("\n")

print("The indices of maximum values along the column are \n")
print(np.argmax(a, axis=0))
print("\n")

print("The indices of maximum values along the row are \n")
print(np.argmax(a, axis=1))
print("\n")



print("****** np.argmin Usage ******\n")

print("The index of minimum value from the flattened version is \n")
print(np.argmin(a))
print("\n")

print("The indices of minimum values along the column are \n")
print(np.argmin(a, axis=0))
print("\n")

print("The indices of minimum values along the row are \n")
print(np.argmin(a, axis=1))
print("\n")


print("****** np.sort Usage ******\n")

b = np.array([[1,4],[3,1]])
print("Numpy array before applying the sorting operation \n")
print(b)
print("\n")
print("The result of sorting along the last axis \n")
print(np.sort(b))
print("\n")

print("The result of sorting the flattened version of the array \n")
print(np.sort(b, axis=None))
print("\n")

print("The result of sorting along the first axis \n")
print(np.sort(b, axis=0))
print("\n")


a = np.arange(6).reshape(2,3) + 10
print("The numpy array is \n")
print(a)
print("\n")

print("****** np.mean Usage ******\n")
print("The mean of the flattened version of array is \n")
print(np.mean(a))
print("\n")

print("The mean of each individual column is  \n")
print(np.mean(a, axis=0))
print("\n")

print("The mean of each individual row is \n")
print(np.mean(a, axis=1))
print("\n")



print("****** np.std Usage ******\n")

print("The standard deviation of the flattened version of array is \n")
print(np.std(a))
print("\n")

print("The standard deviation of each individual column is  \n")
print(np.std(a, axis=0))
print("\n")

print("The standard deviation of each individual row is \n")
print(np.std(a, axis=1))
print("\n")



print("****** np.var Usage ******\n")

print("The variance of the flattened version of array is \n")
print(np.var(a))
print("\n")

print("The variance of each individual column is  \n")
print(np.var(a, axis=0))
print("\n")

print("The variance of each individual row is \n")
print(np.var(a, axis=1))
print("\n")

