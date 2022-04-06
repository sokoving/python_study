
x=int(input())
y=int(input())

if x>=0:
    if y>=0:        #중첩 조건문
        print(1)
    else:
        print(4)
else:
    if y>=0:
        print(2)
    else:
        print(3)

'''
if (x>0)and(y>0):
    print(1)
if (x<0)and(y>0):
    print(2)
if (x<0)and(y<0):
    print(3)
if (x>0)and(y<0):
    print(4)
'''