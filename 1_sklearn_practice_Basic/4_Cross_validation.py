# 교차검증 - ML에서 모델링을 위한 훈련용 및 시험용 데이터를 교차 변경하는 방법론
# cross_val_score() : 교차 검증
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

# Train Data와 Test Data를 분리
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.3)

# 모델 지정 및 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# cv: 교차 검증을 위해 몇 개로 나눌 것인지 정하는 인자
scores = cross_val_score(model, diabetes.data, diabetes.target, cv=5)

# np.mean = 평균, np.std = 표준 편차
print("교차 검증 정확도: {}".format(scores))
print("교차 검증 정확도: {} +/- {}".format(np.mean(scores), np.std(scores)))
#  Result : 교차 검증 정확도: [0.42955643 0.52259828 0.4826784  0.42650827 0.55024923]
#           교차 검증 정확도: 0.48231812211149394 +/- 0.049266197765632035
#           -> 정확도가 굉장히 저조한 것을 확인 할 수 있다.


# GridSearchCV: 교차 검증과 최적 하이퍼 파라미터를 찾는 모델을 만들어준다.
#       - 훈련 단계에서 학습한 파라미터에 영향을 받아서 최상의 파라미터를 찾는 일은 항상 어려운 문제이다.
#       - 다양한 모델의 훈련 과정을 자동화하고, 교차 검사를 사용해 최적 값을 제공하는 도구가 필요하다.
#       - 데이터가 적은 경우에는 유용하게 쓰이지만, 데이터가 너무 많아지게 되면 의미가 퇴색되기도 함
# Ridge : Linear model에서 알파 값을 조정하여 예측 가능하도록 함
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
import pandas as pd

# 10단위로 모델에 테스트를 진행
alpha = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
param_grid = dict(alpha=alpha)

# Cross validation 이 가능하도록 모델을 설정해준다.
gs = GridSearchCV(estimator=Ridge(), param_grid=param_grid, cv=10)
result = gs.fit(diabetes.data, diabetes.target)

# 결과 확인
print("최적 점수: {}".format(result.best_score_))
print("최적 파라미터: {}".format(result.best_params_))
print(gs.best_estimator_)
df = pd.DataFrame(result.cv_results_)
print(df)
