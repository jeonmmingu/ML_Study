# Ndarray란?
# 해당 패키지의 핵심이 되는 객체이다.
# Fixed-size homogeneous multidimensional array 정도로 이해할 수 있으며, 기본적으로 vectorization과 broadcasting을 지원한다.
# 파이썬에서 제공하는 list, tuple등의 시퀀스 자료형과는 다르게 같은 데이터타입만을 요소로 가질 수 있고, 크기 역시 고정 되어 있다.
# 만약 크기를 변경하면 새로 메모리에 값이 할당되고 이전 값은 삭제되는 방식으로 이루어진다.
import numpy as np

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [1] Basic usage
# 1차원 배열 형태
x = np.array((0.1,0.2,0.3))
# print(x)
# print(x.shape)
# print(x.dtype)

# 2차원 배열 형태
y = np.array(((1, 2, 3), (4, 5, 6)))
# print(y)
# print(y.shape)
# print(y.dtype)

# << ndarray의 중요 속성 >>
# shape : 배열의 형태
# dtype : 요소의 데이터 타입
# ndim : 차원 수
# size : 요소의 개수. shape 결과 값들의 곱과 같음
# itemsize : 요소 데이터 타입의 크기


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [2] Initialization method
# Make 3x3 blank array
# ex1. make specific array
Y = np.zeros((3, 3))
print(Y)
Y = np.ones((3, 3), dtype='int32')
print(Y)
Z = np.empty((3, 3))
print(Z)

# ex2. when we need to add values repeatedly
A = np.array([],dtype='int32')
for i in range(3):
  A = np.append(A, [1, 2, 3])
print(A)
# 단순한 시퀀스는 range() 함수의 실수버전인 arange(from,to,step)이나 linspace(from,to,npoints)를 사용하면 편리하다. 또한 단위행렬을 위한 eye(n) 함수를 제공한다.
# 1부터 2까지 2를 포함하지 않고 0.1 단위로 배열 생성
print(np.arange(1, 2, 0.1)) 
# 0부터 1단위로 인자만큼 배열 생성
print(np.arange(10))
# float 단위로 배열 생성
print(np.arange(10.))
# 0부터 20까지 같은 간격으로 11개 인자로 배열 생성
print(np.linspace(0., 20., 11))
# 인자 x 인자 단위 행렬 생성
print(np.eye(3))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [3] Change Dtype and Shape
# ex1. Change shape
# reshape() method를 사용해서 Shape을 변경
X = np.arange(0, 9, 1.)
Y = np.reshape(X, (3, 3))
print("X: {}".format(X))
print("Y: {}".format(Y))

# ex2. Change Dtype
a = np.arange(3.)
print("a: {}, Dtype: {}, Shape: {}".format(a, a.dtype, a.shape))
a_int = a.astype(int)
print("a: {}, Dtype: {}, Shape: {}".format(a_int, a_int.dtype, a_int.shape))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #