from ntpath import join
from pandas import DataFrame
from pandas import Series
import pandas as pd
import numpy as np
from pyparsing import col

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [1] Query
# DataFrame에서 Boolean Equation을 사용하여 조건을 만든 후 이를 사용해 필터링하는 것 처럼 query 매서드를 사용하면
# 특정 조건에 부합하는 데이터를 쉽게 필터링 할 수 있다.
# Query는 값을 참조하여 데이터를 불러오는 method 이다.
data = [
    {"cd":"A060310", "nm":"3S", "open":2920, "close":2800},
    {"cd":"A095570", "nm":"AJ네트웍스", "open":1920, "close":1900},
    {"cd":"A006840", "nm":"AK홀딩스", "open":2020, "close":2010},
    {"cd":"A054620", "nm":"APS홀딩스", "open":3120, "close":3200}
]
df = DataFrame(data=data)
df = df.set_index('cd')
print("[1] Set index \n", df, "\n")

# 시가가 2000원 이상이라는 조건을 생성
# Use Boolean Equation
cond = df['open'] >= 2000
print("[2] Get data that open value is bigger than 2000 \n", df[cond], '\n')

# Use query() method
print("[3] Use query to filtering data 1 \n", df.query("nm=='3S'"), '\n')
print("[4] Use query to filtering data 2 \n", df.query('nm=="3S"'), '\n')
print("[5] Use query to filtering data 3 \n", df.query("open > close"), '\n')
# nm을 기준으로 필터링
print("[6] Use query to filtering data 4 \n", df.query("nm in ['3S', 'AK홀딩스']"), '\n')
# index를 기준으로 필터링
print("[7] Use query to filtering data 5 \n", df.query("cd == 'A060310'"), '\n')
# 쿼리 데이터를 넘겨주는 경우 @를 붙이면 파이썬 변수도 참조할 수 있다.
name = "AJ네트웍스"
print("[8] Use query to filtering data 6 \n", df.query('nm == @name'), '\n')


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [2] Filter
# Index나 column 이름에 대해 특정 조건으로 필터링이 가능하다.
data = [
    [1416, 1416, 2994, 1755],
    [6.42, 17.63, 21.09, 13.93],
    [1.10, 1.49, 2.06, 1.88]
]

columns = ["2018/12", "2019/12", "2020/12", "2021/12(E)"]
index = ["DPS", "PER", "PBR"]

df = DataFrame(data=data, index=index, columns=columns)

# Column에 대해 필터링을 진행
print("[9] Use filter.item() method to filtering data\n", df.filter(items=['2018/12']), '\n')
# 인덱스에 대해 필터링을 진행
print("[10] Filtering data by index\n", df.filter(items=["PER"], axis=0), '\n')
# regex 파라미터를 통해서 정규화된 조건을 사용할 수 있다.
print("[11] Filtering data by regex parameter 1\n", df.filter(regex="^2020"), '\n')
# regex 파라미터를 통해서 정규화된 조건을 사용할 수 있다.
print("[12] Filtering data by regex parameter 2\n", df.filter(regex="R$", axis=0), '\n')
# \d{num} : num만큼의 숫자가 연속해 등장하는 데이터 값들을 불러오라는 의미이다.
print("[13] Filtering data by regex parameter 3\n", df.filter(regex="\d{4}"), '\n')
# make complete regex
print("[14] Filtering data by regex parameter 3\n", df.filter(regex="\d{4}/\d{2}$"), '\n')  # 연속된 숫자 4개 + / + 연속된 숫자 2개


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [3] Sorting and Ranking
data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005670", "ACTS", 1185]
]

columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
df.set_index("종목코드", inplace=True)

# 데이터프레임 객체는 여러 개의 칼럼으로 구성되어 있기 때문에 시리즈와 달리 정렬 기준을 정해줘야 한다.
# '현재가'를 기준으로 잡고 정렬한 결과
# 'by='은 명시하지 않아도 상관없긴 하지만 parameter가 많은 경우에는 명시적으로 사용하는 것이 좋다.
df2 = df.sort_values(by="현재가")
print("[15] Sort DataFrame by '현재가' column\n", df2, '\n')

# 내림차순으로 정렬
df2 = df.sort_values(by="현재가", ascending=False)
print("[16] Sort DataFrame by '현재가' column in ascending order\n", df2, '\n')

# Set Rank
df['순위'] = df['현재가'].rank()
df = df.sort_values(by='순위')
print("[17] ADD rank column\n", df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [4] Calculate using index

idx1 = pd.Index([1, 2, 3])
idx2 = pd.Index([2, 3, 4])
print("[18] show index data type\n", type(idx1), "\n")

# 두 개의 인덱스를 합침
# 겹치는 부분은 한번만 표기됨
idx1 = idx1.union(idx2)
print("[19] Union two index\n",idx1, "\n")

# 두 개의 인덱스의 겹치는 인자들을 모아서 새로운 인덱스로 만듦
idx1 = idx1.intersection(idx2)
print("[20] InterSection two index\n",idx1, "\n")

# 현재 인덱스와 비교하는 인덱스 사이에 같은 인덱스 값들을 제거해주는 method이다.
idx1 = idx1.difference(idx2)
print("[21] Difference between two index set\n", idx1, "\n")

# example 1
data1 = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790]
]
data2 = [
   ["005670", "ACTS", 1185]
]
columns = ["종목코드", "종목명", "현재가"]

df1 = DataFrame(data=data1, columns=columns)
df2 = DataFrame(data=data2, columns=columns)

df1.set_index("종목코드", inplace=True)
df2.set_index("종목코드", inplace=True)

print("[22] Union two index set\n", df1.index.union(df2.index), "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [5] GroupBy method
# 데이터를 집계하는 method
data = [
    ["2차전지(생산)", "SK이노베이션", 10.19, 1.29],
    ["해운", "팬오션", 21.23, 0.95],
    ["시스템반도체", "티엘아이", 35.97, 1.12],
    ["해운", "HMM", 21.52, 3.20],
    ["시스템반도체", "아이에이", 37.32, 3.55],
    ["2차전지(생산)", "LG화학", 83.06, 3.75]
]

columns = ["테마", "종목명", "PER", "PBR"]
df = DataFrame(data=data, columns=columns)
# df.set_index("종목명", inplace=True)

# 직접 데이터를 분리한 후 평균 값을 계산하였다.
df1 = df[df['테마'] == "2차전지(생산)"]
print("[23] 2차전지(생산)에 관련된 테마만 집계한 데이터프레임\n", df1, "\n")
print("[24] 2차전지(생산)에 관련된 테마의 데이터 값들의 평균\n", df1['PER'].mean(), "\n")

# 이러한 작업들을 편리하게 groupy() method를 이용하여 처리할 수 있다.
# 전체 테마들에 대한 PER 값들의 평균을 계산한 값이 나오게 된다.
print("[25] groupby() method를 이용한 case\n", df.groupby("테마")["PER"].mean(), "\n")  # 테마 데이터 별로 묶은 후에 각 테마별 PER값들의 평균값을 구하라는 의미이다.

# 하나의 테마에 대해 분리 및 데이터 처리를 진행하는 방법
gb = df.groupby("테마")
# 테마중 하나의 테마 데이터들을 가져오라는 의미
temp = gb.get_group("2차전지(생산)")
print("[26] Calculate PER value that groupby for one theme\n", temp, "\n")

# 필요 컬럼만 고른 뒤 groupby를 진행
temp = df[["테마", "PER", "PBR"]].groupby("테마").get_group("2차전지(생산)")
print("[27] choose column that i want to see\n", temp, '\n')

# 먼저 테마로 그룹을 묶은 뒤 필요한 컬럼을 고른다음 원하는 테마를 선택
temp = df.groupby("테마")[ ["PER", "PBR"] ].get_group("2차전지(생산)")
print("[28] Choose theme to grouping and choose columns to use and split data by theme\n", temp, '\n')
print("[29] Add some calculate functions\n", df.groupby("테마")[["PER", "PBR"]].mean(), '\n')

# groupby method는 PER과 PBR외의 종목명 컬럼은 평균 연산을 수행할 수 없기 때문에 자동적으로 제거하고 데이터프레임을 반환하게 된다.
print("[30] Groupby() method's default setting\n", df.groupby("테마")[["PER", "PBR"]].mean(), '\n')
df.groupby("테마").mean()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [6] Concat (left/right side)
# 인덱스는 동일한데 컬럼이 다른 경우 concat() method를 이용하여 좌/우로 데이터를 붙여서 사용할 수 있다.

# //// 인덱스가 동일한 경우 ////

# 첫 번째 데이터프레임
data = {
    '종가':   [113000, 111500],
    '거래량': [555850, 282163]
}
index = ['2019-06-21', '2019-06-20']
df1 = DataFrame(data=data, index=index)

# 두 번째 데이터프레임
data = {
    '시가':   [112500, 110000],
    '고가':   [115000, 112000],
    '저가':   [111500, 109000]
}
index = ['2019-06-21', '2019-06-20']
df2 = DataFrame(data=data, index=index)

df = pd.concat([df1, df2], axis=1)
print("[30] Add two dataframe (Same index set)\n", df, '\n')

#  //// 인덱스가 다른 경우 ////
# 첫 번째 데이터프레임
data = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}
index = ["2019-06-21", "2019-06-20"]
df1 = DataFrame(data=data, index=index)

# 두 번째 데이터프레임
data = {
    '시가': [112500, 110000],
    '고가': [115000, 112000],
    '저가': [111500, 109000]
}
index = ["2019-06-20", "2019-06-19"]
df2 = DataFrame(data=data, index=index)

# 데이터프레임 합치기
df = pd.concat([df1, df2], axis=1)
print("[31] Add two dataframe (Different index set)\n", df, '\n')

# concat의 join parameter => outer : 합집합 (결측치를 nan으로 표기하고 모든 값을 다 나타냄) / inner : 교집합 (인덱스에 결측치가 존재하면 표시하지 않고 제거)
df = pd.concat([df1, df2], axis=1, join='inner')
print("[32] Inner joining add two dataframe\n", df, '\n')


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [7] Concat (up/down side)
# column별로 데이터프레임을 정렬한 후 두개의 데이터 프레임을 합치는 방법이다.
# append() method를 또는 concat() method를 이용하여 두 개의 데이터프레임을 합친다.
# append() : dataframe의 method // concat() : pandas의 method

# 첫 번째 데이터프레임
data = {
    '종가': [113000, 111500],
    '거래량': [555850, 282163]
}
index = ["2019-06-21", "2019-06-20"]
df1 = DataFrame(data, index=index)

# 두 번째 데이터프레임
data = {
    '거래량': [110000, 483689],
    '시가': [109000, 791946]
}
index = ["2019-06-19", "2019-06-18"]
df2 = DataFrame(data, index=index)

df = df1.append(df2)
print("[33] Union two different dataframe\n", df, "\n")

# append()외에 concat() method도 사용가능하다.
df = pd.concat([df1, df2], axis=0, join='inner')
print("[34] Union two different dataframe to use concat() method\n", df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [8] Merge
# concat과는 다르게 특정 칼럼의 값을 기준으로 데이터를 병합한다.

# 첫 번째 데이터프레임
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["전기전자", "000660", "SK하이닉스", 101500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["업종", "등락률"]
df2 = DataFrame(data=data, columns=columns)

# 병합의 기준을 "업종"으로 설정하여 merge를 진행한다.
# 업종을 기준으로 겹치는 것들에 대해 병합을 실행한다.
df = pd.merge(left=df1, right=df2, on='업종')
print("[35] merge하여 두 개의 데이터프레임을 병합\n", df, '\n')


# //// Use how parameter ////
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "035720", "카카오", 121500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["업종", "등락률"]
df2 = DataFrame(data=data, columns=columns)

# left 옵션에 의해 left 파라미터에 입력된 데이터프레임 df1을 기준으로 두 데이터프레임을 병합한다.
# 기존 merge와는 다르게 기준이 되는 데이터에 맞는 값들만 병합을 진행하고, 만약 기준이 되는 데이터에 맞는 값이 존재하지 않으면 결측값으로 출력한다.
df = pd.merge(left=df1, right=df2, how='left', on='업종')
print("[36] Option을 설정 후 merge하여 두 개의 데이터프레임을 병합\n", df, '\n')


# //// 두 데이터 프레임의 칼럼 값이 모두 다른 경우 ////

# 첫 번째 데이터프레임
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "035720", "카카오", 121500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data, columns=columns)

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["항목", "등락률"]
df2 = DataFrame(data=data, columns=columns)

# 각 데이터 프레임의 기준이 되는 칼럼을 모두 지정해줘야 한다.
df = pd.merge(left=df1, right=df2, left_on='업종', right_on='항목')
print("[37] 두 개의 데이터 프레임의 칼럼이 모두 다른 경우\n", df, '\n')


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [9] Join
# 데이터프레임의 join매서드는 판다스의 merge와 유사하지만, 데이터프레임의 인덱스 기준으로 병합하는 경우에는 join을 사용한다.

# 첫 번째 데이터프레임
data = [
    ["전기전자", "005930", "삼성전자", 74400],
    ["화학", "051910", "LG화학", 896000],
    ["서비스업", "035720", "카카오", 121500]
]

columns = ["업종", "종목코드", "종목명", "현재가"]
df1 = DataFrame(data=data, columns=columns)
df1 = df1.set_index("업종")

# 두 번째 데이터프레임
data = [
    ["은행", 2.92],
    ["보험", 0.37],
    ["화학", 0.06],
    ["전기전자", -2.43]
]

columns = ["항목", "등락률"]
df2 = DataFrame(data=data, columns=columns)
df2 = df2.set_index("항목")


print("[38-1] dataframe 1\n", df1, "\n")
print("[38-2] dataframe 2\n", df2, '\n')

# 각 데이터프레임에 대하여 reset_index() method를 사용해도 되지만, join method를 사용하므로써 코드 사이즈를 단축할 수 있다.
df1.join(other=df2)
print("[38-3] join two dataframe\n", df1, "\n")


# example. 시가총액을 사용해서 대형주와 중/소형주로 구분하는 예제

# 연도별로 회사와 시가총액이 저장된 데이터프레임을 생성한다.
data = [
    ["2017", "삼성", 500],
    ["2017", "LG", 300],    
    ["2017", "SK하이닉스", 200],
    ["2018", "삼성", 600],
    ["2018", "LG", 400],
    ["2018", "SK하이닉스", 300],    
]

columns = ["연도", "회사", "시가총액"]
df = DataFrame(data=data, columns=columns)
print("[39] Dataframe\n", df, "\n")

df_mean = df.groupby("연도")["시가총액"].mean().to_frame()
df_mean.columns = ['시가총액평균']
print("[40] 시가총액평균\n", df_mean, "\n")

df = df.join(df_mean, on='연도')
print("[41] Join two dataframe\n", df, "\n")

# np.where() : 행 단위로 조건을 나타낼 때 쓰는 method 이다.
# 시가총액이 시가총액평균보다 큰 경우를 대형주 그렇지 않은 경우를 중/소형주로 구분
df['규모'] = np.where(df['시가총액'] >= df['시가총액평균'], "대형주", "중/소형주")
print("[42] Make new column with np.where() method\n", df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [9] Multi-index
# 엑셀에서는 셀(cell)을 병합하는 형태로 여러 컬럼으로 구분된 구조적인 데이터를 표현할 수 있다.
# DataFrame 상에서 이렇게 표현하는 방법이 Multi-index이다.

data = [
    ['영업이익', '컨센서스', 1000, 1200],
    ['영업이익', '잠정치', 900, 1400],
    ['당기순이익', '컨센서스', 800, 900],
    ['당기순이익', '잠정치', 700, 800],
]

# column명을 설정해주지 않아 자동으로 컬럼이 맵핑된다.
df = DataFrame(data=data)

# 멀티인덱스로 사용할 칼럼의 이름을 리스트로 전달
df = df.set_index( [ 0, 1 ] )
print("[43] Use Multi-index\n", df, "\n")

# 가독성을 높이기 위해 인덱스와 칼럼 네임을 지정
df.index.names = ["재무연월", ""]
df.columns = ["2020/06", "2020/09"]
print("[43] Use Multi-index after set indexes and columns\n", df, "\n")
print("[44] Slicing one index\n", df.loc['영업이익'], "\n")

# 두번의 슬라이싱으로 구할 수도 있지만 속도가 느리기 때문에 튜플의 형태로 원하는 값을 구하는 것이 더 빠르다.
print("[45] Double slicing\n", df.loc[ ('영업이익', '컨센서스') ], "\n")

# # 슬라이싱 예시
# a = [1, 2, 3, 4, 5]
# print(a[0:5:2])
# print(a[slice(0, 5, 2)])

# 적용
# slice(None) : level 0 에 해당하는 모든 값들을 선택하라는 의미
print(df.loc[ (slice(None), '컨센서스'), :])


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [9] Multi-column


