
#가로로 출력
dog='멍멍이'
cat='야옹이'
print(dog, cat, '짹짹이', sep='')  #sep(구분자) 값 사이에 무엇을 넣을 것인가.
print(dog, cat, '짹짹이', sep='!')  #별도 지정하지 않으면 ' '로 기본값 지정.

#세로로 출력
fruit='딸기'
food='짜장면'
print(fruit); print(food) 

#\n (엔터, 줄바꿈, 문자 형식)
print(fruit + '\n')
print(food)

#end : 출력값 마지막에 출력되는 값, 별도 지정하지 않으면 기본값 \n으로 지정
print(fruit, end='') 
print(food)