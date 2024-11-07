def nLogNFunc(n):
    y = n
    while (n > 1):
        n = n // 2
        print(f'Level  {n}')
        for i in range(y):
            print(i)

nLogNFunc(4)