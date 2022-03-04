# Ndarray란?
# 해당 패키지의 핵심이 되는 객체이다.
# Fixed-size homogeneous multidimensional array 정도로 이해할 수 있으며, 기본적으로 vectorization과 broadcasting을 지원한다.
# 파이썬에서 제공하는 list, tuple등의 시퀀스 자료형과는 다르게 같은 데이터타입만을 요소로 가질 수 있고, 크기 역시 고정 되어 있다.
# 만약 크기를 변경하면 새로 메모리에 값이 할당되고 이전 값은 삭제되는 방식으로 이루어진다.
import numpy as np
x = np.array((0.1,0.2,0.3))
print(x)
