# Axis Scale 설정(Default는 상수로 설정)
# plt.xscale(), plt.yscale(), axis scale, linear, log method를 이용해서 변환 가능
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [1] Set X axis scale setting
x = np.linspace(-10, 10, 100)
y = x ** 3
# xscale: Symmetrical Log Scale -> 대칭적인 로그 스케일로 설정
plt.plot(x, y)
plt.xscale('symlog')
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [2] Set Y axis scale setting
# exponent 함수로 y값이 설정 되어 log 스케일로 나오면 선형의 형태를 띈다.
# np.linspace -> np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# = start값부터 stop값까지 num개 만큼 수를 생성. endpoint는 마지막 값을 포함시킬것인지 설정.
x = np.linspace(0, 5, 100)
print(x)
y = np.exp(x)
# yscale: log -> 일반적인 로그 스케일로 설정
plt.plot(x, y)
# plt.yscale('linear')
plt.yscale('log')
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #