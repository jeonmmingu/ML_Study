# Numpy에서 차원이 맞지 않는 배열끼리의 연산을 가능하도록 해주는 기능이다.
# 예를 들어, 2차원 배열에 스칼라 값이나 1차원 배열을 연산하는 것 등이 존재한다.
import numpy as np

A = np.arange(9.).reshape(3,3)   # 2d array : (3,3)
x = np.array([1.,0,0])   # 1d array : (3,)
y = x.reshape(1,3)       # 2d array : (1,3)
z = x.reshape(3,1)       # 2d array : (3,1)

# ex1. scalar addition
print(A)
print(A + 1)


# ex2. Extension of Matrix
# 만약 차원이 맞지 않는다면 작은 차원을 확장하여 계산하는 브로드캐스팅 방식을 취하게 된다.
# 확장 방식은 기존 행 또는 열을 그대로 복사하는 방식을 사용한다.
print(A + x)
print(A + y)
print(A + z)


# ex3. y + z (double extension)
print(y + z)


# ex4. warning to use Broadcasting
print(A @ z) # (3, 3)*(3, 1) -> (3, 1)
print(A @ x) # (3, 3)* 1차원 행렬 -> (3, 1)과 같은 취급을 하지만 결과 값은 (3, )값을 돌려준다.
print(A @ y) # (3, 3)*(1, 3)차원이 맞지 않아 오류 발생
