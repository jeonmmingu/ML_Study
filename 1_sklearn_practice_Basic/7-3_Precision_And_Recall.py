import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import numpy as np

# 가상 분류군 생성
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2,
                           n_redundant=0, n_clusters_per_class=1)

# 모델 설정 후 학습
model = LogisticRegression(solver='lbfgs', multi_class='auto', C=100.0)

# 데이터 처리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 모델 학습
model.fit(X_train, y_train)

# 학습 된 모델 예측 및 평가
predict = model.predict(X_test)
print("정확도: {}".format(accuracy_score(y_test, predict)))

# 오차 행렬로 모델 평가
confmat = confusion_matrix(y_true=y_test, y_pred=predict)
print(confmat)

fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')

# plt.xlabel('Predicted label')
# plt.ylabel('Ture label')
# plt.tight_layout()
# plt.show()


# 정밀도(Precision)와 재현율(Recall)
#   - 정밀도 = TP/(FP + TP)                  : 모델이 True라고 분류한 것 중에서 실제 True인 것의 비율
#   - 재현율 = TP/(FN + TP)                  : 실제로 True인 것 중에서 모델이 True라고 예측한 것의 비율
#   - 정확도 = (TN + TP)/(TN + FP + FN + TP) : 전체에서 실제 값이 True인 모든 경우
#   - 오류율 = (FN + FP)/(TN + FP + FN + TP) : 전체에서 실제 값이 False인 모든 경우
from sklearn.metrics import precision_score, recall_score

precision = precision_score(y_test, predict)
recall = recall_score(y_test, predict)

print("정밀도: {}".format(precision))
print("재현율: {}".format(recall))


# F1-Score(F-measure)
#   - 정밀도와 재현율을 결합한 지표
#   - 정밀도와 재현율이 어느 한쪽으로 치우치지 않을 때 높은 값을 가짐
#   - F1 = 2 * (precision x Recall) / (precision + Recall)
from sklearn.metrics import f1_score

f1 = f1_score(y_test, predict)
print("F1 score: {}".format(f1))


# ROC 곡선과 AUC
#   - ROC 곡선은 FPR(False Positive Rate)이 변할 때 TPR(True Positive Rate)이 어떻게 변하는지 나타내는 곡선이다.
#       1) TPR(Ture Positive Rate): TP/(FN + TP), 재현율
#       2) TNR(True Negative Rate): TN/(FP + TN)
#       3) FPR(False Positive Rate): FP/(FP + TN), 1-TNR
#   - AUC(Area Under Curve) 값은 ROC곡선 밑에 면적을 구한 값 (1이 가까울 수록 좋은 값)
from sklearn.metrics import roc_curve

# class가 1인 값에 대해 확률 값을 계산
pred_proba_class1 = model.predict_proba(X_test)[:, 1]
fprs, tprs, thresholds = roc_curve(y_test, pred_proba_class1)

plt.plot(fprs, tprs, label='ROC')
plt.plot([0, 1], [0, 1], '--k', label='Random')
start, end = plt.xlim()
plt.xticks(np.round(np.arange(start, end, 0.1), 2))
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('FPR(1-Sensitivity[TNR])')
plt.ylabel('TPR(Recall)')
plt.show()

# 또는
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_test, predict)

print("ROC AUC Score: {}".format(roc_auc))
