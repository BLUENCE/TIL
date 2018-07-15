## 예제를 통해 Pandas 사용해보기



### 1. 환경 준비하기



~~~
!pip install --upgrade -q gspread

import pandas as pd

from google.colab import auth

auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials


def get_sheet(title, sheet_name):
  gc = gspread.authorize(GoogleCredentials.get_application_default())
  return gc.open(title).worksheet(sheet_name)
~~~



Pandas 를 pd로 import 하고 

get_sheet 에 대한 함수를 정의한다.  



### 2. 자료의 요약 불러오기 

~~~
# 자료의 요약에 있는 '특정 시트'를 불러옵니다.
# 1번 row를 0번 인덱스로 읽어오는 데, 0번 인덱스를 컬럼으로 지정해 주도록 했습니다.
# 그러면 스프레드시트에서 봤던 것 처럼 데이터프레임이 생성됩니다.

def get_df(sheet_name):
  sheet = get_sheet('자료의 요약', sheet_name)

  # Create dataframe from the sheet
  rows = sheet.get_all_values()
  df = pd.DataFrame.from_records(rows)

  df.columns = df.iloc[0]  # 0번째 있는 값을 컬럼으로 지정한다.
  df = df.reindex(df.index.drop(0)) # 0 이라는 제목을 버리고 컬럼 0 을 reindex한다
  return df
~~~

[파이썬 pandas DataFrame의 iloc, loc, ix의 차이](http://yeyej.blogspot.com/2016/02/pandas-dataframe-iloc-loc-ix.html)



#### .iloc

integer positon를 통해 값을 찾을 수 있다. label로는 찾을 수 없다

#### .loc

label 을 통해 값을 찾을 수 있다. integer position로는 찾을 수 없다.

#### .ix

integer position과 label모두 사용 할 수 있다. 만약 label이 숫자라면 label-based index만 된다.



### 3. 자료의 요약 내에서 원하는 시트 불러오기 

~~~
sheet = get_sheet('자료의 요약', '혈액형')

# Create dataframe from the sheet

rows = sheet.get_all_values()
df = pd.DataFrame.from_records(rows)


df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0))
~~~



### 4. 데이터 탐색해보기(예제) 

~~~
df_blood = get_df('혈액형')     # 혈액형 데이터를 불러와서 df타입으로 저장 

# 상위 5개의 데이터를 가져옵니다.
print(df_blood.shape)     # 몇행 몇열로 구성되어 있는지 보기 
df_blood.tail(3)          # 맨 마지막 3개 자료만 보기 
df_blood.head()           # 상위 5개의 자료만 보기 

df_blood.columns		# 어떤 컬럼이 있는지 보기
df_blood.info()			# 어떤 컬럼이 있고 데이터의 row, column 수, 데이터 타입을 볼 수 있다.
df_blood.isnull().sum()   # 결측치가 보고 싶을 때 널값을 구해 본다. 

#  period 순으로 가장 오래 집권한 왕순으로 정렬해 보고 상위 5개의 데이터만 본다.
df_king.sort_values(by='period', ascending=False)   

# 데이터 타입을 int로 변경해 준다.
df_king['life'] = df_king['life'].astype(int)
df_king['period'] = df_king['period'].astype(int)

# 데이터의 타입이 object 인지 int 인지에 따라 describe() 했을 때의 보여주는 정보가 다르다. 
# 수치형 데이터 일 때는 describe()하면 count, mean, std, min/max, 사분위수를 보여준다.

df_king.mean()    		# 평균값만 본다
df_king.std() 			# 표준편차만 본다 
df_king.max() 			# 최대값만 본다. 
df_king['period'].max()    # period를 기준으로 최대값을 본다 .

df_king['life'].plot()    # life를 기준으로 꺾은선 그래프 그려보기 
da_king['life'].hist()    # life를 기준으로 히스토그램 그려보기 
df_king['period'].hist(stacked=True, bins=10) 


df_titanic['Class'].value_counts()     # 'class'에 있는 값들을 카운트 해준다. 

							
~~~



 `df_animal['몸무게', '뇌무게'].mean()` 형식으로 칼럼 이름을 명시하려면

 `df_animal[['몸무게', '뇌무게']].mean()`처럼 대괄호를 두개씩 써야 한다.





