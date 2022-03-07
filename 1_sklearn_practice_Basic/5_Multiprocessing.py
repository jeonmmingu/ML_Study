# 모델을 병렬적으로 수행 가능 하도록 함
import multiprocessing
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import pandas as pd

# 데이터 지정
iris = load_iris()

# 1. parameter 지정
# l1, l2 : 정규화 방법 (l1 : Lasso Regression, l2 : Ridge Regression)
# Lidge Regression : Loss Function 의 penalty 항으로 계수의 "제곱 크기"를 추가함
# Lasso Regression : Loss Function 의 penalty 항으로 계수의 "크기의 절대 값"을 추가함
# C : Create regularization hyperparameter space
# https://chrisalbon.com/code/machine_learning/model_selection/hyperparameter_tuning_using_grid_search/ (각 인자 별 의미 확인 관련 주소)
# https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c (penalty 관련 내용 확인 주소)
param_grid = [{'penalty': ['l1', 'l2'], 'C': [1.5, 2.0, 2.4, 2.5, 3.0, 3.5]}]

# 2. 모델 설정
# multiprocessing.cpu_count() : cpu 개수에 맞게 multiprocessing을 진행
# n_jobs=multiprocessing.cpu_count() 이런 식으로 명령을 주면 된다.
gs = GridSearchCV(estimator=LogisticRegression(), param_grid=param_grid,
                  scoring='accuracy', cv=10, n_jobs=multiprocessing.cpu_count())

# 3. 모델 훈련
result = gs.fit(iris.data, iris.target)

# 4. 결과 확인
print("최적 점수: {}".format(result.best_score_))
print("최적 파라미터: {}".format(result.best_params_))
print(gs.best_estimator_)
df = pd.DataFrame(result.cv_results_)
print(df)
