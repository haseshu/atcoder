N = int(input())
A =list(map(int, input().split()))

def half(i):
    return int(i/2)

can_half = True
count =0

while can_half is True:
    for i in A:
#        print(i)
        if i%2 != 0:
            can_half=False
#            print("{} is odd".format(i))
    if can_half is True:
        count = count +1
        A = list(map(half,list(A)))
print(count)
