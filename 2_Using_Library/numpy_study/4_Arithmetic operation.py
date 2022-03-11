from math import sin
import numpy as np

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ex1. Add each array's elements
# 각각의 요소들이 더해지는 방식으로 연산이 이루어진다.
a = np.array([1,2,3,4])
b = np.array([4,5,6,7])
c = a + b
print("1. ",c)

# ex2. Various operations
print("2. ", a * b)
print("3. ", a ** 2)
print("4. ", 10 * np.sin(a))
# a = a * b 와 동일한 의미를 갖는다.
a *= b
print("5. ", a)

# ex3. matrix operation
# 행렬 곱 연산자는 dot(), matmul(), @ 세 개의 연산자를 사용하여 나타낼 수 있다.
# 전치 행렬을 사용해야 하는 경우에는 A.T 이런식으로 사용하거나 A.transpose() method를 이용하면 된다.
A = np.arange(9).reshape(3,3)         # (3,3)
B = np.arange(11,11+9).reshape(3,3)   # (3,3)

x = np.arange(3)                      # (3,)
y = np.arange(3).reshape(3,1)         # (3,1)
z = np.arange(3).reshape(1,3)         # (1,3)
#  C = A*B  ... same results
C1 = np.dot(A,B)
C2 = np.matmul(A,B)
C3 = A@B
print("1.", C1, C2, C3)
# A*x ... 2d*1d  ... same results
Ax1 = np.dot(A,x) # array([ 5, 14, 23])
Ax2 = np.matmul(A,x) 
Ax3 = A@x
print("2.", Ax1, Ax2, Ax3)
# A*y ... 2d*(2d,but 1d vector) ... same results
Ay1 = np.dot(A,y)     # array([[ 5],[14],[23]])
Ay2 = np.matmul(A,y)  
Ay3 = A@y
print("3.", Ay1, Ay2, Ay3) 
# A*z ... 2d*(2d, but 1d vector)  ... all dimension error
Az1 = np.dot(A,z.T)     # array([[ 5],[14],[23]])
Az2 = np.matmul(A,z.T)  
Az3 = A@z.T            
print("4.", Az1, Az2, Az3)
# left make (row vector), right make (column vector)
xy = x@y   # array([5])
print("5.", xy)

# ex4. Sort and Search
# 배열에서 찾는 것은 최소값 또는 최대값은 np.amin(x), np.amax(x)를 이용하면 된다. 
# 만약 최소값 또는 최대값이 있는 위치를 구하려면 np.argmin(x), np.argmax(x)를 사용한다. 
# np.sort(x)를, 정렬했을 때의 인덱스를 구하려면 np.argsort(x)를 사용하면 된다.
x = np.array([9.1,8.2,2.3,3,3,7.6,5.2])
print(x)
print(np.amin(x))
print(np.argmin(x))
print(np.sort(x))
# 두번째로 큰 값의 index를 찾는 방법
imax2 = np.argsort(x)[-2]
print(imax2)

# ex5. Binary Search
# 이미 정렬되어 있는 배열을 대상으로 탐색할 때는 이진탐색(binary search)를 사용하면 계산효율을 대폭 높일 수 있다.
# Numpy는 np.searchsorted(array,value,side='left')를 통해 이진탐색을 수행할 수 있다. 
# side 인자로는 'left'와 'right'가 가능하다. 
# side='left'는 array[i-1] < value <= array[i]이고, side='right'는 array[i-1] <= value < array[i]이다. 
# C언어의 upper_bound, lower_bound와 비슷한 의미로 사용되어진다.
# 결과 값으로 인덱스 값을 출력해준다.
x = np.array([0.,13.,26.,30.])
print(x)
print(-1,':',np.searchsorted(x,-1.),',',np.searchsorted(x,-1.,side='right'))
print( 0,':',np.searchsorted(x, 0.),',',np.searchsorted(x, 0.,side='right'))
print( 5,':',np.searchsorted(x, 5.),',',np.searchsorted(x, 5.,side='right'))
print(13,':',np.searchsorted(x,13.),',',np.searchsorted(x,13.,side='right'))
print(15,':',np.searchsorted(x,15.),',',np.searchsorted(x,15.,side='right'))
print(30,':',np.searchsorted(x,30.),',',np.searchsorted(x,30.,side='right'))
print(35,':',np.searchsorted(x,35.),',',np.searchsorted(x,35.,side='right'))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #