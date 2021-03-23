N = int(input())
T=[]
X=[]
Y=[]
for i in range(N):
    a,b,c=list(map(int,input().split()))
    T.append(a)
    X.append(b)
    Y.append(c)

t, x, y =0, 0, 0
have_route =True
for i in range(len(T)):
#    for j in range(T[i]):
#    print("{}={},{},{}".format(i,t,x,y))
    subt = T[i] - t
    subx = X[i] - x
    suby = Y[i] - y
#    print("{},{},{}".format(T[i],X[i],Y[i]))
    length = abs(subx) + abs(suby)
    if (subt - length) % 2 ==0 and subt >= length:
        #T[i]の地点にはいける。
#        print("{} is OK".format(i))
        t = T[i]
        x = X[i]
        y = Y[i]
    else:
        have_route=False
        break
if have_route:
    print("YES")
else:
    print("NO")