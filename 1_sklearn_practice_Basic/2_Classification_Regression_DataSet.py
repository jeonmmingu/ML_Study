# 내장된 Data Set
#   1) datasets.load_boston()     : 미국 보스턴의 집에 대한 특징과 과거 데이터 (회귀용)
#   2) datasets.load_cancer()     : 위스콘신 유방암 특징들과 악성/음성 레이블 데이터 (분류용)
#   3) datasets.load-diabetes()   : 당뇨 데이터 (회귀용)
#   4) datasets.load_digits()     : 0에서 9까지 숫자 이미지 픽셀 데이터 (분류용)
#   5) datasets.load_iris()       : 붓꽃에 대한 특징을 가진 데이터 (분류용)

# 온라인 Data Set
#   Data Set의 크기가 너무 커서 fetch 하는 방법으로 제공하고 있다.
#   1) fetch_california_housing() : 캘리포니아 주택 가격 데이터
#   2) fetch_covtype()            : 회귀 분석용 토지 조사 데이터
#   3) fetch_20newsgroups()       : 뉴스 그룹 텍스트 데이터
#   4) fetch_olivetti_faces()     : 얼굴 이미지 데이터
#   5) fetch_lfw_people()         : 얼굴 이미지 데이터
#   6) fetch_lfw_paris()          : 얼굴 이미지 데이터
#   7) fetch_rcv1()               : 로이터 뉴스 말뭉치 데이터
#   8) fetch_mldata()             : ML 웹 사이트에서 실제 데이터를 다운로드 받을 수 있음

# 분류와 클러스터링을 위한 표본 데이터 생성 도구
#   1) datasets.make_classifications() : 분류를 위한 데이터 세트 생성. 높은 상관도, 불필요한 속성등의 노이즈를 고려한 데이터를 무작위 생성
#   2) datasets.make_blobs()           : 클러스터링을 위한 데이터 세트 생성. 군집 지정 개수에 따라 여러 가지 클러스터링을 위한 데이터 셋트를 무작위로 생성

# 예제 데이터 세트 구조
#   1) 일반적으로 딕셔너리 형태로 구성
#   2) data: 특징 데이터 세트
#   3) target: 분류용은 레이블 값, 회귀용은 숫자 결과값 데이터
#   4) target_names: 특징 이름
#   5) DESCR(description): 데이터 세트에 대한 설명과 각 특징 설명

from sklearn.datasets import load_diabetes

# API call
diabetes = load_diabetes()
# print(diabetes.keys())
# Result : dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# print(diabetes.DESCR) -> 해당 데이터의 개요를 보고 싶을 때 먼저 검색
# print(diabetes.data) -> feature datas
# print(diabetes.target) -> diabetes related data
# print(diabetes.feature_names)
# print(diabetes.data_filename)
# print(diabetes.target_filename)
# print(diabetes.data_module)