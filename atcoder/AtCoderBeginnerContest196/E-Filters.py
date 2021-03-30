##タイムアウトと、一部実行時エラーが出る。
N = int(input())
#print(N)

a = []
t = []
for i in range(N):
    ai,ti = list(map(int,input().split()))
    a.append(ai)
    t.append(ti)
#print(a)
#print(t)
Q = int (input())
#print(Q)
x = list(map(int, input().split()))
#print(x)

f=[-999] * Q

##ここを再帰ではなく、1回式を作ったらそれを保存して使いまわしにすればタイムアウトは無くなるのでは。

def saiki(q, n):
    if n == 0:
        if t[n] == 1:
            return a[n] + x[q]
        if t[n] == 2:
            return max([a[n], x[q]])
        if t[n] == 3:
            return min([a[n], x[q]])
    elif n == N-1:
        for i in range(q):
            if t[n] == 1:
                print(saiki(i, n-1) + a[n])
            elif t[n] == 2:
                print(max([a[n],saiki(i, n-1)]))
            elif t[n] == 3:
                print(min([a[n],saiki(i, n-1)]))
    else:
        if t[n] == 1:
            return saiki(q, n-1) + a[n]
        elif t[n] == 2:
            return max([a[n],saiki(q, n-1)])
        elif t[n] == 3:
            return min([a[n],saiki(q, n-1)])

saiki(Q,N-1)
"""
def saiki(i, n):
    if n == 0:
        if t[n] == 1:
            return a[n] + x[i]
        if t[n] == 2:
            return max([a[n], x[i]])
        if t[n] == 3:
            return min([a[n], x[i]])
    else:
        if t[n] == 1:
            return saiki(i, n-1) + a[n]
        elif t[n] == 2:
            return max([a[n],saiki(i, n-1)])
        elif t[n] == 3:
            return min([a[n],saiki(i, n-1)])

for i in range(Q):
    print(saiki(i, N-1))
"""