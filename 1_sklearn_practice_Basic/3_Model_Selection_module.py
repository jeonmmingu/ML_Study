# model_selection module
#   - 학습용 데이터와 테스트 데이터로 분리
#   - 교차 검증 분할 및 평가
#   - Estimator의 하이퍼 파라미터 튜닝을 위한 다양한 함수와 클래스 제공

# train_test_split() : 학습/테스트 데이터 세트 분리
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

# 1. 모델 지정
model = LinearRegression()

# 2. 데이터를 특징 벡터와 대상 벡터로 배치
# ML에서는 데이터가 여러가지인 경우 대문자(ex.X)로 표기하고, 데이터가 하나인 경우는 소문자(ex.y)로 표기함.
# test_size => test data의 비율을 정함. (ex.test_size=0.3 이면 train_data의 비율이 70%가 됨)
# y_train, y_test data는 데이터 간의 순서가 없기 때문에 무작위로 출력된다.
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.3)

# 3. 모델 학습
model.fit(X_train, y_train)

# model_score는 1에 가까울 수록 좋은 점수이다.
# 실제로 모델을 실행해 보면 굉장히 성능이 낮게 나옴 -> 모델을 다른 것으로 바꾸던지 데이터를 전처리 하는 방식으로 개선 가능
print("학습 데이터 점수: {}".format(model.score(X_train, y_train)))
print("평가 데이터 점수: {}".format(model.score(X_test, y_test)))

import matplotlib.pyplot as plt

# 4. test 데이터 셋으로 결과 값 예측 단계
predicted = model.predict(X_test)
expected = y_test

# 5. 예측 결과 값 시각화
plt.figure(figsize=(8, 4))
plt.scatter(expected, predicted)
plt.plot([30, 350], [30, 350], '--r')
plt.tight_layout()
plt.show()
