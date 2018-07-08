## Dictionary  = { key : value } 의 형태로 값을 저장 함

- 예시 : cat 이라는 dictionary 에는 ''이름, 품종, 나이'' 라는 Key값으로 아래와 같이 values를 가지고 있습니다.

  

cat = {}  

{ 이름 : 초코 , 파이 , 정 }

{ 품종 : 터키시앙고라 , 샴, 아메숏 }

{ 나이 : 3 , 5, 1 } 



1. key  : key를 가져옵니다. 
2. values() : values를 가져옵니다. 
3. item() : key와 values를 모두 가져옵니다.
4. cat.keys() : dictionary의 키 이름을 가져옵니다.
5. get('이름') : '이름'이라는 키의 values 를 가져옵니다. 

~~~
# -*- coding: utf-8 -*-

cat = {'이름': ['초코', '파이', '정'], '품종': ['터키시앙고라', '샴', '아메숏'], '나이': [3, 5, 1]}


for k in cat.keys():
	print(k)


이름
품종
나이

for v in cat.values():
	print(v)


['초코', '파이', '정']
['터키시앙고라', '샴', '아메숏']
[3, 5, 1]


for g in cat.get('품종'):
	print(g)


터키시앙고라
샴
아메숏


for i in cat.items():
	print(i)

('이름', ['초코', '파이', '정'])
('품종', ['터키시앙고라', '샴', '아메숏'])
('나이', [3, 5, 1])
~~~







