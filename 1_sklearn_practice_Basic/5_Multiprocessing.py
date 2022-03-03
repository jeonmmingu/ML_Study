# 모델을 병렬적으로 수행 가능
import multiprocessing
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import pandas as pd

iris = load_iris()

# 패널티와 C값이 뭔지 확인
param_grid = [{'penalty': ['l1', 'l2'], 'C': [1.5, 2.0, 2.4, 2.5, 3.0, 3.5]}]

# 설정하는 인자들에 대한 것들도 확인
gs = GridSearchCV(estimator=LogisticRegression(), param_grid=param_grid,
                  scoring='accuracy', cv=10, n_jobs=multiprocessing.cpu_count())

result = gs.fit(iris.data, iris.target)

# 결과 확인
print("최적 점수: {}".format(result.best_score_))
print("최적 파라미터: {}".format(result.best_params_))
print(gs.best_estimator_)
df = pd.DataFrame(result.cv_results_)
print(df)
