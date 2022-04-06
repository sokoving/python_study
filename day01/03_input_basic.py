a=input() #프로그램 실행 중 입력
b=input() 
print(a+b)
print(type(a))
# input 함수는 키보드 입력을 처리하는 함수
# input의 특징음 문자열(str)로 처리됨.
# 따라서 산술 연산이 불가능함.

# int(input())
a=int(input())
print(a+10)
print(type(a))
#int(input()) 입력된 문자를 정수(int)로 변환
#단 정확한 정수를 쓰지 않으면 에러 발생
