# 복사는 얕은 복사(Shallow Copy와 Deep Copy로 나눠진다.)
# Shallow Copy는 주소 값만 복사하여 값을 참조하는 것을 의미하고, Deep Copy는 새로운 메모리에 값을 저장하는 것을 의미한다.
# Shallow Copy의 경우 주소 값만 복사하는 것이기 때문에 참조하는 실제 값은 같다고 볼 수 있다.
# Numpy의 대입 연산은 Shallow Copy형식으로 동작한다.
import numpy as np

a = [1, 2, 3]
x = np.array(a)

# Shallow Copy
y = x
print(y)
y[0] = 10
print(x)
print(y is x)

# Deep Copy
z = x.copy()
print(z is x)

# 부분 행렬도 Shallow Copy 방식으로 동작한다.
# List의 slicing은 Deep Copy 방식으로 동작한다.
X = np.array([1, 2, 3])
y = x[0:2]
y[0] = 10
print(x)
print(y)
