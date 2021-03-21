### きっと2文探索とか使う気がする
N, Y = map(int, input().split())
clear = False
man, gosen, sen =  -1,-1,-1
for i in range (N+1):
    if clear is True or i * 10000 > Y:
        break
    for j in range(N + 1 - i):
        if clear is True or i * 10000 + j * 5000> Y:
            break
        if (clear is False) and (10000 * i + 5000 * j + 1000 * (N-i-j) == Y) :
                clear = True
                man =i
                gosen=j
                sen=N-i-j
                break
print("{} {} {}".format(man,gosen,sen))