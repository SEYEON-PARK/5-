def calsum(a, b):
    print(a+b)
def calminus(a, b):
     print(a-b)
def calmul(a, b):
     print(a*b)
def caldiv(a, b):
     print(a/b)

a=input('계산하고 싶은 수식을 입력하시오.(숫자 연산자 숫자) : ')
a=a.split(" ")
x=int(a.pop(0))
y=int(a.pop(1))
if('+' in a ):
    calsum(x, y)
elif('-' in a ):
    calminus(x, y)
elif('*' in a ):
    calmul(x, y)
elif('/' in a ):
    caldiv(x, y)
else :
    print("잘못 입력하셨습니다.")

