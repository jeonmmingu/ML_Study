# 그래프 영역 채우기
# plt.fill_between(), plt.fill_betweenx(), plt.fill() method를 사용하여 표시
import matplotlib.pyplot as plt


# [1] Basic usage
# y축 기준
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.fill_between(x[1:3], y[1:3], alpha=0.5)
plt.show()

# x축 기준
x = [1, 2, 3, 4]
y = [2, 3, 5, 10]

plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# y와 x의 위치를 바꿔서 사용
plt.fill_betweenx(y[2:4], x[2:4], alpha=0.5)
plt.show()


# [2] Fill graph area between two graph
# 해당 축의 scale을 2개 설정하면 된다.
x = [1, 2, 3, 4]
y1 = [2, 3, 5, 10]
y2 = [1, 2, 4, 8]

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.fill_between(x[1:3], y1[1:3], y2[1:3], color='lightgray', alpha=0.5)
plt.show()
