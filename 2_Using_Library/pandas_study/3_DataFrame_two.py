from pandas import DataFrame
from pandas import Series
import numpy as np

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

