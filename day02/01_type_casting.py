#정수 srt / 실수 float
'''
n1=10
n2='34'
print(n1+n2)
오류: 피연산자(operand)의 타입 불일치
'''
# 형 변환
n1=10
n2='34'
print(n1+int(n2)) #str > int
print(str(n1)+n2) #int > str

'''
s1='Hello'
print(int(n3))
문자열 내부값이 순수한 정수가 아닌 경우 변환 불가
'''

s2='3.14'
print(float(s2)) #실수로 변환

f1=3.1
print(int(f1)) #실수를 정수로 변환하면 변환이 됨(소수점 소실, 내림)
#사용 예시) 2천 원으로 600원 과자 몇 개를 살 수 있는가?

#반올림
f2=3.6
print(round(f2))
#두번째 소수점까지 반올림
f3=3.147
print(round(f3, 2))

#0 ''(빈 문자) >False
# 값이 있으면 True