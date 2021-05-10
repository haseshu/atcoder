import copy
#W,Vを辞書に,Xを配列に入れる
#配列XからL～Rまでを削除する
#Xをソートする
#Vでソートして、Vが大きい方からWとXで比較して、最も小さいXに入れていく
#入ったVの合計を出力する

N,M,Q = list(map(int, input().split()))
WV = {}
LR = {}

for i in range(N):
    WV[i] = list(map(int, input().split()))
#入力確認
#print("N: {}".format(N))
#print("M: {}".format(M))
#print("Q: {}".format(Q))
#for i in range(N):
#    print("WV[{}] = {}".format(i, WV[i]))
#print(WV)

X = list(map(int, input().split()))
#入力確認
#print("X = {}".format(X) )

for i in range(Q):
    LR[i] = list(map(int, input().split()))
#入力確認
#for i in range(Q):
#    print("LR[{}] = {}".format(i, LR[i]))
#    print("LR[{}] = {},{}".format(i, LR[i][0],LR[i][1]))
#ここからコード

sorted_WV =sorted(WV.items(), key = lambda x:x[1][1],reverse=True)
#入力確認
#print("sorted_WV ={}".format(sorted_WV))
#print(sorted_WV[0][1][1])


for i in range (Q):
    Xi = copy.copy(X)
    #入力確認
    #print("Xi[{}:{}] = {}".format(LR[i][0],LR[i][1],Xi[LR[i][0] - 1 :LR[i][1]]))
    del Xi[LR[i][0] - 1 : LR[i][1]]
    Xi.sort()
    cost = 0
    sorted_WV_Is_ship =[False]*N
    Xi_Is_Full =[False]*len(Xi)
    length = 0
    length = len(Xi)
#    if N < len(Xi):
#        length = N
#    else:
#        length = len(Xi)

    #入力確認
    #print("LR = {}".format(LR[i]))
    #print("Xi = {}".format(Xi))
    #print(sorted_WV_Is_ship)
    #Vが大きい方からWとXで比較して、最も小さいXに入れていく
    for i in range(length):
        for j in range(N):
            if sorted_WV[j][1][0] <= Xi[i] and sorted_WV_Is_ship[j] is False and Xi_Is_Full[i] is False:
                cost = cost + sorted_WV[j][1][1]
    #            print(sorted_WV[j])
                sorted_WV_Is_ship[j] = True
                Xi_Is_Full[i] = True
    print(cost)


