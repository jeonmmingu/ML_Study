# 판다스의 시리즈는 일차원 데이터를 관리하는 자료구조로, 데이터와 함께 인덱스라는 것을 사용해서 데이터에 레이블을 달 수 있도록 만든 자료 구조이다.
# 예를 들어 순서를 작성할 수도 있고, 아니면 작성 날짜를 달아둘 수도 있다.
from pandas import Series

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [1] Create Series

# Using List
data = [10, 20, 30]
s = Series(data)
print("[1]\n",s, "\n")

# Using Numpy
import numpy as np
data = np.arange(5)
s = Series(data)
print("[2]\n",s, "\n")

# String data
# String data는 object로 관리가 된다.
data = ["시가", "고가"]
s = Series(data)
print("[3]\n", s, "\n")

# Mixed data type
# string data와 integar data등 이질적인 두 데이터를 한번에 저장하면 object 타입으로 관리되어 Broadcasting등 유용한 기능의 지원이 안될 수 있기 때문에 혼용하지 않는 편이 좋다.
data = ["Samsung", 81000]
s = Series(data)
print("[4]\n", s, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [2] Index

# See Indexing Information
data = [1000, 2000, 3000]
s = Series(data)
print("[5]\n", s.index, "\n")
print("[6]\n", s.index.to_list(), "\n")

# Decide Indexes
s.index = ["메로나", "구구콘", "하겐다즈"]
print("[7]\n", s, "\n")

# Reindex
s2 = s.reindex(["메로나", "비비빅", "하겐다즈"])
print("[8]\n", s2, "\n")

# remove isna
print("[9]\n", s2.fillna(0), "\n")
# or
s3 = s.reindex(["메로나", "비비빅", "구구콘"], fill_value=0)
print(s3, "\n")

# Example 1
# 날짜별 주가 정보 데이터 저장
price = [42500, 42550, 41800, 42550, 42650]
date = ["2019-05-31", "2019-05-30", "2019-05-29", "2019-05-28", "2019-05-27"]
s = Series(price, date)
print("[10]\n", s, "\n")

# or
# Dictionary 를 사용하면 key : index / Value: series data 로 받아들여진다.
data = {
    "2019-05-31" : 42500,
    "2019-05-30" : 42550,
    "2019-05-29" : 41800,
    "2019-05-28" : 42550,
    "2019-05-27" : 42650
}
s = Series(data)
print("[11]\n", s, "\n")
# index : list
print(s.index)
# values : Ndarray
print(s.values)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [3] Indexing

# iloc : Column indexing -> value return
data = [1000, 2000, 3000]
s = Series(data=data)
print("[12]\n", s.iloc[0], "\n")

# loc : index value indexing -> value return
print("[13]\n", s.loc[1], "\n")

# Warning to use
# 기본적으로 [] 기호는 Series 객체 안에서 loc 매서드를 호출하도록 설정되어있다.
s1 = Series([10, 20, 30])
s2 = Series([10, 20, 30], index=[1, 2, 3])
print(s1[0], "\n")
# index가 존재하지 않으면 error occur
# print(s2[0]) 
# BUT
# Index가 integar data type이 아닌 경우 iloc 형태로 받아들이기 때문에 출력이 진행된다!!
s3 = Series([10, 20, 30], index=['a', 'b', 'c'])
print(s3[0], "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [4] Series Modify, Add, Drop values

# Modify data
data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)

s.loc['메로나'] = 500
print("[14]\n", s, "\n")
s.iloc[1] = 10000
print("[15]\n", s, "\n")

# Add data
# 이전에 존재하지 않았던 값이 들어오게 되면 새로운 값이 추가된다.
s.loc["비비빅"] = 350
print("[16]\n",s, "\n")

# Delete data
# drop() method는 해당 index값이 삭제된 객체를 반환함에 주의 해야한다.
# 즉, 원본 데이터는 지워지지 않는다.
s = s.drop(['메로나'])
print("[17]\n",s, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [5] Series calculate

# Baisc Add
# 데이터의 위치에 상관없이 index가 동일한 데이터 끼리 연산이 진행되는 것을 확인할 수 있다.
철수 = Series([10, 20, 30], index=['NAVER', 'SKT', 'KT'])
영희 = Series([10, 30, 20], index=['SKT', 'KT', 'NAVER'])
가족 = 철수 + 영희
print(가족, "\n")

# Scholar calculate
print(철수 * 10, "\n")

# Example 1. 삼성전자의 5일 일봉 데이터에서 고가와 저가 시리즈로 각 거래일의 변동폭 계산. [변동폭 :'고가'와 '저가'의 처분 값]
high = Series([42800, 42700, 42050, 42950, 43000])
low = Series([42150, 42150, 41300, 42150, 42350])
diff = high - low
print("[18] 변동폭(diff)\n", diff, "\n")
print("[19] 가장 큰 변동폭\n", diff.max(), "\n")
print("[20] 가장 작은 변동폭\n", diff.min(), "\n")

# Example 2. 변동폭이 가장 큰 날짜를 찾아보자
date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
high = Series([42800, 42700, 42050, 42950, 43000], index=date)
low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
diff = high - low
print("[21] 변동폭이 가장 큰 날짜\n", diff.idxmax(), "\n")

# Example 3. 매일 저가에 사서 고가에 팔았을 경우 수익률 계산
date = ["6/1", "6/2", "6/3", "6/4", "6/5"]
high = Series([42800, 42700, 42050, 42950, 43000], index=date)
low = Series([42150, 42150, 41300, 42150, 42350] , index=date)
profit = high / low
print("[22] 매일 저가에 사서 고가에 팔았을 때 수익률\n", profit, "\n")
# cumprod() : pandas에서 제공하는 누적 곲 계산 Method
# 해당 메서드는 다시 Series 객체를 돌려준다.
print("[23] 누적 수익률\n", profit.cumprod())
print("[24] 누적 수익률 중 마지막 값만 추출\n" , profit.index[-1] ,profit.cumprod( ).iloc[ -1 ] , "\n")

# Example 4. Data count
data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}
s = Series(data)
# 중복을 제거하고 업종명을 받아오기
# unique() method를 사용한다.
print("[25] 업종 리스트\n", s.unique(), "\n")
# 시리즈 안에 해당 index 데이터가 얼마나 있는지 계산
# value_counts() method를 사용한다.
print("[26] 업종 별 회사 개수\n", s.value_counts(), "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [6] Series & Map

# 기본 연산 이외의 복잡한 형태의 사용자 정의 코드를 적용하고 싶은 경우 Map method를 사용
# ex) 숫자가 문자열 타입으로 시리즈에 바인딩 되어있을 때, 이를 숫자로 변환하는 경우
# ex) 시리즈의 데이터가 특정 값보다 크거나 작은지 의문형으로 물어보는 경우

# Convert Type
s = Series(["1,234", "5,678", "9,876"])
# Error occur
# print( int(s) )
def remove_comma(x) :
  return int(x.replace(",", ""))

s = Series(["1,234", "5,678", "9,876"])
result = s.map(remove_comma)
print("[27] 시리즈 데이터의 콤마 제거\n", result, "\n")

# Make Categorical data
def is_greater_than_5000(x):
  if x > 5000:
    return "크다"
  else:
    return "작다"

s = Series([1234, 5678, 9876])
s = s.map(is_greater_than_5000)
print("[28] 시리즈 데이터가 5000보다 큰가?\n", s, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [7] Sorting and Ranking

# Sorting
# 시리즈 객체는 sort_values라는 자체 정렬 메서드를 가지고 있다.
# 해당 함수의 ascending 파라미터를 통해 오름차순과 내림차순을 정할 수 있다. (False : 내림차순 / True : 오름차순)

data = [3.1, 2.0, 10.1, 5.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
print("[28] 원본 데이터\n",s, "\n")
 
# 정렬 (오름차순)
s1 = s.sort_values()
print("[29] 오름차순 정렬\n",s1, "\n")

# 정렬 (내림차순)
s2 = s.sort_values(ascending=False)
print("[30] 내림차순 정렬\n",s2, "\n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [8] Sorting and Ranking

# Ranking
# 해당 메서드에서는 기본적으로 값이 작은 데이터를 1순위로 지정한다.

data = [3.1, 2.0, 10.1, 3.1]
index = ['000010', '000020', '000030', '000040']
s = Series(data=data, index=index)
# 같은 데이터 값을 갖는 값들에 대해 표현하기 순위를 매기기 위해 float64 형태로 출력된다.
print("[31] Rank 오름차순 출력\n",s.rank(), "\n")
print("[32] Rank 내림차순 출력\n",s.rank(ascending=False), "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #