# Grid(격자)설정
# 정확한 값을 확인하기 위해 Grid 설정 가능
# plt.grid(), grid style method를 사용하여 설정 가능
import matplotlib.pyplot as plt
import numpy as np

# [1] Basic usage
# 0 ~ 1.8 까지 0.2 단위로 존재
# plt.grid() method를 True 설정하여 그리드를 지정한다.
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.grid(True)
# plt.show()


# [2] Apply on one axis
# plt.grid() method에 파라미터로 설정하면 된다.
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
plt.grid(True, axis='y')
# plt.show()


# [3] Set grid style
x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
# color/ alpha: 선의 투명도/ linestyle 인자 존재
plt.grid(True, axis='y', color='red', alpha=0.5, linestyle='--')
plt.show()
