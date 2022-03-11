# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# preprocessing 데이터 전처리 모듈
#   - 데이터의 특징 스케일링(feature scaling)을 위한 방법으로 표준화(Standardization)와 정규화(Normalization)을 사용
#   - 표준화(Standardization) 방법 :  x.i' = x.i - mean(x)/ stdev(x)
#   - 정규화(Normalization) 방법 :  x.i' = x.i - min(x)/ max(x) - min(x) -> minmax scaling (0, 1 사이의 값들로 데이터 값을 변환)
#   * x.i' : 처리된 결과 값을 의미한다.
#   - scikit-learn 에서는 개별 벡터 크기를 맞추는 형태로 정규화


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 1. StandardScaler : 표준화 클래스
from sklearn.preprocessing import StandardScaler
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(iris_df.describe())

scaler = StandardScaler()
# fit method를 통해 표준화에 필요한 데이터를 가져옴 -> transform을 통해 표준화 과정을 거친다. -> 둘을 합쳐서 fit_transform method
iris_scaled = scaler.fit_transform(iris_df)
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)
print(iris_df_scaled.describe())

model = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(iris_df_scaled, iris.target, test_size=0.3)

model.fit(X_train, y_train)

print("훈련 데이터 점수: {}".format(model.score(X_train, y_train)))
print("평가 데이터 점수: {}".format(model.score(X_test, y_test)))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 2.MinMaxScaler: 정규화 클래스
from sklearn.preprocessing import MinMaxScaler
# fit method를 통해 정규화에 필요한 데이터를 가져옴 -> transform을 통해 정규화 과정을 거친다. -> 둘을 합쳐서 fit_transform method
scaler = MinMaxScaler()
iris_scaled = scaler.fit_transform(iris_df)
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)
print(iris_df_scaled.describe())

model = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(iris_df_scaled, iris.target, test_size=0.3)

model.fit(X_train, y_train)

print("훈련 데이터 점수: {}".format(model.score(X_train, y_train)))
print("평가 데이터 점수: {}".format(model.score(X_test, y_test)))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 3. 데이터 전처리를 하지 않은 모델
# fit method를 통해 정규화에 필요한 데이터를 가져옴 -> transform을 통해 정규화 과정을 거친다. -> 둘을 합쳐서 fit_transform method

model = LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

model.fit(X_train, y_train)

print("훈련 데이터 점수: {}".format(model.score(X_train, y_train)))
print("평가 데이터 점수: {}".format(model.score(X_test, y_test)))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #