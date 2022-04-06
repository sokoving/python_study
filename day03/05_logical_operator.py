'''
#논리 연산자

#and 연산 (예시: 로그인의 경우)
T and T → T  #둘 다 True일 경우에만 전체 결과 참
T and F → F
F and T → F
F and F → F

#or 연산
T or T → T  #둘 중 하나라도 True일 경우에 전체 결과 참
T or F → T
F or T → T
F or F → F
'''

from cgi import print_arguments


T=True
F=False

print(T and T)
print(T and F)
print(F and T)
print(F and F)

print('=====================')

print(T or T)
print(T or F)
print(F or T)
print(F or F)

print('=====================')

a=5
if(a>1) and (a<10):  #T and T → T
    print('a는 1과 10 사이의 정수입니다!')
else:
    print('a는 범위 안의 정수가 아닙니다.')

print('=====================')

b=4
if(b==2)or(b==4):  #F of F → F
    print('b는 2 또는 4입니다.')
else:
    print('b는 2 또는 4가 아닙니다.')