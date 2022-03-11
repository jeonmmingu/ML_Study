import numpy as np

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# Indexing
# ex1.Basic usage
a = np.array([1.2, -1.3, 2.2, 5.3, 3.7])
print("1.",a)
print("2.",a[0])
print("3.",a[0:3])
print("4.",a[-1])
print("5.",a[-2])
print("6.",a[0:1])

# ex2.Save index
a = np.array([1.2,-1.3,2.2,5.3,3.7])
idx = [0,3]
print(a[idx])


# ex3.Boolean array
# 부등식의 형태로 Ndarray를 사용하게 되면 결과 값을 Boolean shape으로 값을 전달해준다.
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a > 3)
print(a[a > 3])
# 요소들 중 0이 아닌 값들의 index들을 배열 형태로 돌려주는 함수이다.
print(np.nonzero(a))


# ex4.Concatenate arraies
# concatenate((A,B,...),axis=0), hstack((A,B,...)), vstack((A,B,...)) method 들을 이용하여 합칠 수 있다.
a = np.array([1, 2, 3, 4])
b = np.array([2.5, 4.5, 6. ])
print(np.concatenate((a, b), axis=0))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #