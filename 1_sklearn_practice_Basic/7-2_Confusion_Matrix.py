# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 오차 행렬 : 예측 값과 실제 값이 잘 맞는지 확인 할 수 있는 행렬
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 가상 분류 군 생성
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 모델 선정
model = LogisticRegression(solver='lbfgs', multi_class='auto', C=100.0)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 데이터 전처리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 모델 훈련
model.fit(X_train, y_train)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 학습 된 모델 예측 및 평가
predict = model.predict(X_test)
print("정확도: {}".format(accuracy_score(y_test, predict)))


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# 오차 행렬 (Confustion_Matrix)
#   - True Negative(TN): 예측 값을 Negative 값 0으로 예측 했고, 실제 값도 Negative 값 0
#   - False Positive(FP): 에측 값을 Positive 값 1로 예측 했는데, 실제 값은 Negative 값 0
#   - False Negative(FN): 예측 값을 Negative 값 0으로 예측 했는데, 실제 값은 Positive 값 1
#   - True Positive(TP): 예측 값을 Positive 값 1로 예측 했는데, 실제 값도 Positive 값 1
#   - 실제값 동일성 + 참/거짓

from sklearn.metrics import confusion_matrix

confmat = confusion_matrix(y_true=y_test, y_pred=predict)
print(confmat)

# https://codetorial.net/matplotlib/subplot.html (subplots 관련 페이지)
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')

plt.xlabel('Predicted label')
plt.ylabel('Ture label')
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #