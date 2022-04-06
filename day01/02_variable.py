'''
#variable(변수)
-프로그램 실행 중 입력되어 변화하는 값을 저장한다.

#변수의 특징
-데이터를 저장하는 공간이다.
-자료를 일관성 있게 사용, 관리, 할 수 있다.
-특정 값에 개발자가 이름을 부여해 다른 변수 또는 자료와 구분해서 사용.
'''
lucky_number=7
# 7을 lucky_number(기억 공간의 이름) 변수로 지정함
# 변수 코드는 출력되지 않는다.
# 변수 처리하는 기호 =는 대입의 의미(동일의 뜻 아님)
# 좌항(변수 이름), 우항(변수 값) 순서 지키기
# 변수 이름은 타인이 봐도 한눈에 알 수 있게 간결/명확하기 짓기
# 애매모호x, 띄어쓰기x, 약어x
print(lucky_number*3)
print(lucky_number)
lucky_number=3 #변수값 수정
print(lucky_number)

login_user_name='홍길동'
friend_user_name='김철수'

print(login_user_name+' 안녕?')
print('당신은 '+login_user_name+'!')
print('내 친구 '+friend_user_name+'~~')

'''
our_living_planet=Earth (snake case, 파이썬 선호)
ourLivingPlanet=Earth (camel case, 자바 선호)
'''
