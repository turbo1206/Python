for x in range(2,100):
    for y in range(2,x+1):
        if x%y == 0:
            if y == x:
                z = y
                print(z)
            else:
                break