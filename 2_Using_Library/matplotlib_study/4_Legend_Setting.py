# Legend Setting: 범례 설정
# 범례: Graph 에서 해당 선이 어떤 걸 의미 하는지 표기 하는 걸 의미
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [1] Basic usage
# plot() method의 인자인 label을 설정해주고 legend() 함수를 호출함으로써 범례를 표시 할 수 있다.
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [2] Location Setting
# ex1) Basic using
# legend() method의 인자인 loc를 사용하여 설정
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc=(0.0, 0.0))
# plt.legend(loc=(0.5, 0.5))
plt.legend(loc=(1.0, 1.0))
plt.show()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ex2) Use string parameters
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='lower right')
plt.legend(loc='upper left')
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [3] column number setting
# ncol: number column(인자로 열 개수를 설정)
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='best')          # ncol = 1
plt.legend(loc='best', ncol=2)    # ncol = 2
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [4] Font size setting
# legend() method의 fontsize parameter로 설정
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='best')
plt.legend(loc='best', ncol=2, fontsize=14)
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [5] Frame setting
# 여기까진 굳이 할 필요 없음, 하지만 이쁘게 사용하고 싶으면 설정
# frameon : 테두리 설정 여부 / shadow: 그림자 설정 여부
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='best')
plt.legend(loc='best', ncol=2, fontsize=14, frameon=True, shadow=True)
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #