# Matplotlib 기본 사용
# 가장 많이 쓰이는 matplotlib.pyplot 모듈 위주로 공부

# pyplot란?
# 해당 모듈은 MATLAB과 비슷하게 명령어 스타일로 동작하는 함수의 모음이다.
# matplotlib.pyplot 모듈의 각각의 함수를 사용해서 간편하게 그래프를 만들고 변화를 줄 수 있다.
# 예를 들어, 그래프 영역을 만들고 선을 표현하는 등의 행위를 할 수 있다.

# pyplot 모듈 import
import matplotlib.pyplot as plt


# ex1) Basic graph drawing
# plot() method 는 입력 받은 리스트 값을 y축 값으로 받아들여 그래프를 생성한다.
# X축 데이터는 기본 값인 [0, 1, 2, 3]으로 입력되어 나타난다.
plt.plot([1, 2, 3, 4])
plt.show()


# ex2) X-Y input graph drawing
# 첫번째 입력 리스트가 X값, 두번째 입력 리스트가 Y값이다.
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


# ex3) Graph style setting
# Format string : 'ro' = red circle marker / 'r-' = red line / 'r--' = red dot line
# axis : 축 설정 함수 / axis method -> [xmin, xmax, ymin, ymax]
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
plt.axis([0, 6, 0, 20])
plt.show()


# ex4) Drawing multi-graph
# 일반적으로 matplotlib에서는 NumPy array를 사용함
# 리스트를 사용하여도 내부적으로 변환 되어 사용 되어진다.
import numpy as np
# 200ms 간격으로 균일하게 시간이 샘플링 됨 : [0, 5) -> 0.2 간격 으로 되어 있음
t = np.arange(0., 5., 0.2)
print(t)
# ** : 제곱 / 빨간 점선, 파란 사각형, 초록 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
