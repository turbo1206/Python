# print("hello world")
# i=1+1
# print(i)
# a=2
# b=2
# c=a*b
# print(c)

# for i in range(1,10):
#     for j in range(1,3):
#         print(i,j)

# i=4
# j=3
# if i>j:
#     print(i)
# else:
#     print(j)

# 구구단 출력
# 연결연산자(+) "Hello"+"World"
# for a in range(1,10):
#     for b in range(1,10):
#          print("{}x{}={}".format(a,b,a*b))
#          print(a,"x",b,"=",a*b)

# a="안녕하세요"
# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# while문
# i=1
# while i<10:
#     print(i)
#     i=i+1

# i=1
# while True:
#     print(i)
#     if i>10:
#         break
#     i=i+1

# print문의 다양성
# import math

# i=16
# print(math.sqrt(i))
# print(f'the value {math.pi:3f}')
# print(f'the value {math.pi:9f}')
# name="Jang Yeon Seo"
# print(f'the name [{name}]')
# print("Hello",end=" & ")
# print("world")

# for i in range(10):
#     print(i*' ',end='')
#     print('*')

# i=12
# j=24
# print('i={}, j={}, str={}'.format(i,j,str))

# 함수선언 후 호출
# def makeBlank(n):
#     return n*' '
# for i in range(1,11):
#     print(makeBlank(i)+'*')

# 배열
# l1=[1,100,25,47,-12,5,-1234]
# for i in l1:
#     print(i)

# l1=[1,100,25,47,-12,5,-1234]
# for i in range(len(l1)):
#     print(l1[i])

# Tuple(튜플): 리스트와 동일하나, ****수정불가.
# l=(1,12,"hello","mine",3.14)
# for i in l:
#     print(i)

# x=10
# y=20
# x,y=y,x
# print(x,y)

# l1=[10,20,30,40]
# l1.append(50)
# l1.remove(10)
# print(l1)

# Set(집합): 리스트와 동일, 수정가능, ****중복 값 불허, *** index 없음.

# l1=[10,20,30,10,20,30] #len(l1) == 6
# l1=(10,20,30,10,20,30) #len(t1) == 6
# s1={10,20,30} #len(s1) == 3

# Dictionary(사전): key, value couple(쌍), 중복 '값' 허용, ***index없음(key사용)
d1={'name':'Jang Yeon Seo','age':27,'ciry':'cheonan','mobile':'82265231'}
for i in d1:
    print(i)

for i in d1.values():
    print(i)
# 저장