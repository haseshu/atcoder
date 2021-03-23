N = int(input())
T=[]
X=[]
Y=[]
T.append(0)
X.append(0)
Y.append(0)
for i in range(N):
    a,b,c=list(map(int,input().split()))
    T.append(a)
    X.append(b)
    Y.append(c)

#print("{},{},{}".format(T,X,Y))
have_route =True
for i in range(1,N+1):
#    for j in range(T[i]):
#    print("{}={},{},{}".format(i,t,x,y))
    subt = T[i] - T[i-1]
    subx = X[i] - X[i-1]
    suby = Y[i] - Y[i-1]
#    print("{},{},{}".format(T[i],X[i],Y[i]))
    length = abs(subx) + abs(suby)
    if (subt % 2 != length % 2) or (subt < length):
        have_route = False
if have_route is True:
    print("YES")
else:
    print("NO")