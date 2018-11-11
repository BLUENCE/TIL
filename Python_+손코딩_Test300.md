

# 파이썬 300제 손코딩 오답노트 


몇번 치다보면(?) 제대로 작성할 수 있지만 ... 

파이썬 문법을 보다 정확하게 알고 사용하기 위해서 손코딩을 해보았다.

해당 문제를 손으로 풀어 보고 살짝 아리까리하면 모두 기록했다.


https://wikidocs.net/7090



```python
# 역 슬래쉬는 파이썬에서 특수 문자로 취급됩니다. 두 개의 역슬래쉬를 입력하면 하나의 역슬래쉬를 문자열로 출력할 수 있습니다.
print("C:\\\\Windows")   # 총 4개를 입력해야 2개의 슬래쉬가 나옴 
```

    C:\\Windows



```python
print("안녕하세요.\n만나서\t\t반갑습니다.")
```

    안녕하세요.
    만나서		반갑습니다.



```python
print("first");print("second")
```

    first
    second



```python
print("first", end="\n");print("second")
```

    first
    second



```python
print ("오늘은", 13, "일")  # 기본적으로 띄어쓰기 한칸을 한다 
```

    오늘은 13 일



```python
#007 print() 함수를 사용하여 다음과 같이 출력하라.

# naver;kakao;sk;samsung

print("naver","kakao",sk,samsum", sep=";")
```

    naver,kakao,sk,samsum


sep을 지정하지 않을 경우 그 값이 공백으로 설정되기 때문에, 
단어 사이에 공백이 추가되는 것입니다. 

sep을 사용한 코드는 구분자의 수정 발생 시 장점이 드러납니다. 구분자가 +로 바뀌어 "naver+kakao+sk+samsung"로 변경을 하는 경우, sep 부분의 한 글자만 수정하면 됩니다.


```python
print("naver", "kakao", "sk", "samsung", sep=";")
```

    naver;kakao;sk;samsung



```python
print("naver", "kakao", "sk", "samsung", sep="/")
```

    naver/kakao/sk/samsung



```python
a = "3"
b = "4"
print(a + b)  # 기본적으로 붙어나온다. 
```

    34



```python
lang = "power"
print(lang[0], lang[2])
```

    p w



```python
# 짝만 출력하고 싶다면 어떻게 해야 할까요? 시작 인덱스를 1로 변경하면 됩니다.
string = "홀짝홀짝홀"
print(string [::2])  # 슬라이싱 3번째거는 인덱스 증감폭지정 
```

    홀홀홀



```python
string = "홀짝홀짝홀"
print(string [1::2])
```

    짝짝



```python
print(string[::-1])
```

    홀짝홀짝홀



```python
phone_number = "010-1234-5678"
```


```python
phone_number.replace("-", "")
```




    '01012345678'




```python
lang = 'python'
```


```python
lang[0] = 'p'  #  기존에 생성한 문자열은 변경 할 수 없습니다.
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-157-1d5585986da1> in <module>()
    ----> 1 lang[0] = 'p'  #  기존에 생성한 문자열은 변경 할 수 없습니다.
    

    TypeError: 'str' object does not support item assignment


# 031 ~ 040
# 문자열 포메팅 ( Formatting )
https://wikidocs.net/13

문자열은 모두 같은데, 숫자만 달라지는 경우, 문자열 내의 특정 값만 바꿔야 하는 경우 

" 현재 온도는 18도 입니다"
" 현재 온도는 20도 입니다"


```python
# 1. 숫자 바로 대입  = %d

print( "나는 사과 %d개를 먹습니다." %3)
```

    나는 사과 3개를 먹습니다.



```python
# 숫자 변수 대입도 %d 

number = 3
print( "나는 사과 %d개를 먹습니다." % number)
```

    나는 사과 3개를 먹습니다.



```python
# 2. 문자열 바로 대입 = %s 

print( "나는 사과 %s개를 먹습니다. " %"다섯" )
```

    나는 사과 다섯개를 먹습니다. 



```python
# 특수문자 퍼센트를 쓰고싶으면 그앞에 퍼센트 하나 더 !

"Error is %d%%." % 98
```




    'Error is 98%.'




```python
# 2개 이상의 값 넣으려면, 퍼센트뒤에 괄호묶기!!

number = 3
day = "시험날"

print("%s 에 저는 사과 %d 개를 먹었습니다." %(day, number) ) 
```

    시험날 에 저는 사과 3 개를 먹었습니다.



```python
print("%10s" % "hi")  # 10개의 빈공간을 두고 hi를 출력 
```

            hi



```python
print("%-10sjane" % "hi")  # hi입력후 (s) , 10개 공백다음 jane 옴
```

    hi        jane



```python
"%0.4f" % 3.42134234  # 원하는 소수점 표기법 
```




    '3.4213'




```python
"%10.4f" % 3.42134234  # 10자리 문자열공간에서 오른쪽정렬 
```




    '    3.4213'




```python
print("I eat {} apples".format("five"))
```

    I eat five apples



```python
print("I eat {0} apples".format("five"))
```

    I eat five apples



```python
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day) )
```

    I ate 10 apples. so I was sick for three days.



```python
print("I ate {number} apples. so I was sick for {day} days.".format(number=2, day="two"))
```

    I ate 2 apples. so I was sick for two days.



```python
print("{:>10}".format("hi"))  # :> 오른쪽정렬이다
```

            hi



```python
print("{:^10}".format("hi"))  # :^ 가운데 정렬이다
```

        hi    



```python
print("{:=>10}".format("hi"))  # :=>10 공백을 =로 채우고 오른쪽정렬
```

    ========hi



```python
y = 3.42134234
print("{0:0.4f}".format(y))
```

    3.4213


### 파이썬 3.6에서는 ' f 문자열 포매팅 ' 기능을 사용할 수 있다


```python
name = "블라블라"
print(f'나의 이름은 {name} 입니다')
```

    나의 이름은 블라블라 입니다



```python
age = 30
print(f'나는 내년이면 {age+1} 입니다')
```

    나는 내년이면 31 입니다



```python
# 딕셔너리 문제에서 사용해보기 

d = {'name':'블라블라', 'age':30}


print( f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.' )
```

    나의 이름은 블라블라입니다. 나이는 30입니다.



```python
print(f"저는 {d['name']}입니다.")
```

    저는 블라블라입니다.



```python
# 문자열에서 문자의 개수 count 

a = "문자개수"
a.count('문')
```




    1




```python
# 문자 위치 알려주기 find 

a.find("룰")   # 없으면 -1이 나온다.
```




    -1




```python
a.index("룰")   # index는 없으면 없다고라도 알려준다 ㅠ 
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-214-ecaeec2d0353> in <module>()
    ----> 1 a.index("룰")   # index는 없으면 없다고라도 알려준다 ㅠ
    

    ValueError: substring not found



```python
# 문자열 삽입 (join)

a=","
a.join("가나다라")
```




    '가,나,다,라'




```python
",".join("가나다라")
```




    '가,나,다,라'




```python
# 오른쪽 공백지우기 

a= "     hi      "
a.rstrip()
```




    '     hi'




```python
a = "a:b:c:d"
a.split(':')
```




    ['a', 'b', 'c', 'd']




```python
":".join(['a', 'b', 'c', 'd'])
```




    'a:b:c:d'




```python
8 // 3  # 몫은 // , 나머지는 %
```




    2




```python
8 % 3
```




    2




```python
divmod(8,3)  # divmod 몫과 나머지를 한번에!
```




    (2, 2)



## 041 ~ 050 : 파이썬 기본 자료구조 

리스트/튜플/딕셔너리/셋 연습문제


```python
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
movie_rank.append("베트맨")
movie_rank
```




    ['닥터 스트레인지', '스플릿', '럭키', '베트맨']



insert 메서드는 새로운 값이 추가되는 위치를 지정할 수 있습니다.

인덱스 1번은 닥터 스트레인지와 스플릿 사이를 가리킵니다.


```python
movie_rank.insert(1, "슈퍼맨")

movie_rank
```




    ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '베트맨']




```python
movie_rank.remove('럭키')

# del movie_rank[3]  

movie_rank
```




    ['닥터 스트레인지', '슈퍼맨', '스플릿', '베트맨']



## 051 ~ 060 


```python
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
```


```python
" ".join(interest)
```




    '삼성전자 LG전자 Naver SK하이닉스 미래에셋대우'




```python
"/".join(interest)
```




    '삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우'




```python
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우

print("\n".join(interest))
```

    삼성전자
    LG전자
    Naver
    SK하이닉스
    미래에셋대우



```python
string = "삼성전자/LG전자/Naver"
```


```python
string.split("/")
```




    ['삼성전자', 'LG전자', 'Naver']



## 061 ~ 070


```python
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0  # 리스트 전체를 넣어버리면 원본도 바뀐다. 
interest_1[0] = 'Naver'
print(interest_0)
```

    ['Naver', 'LG전자', 'SK Hynix']



```python
interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
interest_1 = interest_0[:]  # 슬라이싱해서 넣으면 0은 안바귄다. 
interest_1[0] = 'Naver'
print(interest_0)
```

    ['삼성전자', 'LG전자', 'SK Hynix']



```python
t = 1, 2, 3, 4  # t의 타입은 튜플!!!!! 이다!!! 왜? 괄호가 없어도 튜플로 인식해서..
```


```python
type(t)
```




    tuple




```python
# 변수 t에는 아래와 같은 값이 저장되어 있다. 
# 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.

t = ('a', 'b', 'c')  #  괄호모양을 보니 튜플이네
```


```python
t = t[0].upper(), t[1], t[2]
t
```




    ('A', 'b', 'c')




```python
t[0] = '라'  # 튜플은 엘리먼트의 값이 바뀔 수 없다!!!
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-61-2de81540b330> in <module>()
    ----> 1 t[0] = 'a'
    

    TypeError: 'tuple' object does not support item assignment



```python
my_tuple = (1, 2, 3)
a, b, c = my_tuple
```


```python
print (a+b+c)
```

    6



```python
create_tuple = (1, )  # 튜플 데이터1개 저장하려면 쉼표 입력!
create_tuple
```




    (1,)




```python
create_tuple = (1)
create_tuple  # 튜플이 아니라 정수가 나와버림 
```




    1



## 071 ~ 080  : 데이터 언패킹

기본적으로 좌변 변수 = 우변 데이터 개수 

* *(star expression)을 사용하면 달라도 사용가능


```python
a, b, *c = (0, 1, 2, 3, 4, 5)
```


```python
c
```




    [2, 3, 4, 5]




```python
# 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 
# 좌측 8개의 값을 valid_score 변수에 바인딩하여라

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
```


```python
*valid_score, b, c = scores  # 앞에 8개가 모조리들어가고 나머지 2개는 b,c로

valid_score
```




    [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]



## 딕셔너리 제대로 다시 공부하기 

- 순서없음

- Key는 고유한 값이므로 중복되게 하면 하나 제외하고 모두 무시된다.


    => 따라서 가변적인 리스트는 키값으로 못오고, 튜플은 키값으로 가능!



```python
temp = {}
type(temp)
```




    dict




```python
# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라

icecream_price = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
icecream_price
```




    {'메로나': 1000, '빵빠레': 1800, '폴라포': 1200}




```python
# 딕셔너리에 요소 추가하기 = 딕셔너리 쌍 추가하기 
# 맨 뒤에 들어가는게 아니라 순서는 지멋대로다.ㅠ

icecream_price['월드콘'] = 2000  
icecream_price
```




    {'메로나': 1000, '빵빠레': 1800, '월드콘': 2000, '폴라포': 1200}




```python
# 딕셔너리 요소 삭제하기 

del icecream_price['메로나']

icecream_price
```




    {'빵빠레': 1800, '월드콘': 2000, '폴라포': 1200}




```python
# 모든 키, 밸류 삭제는 클리어!

icecream_price.clear()

icecream_price
```




    {}



## 081 ~ 090


```python
inventory = { '메로나' : [300, 20] } 
inventory
```




    {'메로나': [300, 20]}




```python
print(inventory['메로나'][0], "원")  # print(int, str) => 300원
```

    300 원



```python
inventory['월드콘'] = [500, 7]   # 데이터 추가 
inventory
```




    {'메로나': [300, 20], '월드콘': [500, 7]}




```python
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
```


```python
sum(icecream.values())
```




    6700




```python
# 새로운것 추가하기 

new_product = {'팥빙수':2700, '아맛나':1000}
new_product
```




    {'아맛나': 1000, '팥빙수': 2700}




```python
icecream + new_product  # dict끼리는 합치기가 안된다 ;; .update 써라  
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-144-cc1f7608bf78> in <module>()
    ----> 1 icecream + new_product  # dict끼리는 합치기가 안된다 ;;
    

    TypeError: unsupported operand type(s) for +: 'dict' and 'dict'



```python
# 딕셔너리는 update() 메서드를 제공하는데
# 이는 파라미터로 전달받은 딕셔너리의 값을 현재 딕셔너리에 추가합니다. 

icecream.update(new_product)
                
icecream  # 바로 프린트하면 None이 출력되길래..
```




    {'메로나': 1000,
     '빵빠레': 1800,
     '아맛나': 1000,
     '월드콘': 1500,
     '탱크보이': 1200,
     '팥빙수': 2700,
     '폴라포': 1200}



### (089) 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라.
### (힌트) ZIP함수 쓰면 두개의 자료구조를 하나로 묶어준다

keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.

keys = (apple, pear, peach)

vals = (300, 250, 400)


```python
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys,vals))
result
```




    {'apple': 300, 'peach': 400, 'pear': 250}



### (090)  두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.

date = ['09/05', '09/06', '09/07', '09/08', '09/09']


close_price = [10500, 10300, 10100, 10800, 11000


```python
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000 ]
```


```python
result2 = dict(zip(date,close_price))
result2
```




    {'09/05': 10500,
     '09/06': 10300,
     '09/07': 10100,
     '09/08': 10800,
     '09/09': 11000}



## 091 ~ 100  : 파이썬 제어문 input, if문


```python
print(input()*2)
```

    안녕하세요
    안녕하세요안녕하세요



```python
result = (input())
type(result)
```

    30





    str




```python
# 사용자로부터 숫자를 입력받고, 10을 더해서 출력해라 

print( int(input("숫자를 입력하세요: ")) + 10 )
```

    숫자를 입력하세요: 30
    40



```python
#  사용자로부터 값을 입력받은 후 해당 값에 +20을 더한 값을 출력하라. 
# 단 값의 범위는 0~255로 가정한다. 255를 초과하는 경우 255를 출력해야 한다.

x = int(input()) + 20 

if x > 255:
    print(255)
    
else:
    print(x)
    
```

    240
    255



```python
# min함수를 쓰면 항상 작은 값이 출력되기 때문에 간결해진다.

pixel = int(input("입력값:")) 

print ("출력값:", min(pixel + 20, 255))
```

    입력값:240
    출력값: 255



```python
user_in = input()

if user_in.islower():
    user_in = user_in.upper()
else :
    user_in = user_in.lower()
    
print(user_in)
```

    ABCD
    abcd


### (112) 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.

점수	학점

81~100	A

61~80	B

41~60	C

21~40	D

0~20	E


힌트 : 구간이므로, if elif else 문 사용

### (120)


```python
volatility = int(btc['max_price']) - int(btc['min_price'])
if int(btc['opening_price']) + volatility > int(btc['max_price']) :
    print("상승장")
else :
    print("하락장")
```

# 환율입력받고 변환 

ratio = [100, 200, 300]  # 달러 엔화 유로 

금액 = int(input.split[0])

화폐종류 = input.split[1]

if 화폐종류 == "달러":

    result = ratio[1] * 금액 
    
elif 화폐종류 == "유로":

else:


print(result)


```python
if x.split(' ')[1] == '엔':
    print( int(x.split(' ')[0])*엔 ) 
    
    # 소수점 4번째 자리까지만 표현해라 
    
    print ( "%0.4f" % (int(x.split(' ')[0])*엔) )
```

    109.60000000000001
    109.6000



```python
a = int(input())  # 무조건 인풋값은 int로 바꿔줘야 한다
b = int(input()) 
c = int(input()) 

print(max(a,b,c))
```

    10
    4
    70
    70


### (119) 주민번호 유효성검사

13자리 주민번호 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.

먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 

연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

      8 2 1 0 1 0 - 1 6 3 5 2 1 0
  
    x 2 3 4 5 6 7   8 9 2 3 4 5 

-----------------------------
1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) 

= (128 % 11) = 7

2차 계산: 11 -7 = 4

위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다.

즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

다음과 같이 사용자로부터 주민등록번호를 입력받은 후 

주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

### (120)  비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.

btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 

최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 

최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.



```python
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
```


```python
btc
```




    {'24H_fluctate': '-30000',
     '24H_fluctate_rate': '-0.41',
     'average_price': '7249834.0437',
     'buy_price': '7234000',
     'closing_price': '7234000',
     'date': '1541947444231',
     'max_price': '7274000',
     'min_price': '7229000',
     'opening_price': '7264000',
     'sell_price': '7240000',
     'units_traded': '87231.13412056',
     'volume_1day': '87231.13412056',
     'volume_7day': '578187.69584415'}




```python
변동폭 = int(btc['max_price']) - int(btc['min_price'])

if int(btc['opening_price']) + 변동폭 > int(btc['max_price']) :
    print("상승장")
else :
    print("하락장")

```

    상승장


## 121 ~ 160  : 파이썬 반복문


```python
menu = ["김밥", "라면", "튀김"]

for i in menu:
    print("오늘의 메뉴: %s" % i)
```

    오늘의 메뉴: 김밥
    오늘의 메뉴: 라면
    오늘의 메뉴: 튀김



```python
for i in menu:
    print("오늘의 메뉴: " + i)  # 문자열이니까 더해서 걍 출력
```

    오늘의 메뉴: 김밥
    오늘의 메뉴: 라면
    오늘의 메뉴: 튀김



```python
prices = [100, 200, 300]

for i in prices:
    print(i+10)
```

    110
    210
    310



```python
# menu 리스트에는 음식이름이 뒤집혀 저장돼 있다. 
# 이를 읽기 좋게 뒤집어서 아래와 같이 출력하라.

menu = ["면라", "밥김", "김튀"]

for i in menu:
    print(i[::-1])

```

    라면
    김밥
    튀김


## 231 ~ 250  : 파이썬 함수


```python
def print_coin():
    return(print("비트코인"))
```


```python
print_coin()
```

    비트코인



```python
# "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라. 
# 한 라인에 하나씩 "비트코인" 문자열을 출력한다.

def print_coin():
    for i in range(100):
        print("비트코인")  # 100번 출력되게한다. 출력되니까 return 필요없

```

## 번외)  파이썬 클래스 , 상속 

참고하기 : https://wikidocs.net/28


- C 언어에는 클래스가 없다. 

- 과자 틀 → 클래스 (class)
- 과자 틀에 의해서 만들어진 과자들 → 객체 (object)

클래스(class)란 똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계 도면 같은 것이고(과자 틀), 객체(object)란 클래스에 의해서 만들어진 피조물(과자틀에 의해서 만들어진 과자)을 뜻한다.



```python
class FourCal:
    
    def setdata(self, f, s):  # self = a (본인)
        self.first = f
        self.second = s
        
    def sum(self):
        result = self.first + self.second
        return result
```


```python
a = FourCal()  # 클래스객체 a 만듬
a.setdata(2,4)  # 객체 a에 변수할당 
```


```python
a.sum()  # 더해라
```




    6



a = FourCal()  한다음 

a.sum(2,4) 를 하면?

에러가난다. 변수에 할당이 된게없기 때문이다.

그렇다고 항상 setada 라는 함수를 실행시켜서  변수를 할당시키기 귀찮으니, 

생성자(Constructor)를 쓰는 것이다.

- 생성자 : 객체가 생성될 때 자동으로 호출되는 메서드 


```python
def __init__(self, first, second):
    self.first = first
    self.second = second
```


```python
# 대신에 앞으로는 자동으로 init이 호출되므로 인자값을 줘야한다! 

a = FourCal(4,2)  
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-271-dbc06d83a26e> in <module>()
    ----> 1 a = FourCal(4,2)
    

    TypeError: object() takes no parameters


### 상속 : class 상속받을\_클래스명(기존\_클래스명):


```python
class MoreFourCal(FourCal):
    pass
```

### 메서드 오버라이딩

SafeFourCal 클래스는 FourCal클래스에 있는 div라는 메서드를 동일한 이름으로 다시 작성하였다. 

이렇게 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다. 

이렇게 메서드를 오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.


```python
# 아래 에러가 나는 이유를 고치시오. 
```


```python
class Calculator:
    def __init__(self):
        self.value = 0

    def add(val):
        self.value += val
```


```python
cal = Calculator()
cal.add(3)
cal.add(4)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-280-6f03ef0f0273> in <module>()
          1 cal = Calculator()
    ----> 2 cal.add(3)
          3 cal.add(4)


    TypeError: add() takes 1 positional argument but 2 were given



```python
# 메서드의 첫번째 입력인수는 항상 self이어야 하므로 다음과 같이 클래스를 수정해야 한다.

def add(self, val):
    self.value += val
```

## 번외) Comprehension 제대로 익히기 


```python
# 리스트 컴프리헨션

[x for x in range(10)]
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
# 람다

더하기 = lambda a, b: a+b
```


```python
더하기(3,4)
```




    7



## 번외) 정규표현식 

참고하기 : https://wikidocs.net/4308

메타문자 : 파이썬에서 특별한 용도로 사용하는 문자

. ^ $ * + ? { } [ ] \ | ( )

[a-zA-Z] : 알파벳 모두

[0-9] : 숫자

\d : 숫자매치

\D = [^0-9] 

\s = 공백 = [\t\n\r\f\v]

\w = 문자 + 숫자만 매치 = [a-zA-Z0-9]

\W = 문자 숫자아닌거만 매치 


- a[.]b 하면 a.b만 매칭된다. 


```python
import re

re.match('ab*')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-255-9dab24274bdf> in <module>()
          1 import re
          2 
    ----> 3 re.match('ab*')
    

    TypeError: match() missing 1 required positional argument: 'string'


## 번외) 소트하기 

- sorted(a) : 복사 소트

- a.sort() : 원본 소트 (점이 붙으면 원본에다가 하는거같다) 


```python
a = [5, 3, 2, 1]
sorted(a)
```




    [1, 2, 3, 5]




```python
a.sort()  # 바로 프린트하면 None 이 뜬다 . 

print(a)
```

    [1, 2, 3, 5]



```python
a  # sort를 하면 원본이 바뀌기 때문이다.
```




    [1, 2, 3, 5]




```python
# key이용해서 소트하기 

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

# 이 리스트를 나이 순으로 소트하려면 어떻게 해야 할까?
```


```python
students
```




    [('jane', 22, 'A'), ('dave', 32, 'B'), ('sally', 17, 'B')]


