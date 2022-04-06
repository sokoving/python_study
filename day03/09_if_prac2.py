#배수 조건 
# A%4==0 (A는 4의 배수다/4로 나눴을 때 나머지가 없다)
# A%10!=0(A는 10의 배수가 아니다)


year=int(input())
if(year%4==0)and(year%100!=0)or(year%400==0):
    print(1)
else:
    print(0)