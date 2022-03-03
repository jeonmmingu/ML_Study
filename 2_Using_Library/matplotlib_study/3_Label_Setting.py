# matplotlib.pyplot 모듈의 xlabel(), ylabel() 함수를 사용하여 x, y축에 대한 Label을 표시
import matplotlib.pyplot as plt

# [1] Basic usage
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# X축 이름 설정
plt.xlabel('X-Label')
# Y축 이름 설정
plt.ylabel('Y-Label')
plt.show()


# [2] Set label-pad
# Padding: 여백 / 축에 표시 되는 설정 값들 사이에 여백 설정
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15)
plt.ylabel('Y-Axis', labelpad=20)
plt.show()


# [3] Set font
# 폰트 설정

# ex1) Basic setting
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15, fontdict={'family': 'serif', 'color': 'b',
                                            'weight': 'bold', 'size': 14})
plt.ylabel('Y-Axis', labelpad=20, fontdict={'family': 'fantasy', 'color': 'deeppink',
                                            'weight': 'normal', 'size': 'xx-large'})

# ex2) Using font parameters
font1 = {'family': 'serif',
         'color': 'b',
         'weight': 'bold',
         'size': 14
         }
font2 = {'family': 'fantasy',
         'color': 'deeppink',
         'weight': 'normal',
         'size': 'xx-large'
         }
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15, fontdict=font1)
plt.ylabel('Y-Axis', labelpad=20, fontdict=font2)
plt.show()


# [4] Set Location
# xlabel : ({‘left’, ‘center’, ‘right’}) / ylabel : ({‘bottom’, ‘center’, ‘top’}) 설정 가능
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', loc='right')
plt.ylabel('Y-Axis', loc='top')
plt.show()
