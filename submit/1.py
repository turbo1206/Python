# for x in range(2,100):
#     for y in range(2,x+1):
#         if x%y == 0:
#             if y == x:
#                 z = y
#                 print(z)
#             else:
#                 break

for x in range(2,1000):
    z=0
    for y in range(2,x):
        if x%y==0:
            z=1
            break
    if z == 0:
        print(x, end=" ")