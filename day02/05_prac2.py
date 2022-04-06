
print('2개의 정숫값을 입력하세요.')
x=int(input('정수 x : ')) #사고의 순서대로 입력하여 코딩하면 좋다.(체계적으루~)
y=int(input('정수 y : '))
rate=round(x/y*100) #백분율 구하기
print(f'x값은 y값의 {rate}%입니다.')
# print(f'x값은 y값의 {int(x/y*100)}%입니다.')


print('2개의 정숫값을 입력하세요.')
x=int(input('정수 x : '))
y=int(input('정수 y : '))
reverse=int(-((x+y)/2)) #평균의 반전값
print(f'평균값의 부호를 반전한 값은 {reverse}입니다.')
