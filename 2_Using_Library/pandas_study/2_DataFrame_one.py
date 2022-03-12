# Pandas Series가 1차원 데이터를 표현하는 자료구조라면, DataFrame은 2차원 데이터를 표현하는 데이터 구조이다.
# 엑셀 파일로 생각한다면 행과 열이 모두 존재하는 데이터로 생각하면 된다.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
from pandas import DataFrame, Series


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [1] Basic Usage
# 1. 딕셔너리로 데이터프레임 생성
# 2. 리스트로 데이터프레임 생성
# 3. 리스트와 딕셔너리로 데이터프레임 생성

# [1] - 1
data = {
    '종목코드': ['037730', '036360', '005760'],
    '종목명': ['3R', '3SOFT', 'ACTS'],
    '현재가': [1510, 1790, 1185]
}

df = DataFrame(data)           # DataFrame 클래스의 객체 생성 (생성자 호출)
print("[1] 딕셔너리로 데이터프레임 생성\n", df, "\n")

# [1] - 2
data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185],
]
columns = ["종목코드", "종목명", "현재가"]

df = DataFrame(data=data, columns=columns)
print("[2] 리스트로 데이터프레임 생성\n", df, "\n")

# [1] - 3
data = [
    {"종목코드": "037730", "종목명": "3R", "현재가": 1510},
    {"종목코드": "036360", "종목명": "3SOFT", "현재가": 1790},
    {"종목코드": "005760", "종목명": "ACTS", "현재가": 1185},
]

df = DataFrame(data=data)
print("[3] 리스트로 데이터프레임 생성\n", df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [2] Index of DataFrame

# 기본으로 설정되어 있는 0, 1, 2 ,,, 가 아니고 해당 열을 Index로 사용
data = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005760", "ACTS", 1185, 1.28],
]
columns = ["종목코드", "종목명", "현재가", "등락률"]
df = DataFrame(data=data, columns=columns)
# df = df.set_index('종목코드')  # 종목코드를 열의 index로 활용
# df = df.set_index('종목명')
df.set_index('종목명', inplace=True)
print("[4] 데이터프레임 인덱스 설정\n", df, "\n")

# index parameter를 따로 지정하여 설정
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28],
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]

df = DataFrame(data=data, index=index, columns=columns)
df.index.name = "종목코드"
print("[5] parameter로 index를 지정\n", df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [3] Column indexing
# DataFrame은 기본적으로 []기호로 Column 별 인덱싱을 지원한다.
# 'df.column명' 이런 식으로도 이용할 수 있다.
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
print("[6] 데이터프레임 칼럼별 인덱싱\n", df['현재가'], "\n")
print("[7] 데이터프레임 칼럼별 인덱싱\n", df.현재가, "\n")

# 칼럼 슬라이싱
# 리스트에 들어가는 항목 먼저 표시된다.
li = ["종목명", "현재가"]
print("[8] 데이터프레임 칼럼별 슬라이싱\n", df[li], "\n")
# 또는 변수를 사용하지 않고 간단하게 한줄로 표현 할 수도 있다.
print("[9] 데이터프레임 칼럼별 슬라이싱\n", df[["현재가", "등락률"]], "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [4] Row indexing
# Row별 인덱싱은 loc, iloc method를 사용한다.
# loc : 인덱스를 기준으로 데이터 추출
# iloc : 행 번호를 기준으로 데이터 추출

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
print("[10] 데이터프레임 인덱스 별 출력\n", df.loc[ [ "037730", "036360" ] ], "\n")
print("[11] 데이터프레임 행 별 출력\n", df.iloc[ [ 0, 1 ] ], "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [5] Get specific data
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

print("[12] 특정 데이터 가져오기\n", df.iloc[0].iloc[2])  # 시리즈 행 번호
print(df.iloc[0].loc["현재가"])  # 시리즈 인덱스
print(df.iloc[0][2])  # 시리즈 인덱스
print(df.iloc[0]["현재가"], "\n")  # 시리즈 인덱스

print("[13] 특정 데이터 가져오기 (한번에 표현하는 방법)\n", df.loc["037730", "현재가"])  # 같은 의미 다른 문법으로 사용
print(df.iloc[0, 1], "\n") 

print("[14] 컬럼을 먼저 분리한 후 그중에서 값을 찾아오는 방법\n", df['현재가'].iloc[0])  # 먼저 컬럼 별로 정보를 받아온 후, 필요한 정보를 탐색
print(df['현재가'].loc["037730"])
print(df['현재가']["037730"], "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [5] Get specific data in Range
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

# 위와 같이 코딩을 진행하면 두 번의 슬라이싱을 해야하기 때문에 성능 저하의 문제가 생길 수 있다.
# 때문에 아래와 같이 한번에 범위를 지정하여 사용한다.
print("[15] 범위 값으로 데이터를 불러오는 방법(loc 이용)\n", df.loc[["037730", "036360"], ["종목명", "현재가"]], "\n")
print("[16] 컬럼을 먼저 분리한 후 그중에서 값을 찾아오는 방법(iloc 이용)\n", df.iloc[[0, 1], [0, 1]], "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [6] DataFrame Filtering
# 특정 조건을 만족하는 데이터 값들만 불러오는 방식이다.
# 조건을 설정하면 Boolean Value를 반환받는 형태로 이루어져있다.
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)
cond = df['현재가'] >= 1400
print("[17] Condition Setting\n",cond, "\n")
print("[18] Result 1\n",df.loc[cond], "\n")

cond = (df['현재가'] >= 1400) & (df['현재가'] < 1700)
print("[19] Result 2\n",df.loc[cond], "\n")
print("[20] Result not 2\n",df.loc[~cond], "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [7] Add Column
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

s = Series(data=[1600, 1600, 1600], index=df.index)
# Use Series Data to Add column
df['목표가'] = s
print("[21] Add new Column 1\n",df, "\n")

# Use DataFrame utility Function
df['test'] = [1800, 2000, 3000]
print("[22] Add new Column 2\n",df, "\n")

# Calculate new column and Add that column
df["괴리율"] = (df["목표가"] - df["현재가"]) / df['현재가']
print("[23] Add new Column 3\n",df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [8] Add a row
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

# 새로운 인덱스 값으로 새로운 행을 추가
s = Series(data=["LG전자", 60000, 3.84], index=df.columns)
df.loc["066570"] = s
print("[24] Add new Row 1\n",df, "\n")

# 시리즈 데이터를 사용하지 않고 리스트를 사용해서 추가하면 원래 정해진 컬럼 순서대로 저장된다.
df.loc["044230"] = ['SK하이닉스', 80000, 1.66]
print("[25] Add new Row 2\n",df, "\n")

# DataFrame의 append 매서드를 이용하여 로우를 추가
s = Series(data=["테슬라", 1000000, 13.84], index=df.columns, name="082570")
new_df = df.append(s)
print("[25] Add new Row 3\n",new_df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [8] Delete Column & Row
# Using drop() method
# Parameter axis (1 : column / 0 : row) delete
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

# 현재가 column을 제거하고 df에 결과 값 저장(inplace)
df.drop("현재가", axis=1, inplace=True)  # 원본 데이터프레임 변경
print("[26] Delete specific column\n",df, "\n")

# 종목번호 037730인 인덱스 데이터를 삭제(row 별 삭제)
print("[27] Delete specific row\n",df.drop("037730", axis=0), "\n")

# 한번에 여러 개 데이터 삭제
df.drop(["037730", "005760"], axis=0, inplace=True)  # 원본 데이터프레임 변경
print("[28] Delete specific rows\n",df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [9] Change column label
data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]
df = DataFrame(data=data, index=index, columns=columns)

# change many column or index
df.columns = ['name', 'now price', 'fluctuation']          # 컬럼 이름 변경
df.index.name = 'code'                           # 인덱스 name 변경
print("[29] Change columns and index name 1\n",df, "\n")

# change by rename() method
df.rename(columns={'name': 'Stock name'}, inplace=True)
print("[30] Change columns and index name 2\n",df, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [10] Change Data type
data = [
    ["1,000", "1,100", "1,510"],
    ["1,410", "1,420", "1,790"],
    ["850", "900", "1,185"],
]
columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
print("[31] Check DataFrame\n",df, "\n")

# # remove comma to use replace method
# def remove_comma(x):
#     return int( x.replace(',', '') )

# df['03/02'] = df['03/02'].map(remove_comma)
# df['03/03'] = df['03/03'].map(remove_comma)
# df['03/04'] = df['03/04'].map(remove_comma)
# print("[32] Remove Comma\n",df, "\n")

def remove_comma(x):
    return int( x.replace(',', '') )

# applymap : 데이터프레임의 전체 데이터를 대상으로 map method() 연산을 진행한다.
df = df.applymap(remove_comma)
print("[32] Remove Comma\n",df, "\n")
print("[33] Data type\n",df.dtypes, "\n")

# Use astype method()
import numpy as np

def remove_comma(x):
    return x.replace(",","")

data = [
    ["1,000", "1,100", "1,510"],
    ["1,410", "1,420", "1,790"],
     ["850", "900", "1,185"],
]
columns = ["03/02", "03/03", "03/04"]
df = DataFrame(data=data, columns=columns)
df = df.applymap(remove_comma)
# astype은 딕셔너리 형태로 변환 값을 입력받는다.
df = df.astype( {"03/02":np.int64, "03/03":np.int64, "03/04":np.int64} )
print("[33] Data type change with astype() method\n",df.dtypes, "\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# [11] Preprocessing string data
data = [
    {"cd":"A060310", "nm":"3S", "close":"2,920"},
    {"cd":"A095570", "nm":"AJ네트웍스", "close":"6,250"},
    {"cd":"A006840", "nm":"AK홀딩스", "close":"29,700"},
    {"cd":"A054620", "nm":"APS홀딩스", "close":"19,400"}
]
df = DataFrame(data=data)

# 'cd' column 데이터 값 중 A를 제외하고 남은 데이터 들을 다시 저장
df['cd'] = df['cd'].str[1:]
print("[34] 'cd' column's data changing\n",df, "\n")

# Use str function to delete comma
df['close'] = df['close'].str.replace( ',', '' ).astype(np.int64)
print("[34] Using str's replace method and astype method to remove comma\n",df, "\n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------ #