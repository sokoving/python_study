
'''#가로로 띄어쓰기 구분해서 한 줄에 입력받기
A, B=map(int, input().split())
print(A*B)'''
'''
A=int(input())
B=int(input())
'''

#문제1
A, B, C = map(int, input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)


#문제 2
A = int(input())
B = int(input())

C = A * (B // 10 ** 0 % 10)
print(C)

D = A * (B // 10 ** 1 % 10)
print(D)

E = A * (B // 10 ** 2 % 10)
print(E)

F = (C * 10 ** 0) + (D * 10 ** 1) + (E * 10 ** 2)
print(F)