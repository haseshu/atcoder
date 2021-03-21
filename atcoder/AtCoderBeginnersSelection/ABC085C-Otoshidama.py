### きっと2文探索とか使う気がする
N, Y = map(int, input().split())
clear = False
for i in range (N+1):
    if clear is True or i * 10000 > Y:
        break
    for j in range(N + 1 - i):
        if clear is True or i * 10000 + j * 5000> Y:
            break
        for k in range(N + 1 - i - j):
            if clear is True or i * 10000 + j * 5000 + 1000 * k> Y:
                break
            if (clear is False) and (10000 * i + 5000 * j + 1000 * k == Y) :
                clear = True
                print("{} {} {}".format(i,j,k))
if clear is False:
    print("{} {} {}".format(-1,-1,-1))