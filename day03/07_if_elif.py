'''
#다중분기 조건문 if ~ elif
-3개 이상의 분기를 만들 때 사용하는 조건문(다지선다)
-elif 대신 if를 쓰면 개별 그룹으로 판단해 하나하나 다 값을 낸다.
-위에서부터 조건을 검색해 내려온다.
 그렇기 때문에 범위조건의 경우 상위 조건이 하위 조건을 포괄적으로 포함하지 않도록 한다.
-else 필수는 아님. True가 없을 경우 아무것도 안 하고 종료.
    
'''

age=int(input('나이 : '))
if age>= 20: #거짓일 경우 아래 이어서 검색
    print('성인입니다.') 
elif age>= 17: #참일 경우 검색 중지, 참 출력.
    print('고딩입니다.')
elif age>= 14:
    print('중딩입니다.')
elif age>= 8:
    print('초딩입니다.')
else: #위에가 전부 거짓일 때 마지막에 else 출력
    print('미취학 아동입니다.')
        