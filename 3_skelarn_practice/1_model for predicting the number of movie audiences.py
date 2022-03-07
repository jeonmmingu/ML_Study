# model for predicting the number of movie audiences
# Base-line code
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

train = pd.read_csv('movies_train.csv')
test = pd.read_csv('movies_test.csv')

train.info()
train.head()
test.head()

# 데이터 전처리
# 결측치가 많은 데이터 제거
train = train.drop(['dir_prev_bfnum'],axis = 1)
test =  test.drop(['dir_prev_bfnum'],axis = 1)

# 감독명 : 너무 다양해서 제거
train = train.drop(['director'],axis = 1)
test = test.drop(['director'],axis = 1)

# 제목 : 의미가 없기 때문에 제거
train = train.drop(['title'],axis= 1)
test = test.drop(['title'],axis= 1)

train.distributor.value_counts()


# 상위 5개의 배급사를 제외하고 '기타'로처리
distributor_list = train.distributor.value_counts()[:5]
def func(distributor):
    if distributor in distributor_list:
        return distributor
    else:
        return '기타'

train['distributor'] = train['distributor'].apply(lambda x : func(x))
test['distributor'] = test['distributor'].apply(lambda x : func(x))

# 개봉일을 바탕으로 년,월 변수 생성
train['년'] = train['release_time'].apply(lambda x: int(x[:4]))
train['월'] = train['release_time'].apply(lambda x: int(x[5:7]))
train =  train.drop(['release_time'],axis = 1)

test['년'] = test['release_time'].apply(lambda x: int(x[:4]))
test['월'] = test['release_time'].apply(lambda x: int(x[5:7]))
test =  test.drop(['release_time'],axis = 1)

# 원핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 모델 정의 및 학습
train_x = train.drop(['box_off_num'],axis= 1)
train_y = train['box_off_num']

model=RandomForestRegressor(n_estimators=100)
model.fit(train_x,train_y)

# 학습 된 모델로 예측 데이터 생성
pred = model.predict(test)

# 제출 파일 생성
submission = pd.read_csv('/content/submission.csv')
submission['box_off_num'] = pred
submission.to_csv('베이스라인.csv',index = False)
