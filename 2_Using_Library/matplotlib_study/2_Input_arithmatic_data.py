import matplotlib.pyplot as plt

# [1] Basic usage
# X축 데이터는 기본적으로 [0, 1, 2, 3]로 설정 되어 보여짐
plt.plot([2, 3, 5, 10])
plt.show()


# [2] X-Y input
plt.plot([2, 3, 4, 5], [2, 3, 5, 10])
plt.show()


# [3] Using Label
data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [2, 3, 5, 10, 8]}
plt.plot('data_x', 'data_y', data=data_dict)
plt.show()
