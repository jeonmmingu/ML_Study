# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 성능 평가 지표
# 정확도(Accuracy)
#   - 정확도는 전체 예측 데이터 건수 중 예측 결과가 동일한 데이터 건수로 계산
#   - 정확도는 데이터의 분포가 분산되어 있어도 높게 나올 수 있기 때문에 모델을 평가할 때 잘 도입해야하는 수치이다.
#   - scikit-learn에서는 accuracy_score 함수를 제공

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# n_featuers: 특징의 개수 / n_informative: 의미있는 feature의 개수/ n_redundant: 노이즈
# n_clusters_per_class: 하나의 클래스 당 군집체 개수
# make_classification() : sklearn에서 제공하는 가상 분류모형 패키지이다.
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 모델 지정
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html (Logistic Regression parameter)
model = LogisticRegression(solver='lbfgs', multi_class='auto', C=100.0)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 데이터 처리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 모델 학습
model.fit(X_train, y_train)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 결과 출력
print("훈련 데이터 점수: {}".format(model.score(X_train, y_train)))
print("평가 데이터 점수: {}".format(model.score(X_test, y_test)))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 모델 정확도 측정
predict = model.predict(X_test)
print("정확도: {}".format(accuracy_score(y_test, predict)))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #