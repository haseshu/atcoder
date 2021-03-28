N = int(input())

print(N)

a = []
t = []
for i in range(N):
    ai,ti = list(map(int,input().split()))
    a.append(ai)
    t.append(ti)
print(a)
print(t)
Q = int (input())
print(Q)
x = list(map(int, input().split()))
print(x)

f=[-999] * Q

##ここを作る
def saiki(i):
    if f[i] == -999:
        if t[i] == 1:
            f[i] = saiki(i-1) + a[i]
        elif t[i] == 2:
            f[i] = max()
            pass
        elif t[i] == 3:
            pass

    if f[i] == -999:
        f[i] = saiki(i-1)

    pass

for i in range(Q):
    pass
