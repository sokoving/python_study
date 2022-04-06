
korean=int(input('국어 : '))
english=int(input('영어 : '))
math=int(input('수학 : '))

total=(korean+english+math)
average_score=round((total/3), 2)
print(f'당신의 평균점수: {average_score}점')
if average_score>=60:
    print('이번 시험에 통과하셨습니다.')
else:
    print('재수강 대상자입니다.')
print('열공하세요!')

##평균점수 소수점 2자리까지 표시하기