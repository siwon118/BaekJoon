while True:
    x, y, z = map(int, input().split())

    if x == 0 and y == 0 and z == 0:
        break

    if x > y and x > z:
        if x*x == y*y + z*z:
            print('right')
        else:
            print('wrong')
    elif y > x and y > z:
        if y*y == x*x + z*z:
            print('right')
        else:
            print('wrong')
    elif z > x and z > y:
        if z*z == x*x + y*y:
            print('right')
        else:
            print('wrong')
