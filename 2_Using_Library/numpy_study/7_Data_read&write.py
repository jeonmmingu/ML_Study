# Numpy Library에서 지원하는 데이터를 읽고 쓰는 방법이다.
import numpy as np

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ex1. Basic usage
x = np.arange(9).reshape(3,3)
print(x)
np.savetxt('3by3.txt',x)
y = np.loadtxt('3by3.txt')
print(y)

# ex2. When we use 1 demension vector
# n*1 or 1*n 벡터의 경우 전부 다 1차원 벡터의 형태로 취급 받는 점에 주의!
x1 = np.array([1.1,2.2,3.1])
np.savetxt('x1.txt',x1)

x2 = np.array([1.1,2.2,3.1]).reshape(1,3)
np.savetxt('x2.txt',x2)

x3 = np.array([1.1,2.2,3.1]).reshape(3,1)
np.savetxt('x3.txt',x3)

y1 = np.loadtxt('x1.txt')  # array([1.1, 2.2, 3.1])
y2 = np.loadtxt('x1.txt')  # array([1.1, 2.2, 3.1])
y3 = np.loadtxt('x1.txt')  # array([1.1, 2.2, 3.1])
# 셋 다 동일한 1차원 벡터 형태로 출력되는 것을 확인 할 수 있다.
print(y1)
print(y2)
print(y3)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #