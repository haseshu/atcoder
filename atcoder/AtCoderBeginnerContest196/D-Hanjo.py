#tatamiが複製されず、同じものになっている。
#複製するようにする
H, W, A, B = map(int, input().split())

ans = 0

def dfs(i, j, tatami, A, B):
#    print("({},{},{},{})".format(i,j,A,B))
#    print(tatami)
    kekka = True
    for k in range(H):
        #print("{},{}".format(k,tatami[k]))
        if 0 in tatami[k]:
            #print("False")
            kekka = False
    if kekka == True:
        global ans
        ans += 1
#        print(tatami)
#        print("True")
        return 1
    if j >= W:
#        print("end")
        return 0
    if i >= H:
        t = [row[:] for row in tatami]
        dfs(0, j+1, t, A, B)
    
    #print("({},{},{},{})".format(i,j,A,B))
    if j < W and i < H:
        if tatami[i][j] !=0:
            t = [row[:] for row in tatami]
            dfs(i+1, j, t, A, B)
        else:
            for k in range(3):
                #print("k={}".format(k))
                #print("({},{},{},{})".format(i,j,A,B))
                if k == 0 and B != 0:
                    t = [row[:] for row in tatami]
                    t[i][j] = 1
                    #print("{} = tatami".format(id(tatami)))
                    #print("{} = t".format(id(t)))
                    dfs(i+1, j, t, A, B -1)
                elif k ==1 and A != 0:
                    if i+1 < H and tatami[i+1][j] == 0:
                        t = [row[:] for row in tatami]
                        t[i][j] = 2
                        t[i+1][j] = 2
                        
                        dfs(i+2, j, t, A - 1, B)
                elif k == 2 and A != 0:
                    #print("({},{},{},{})".format(i,j,A,B))
                    if j+1 < W and tatami[i][j+1] == 0:
                        t = [row[:] for row in tatami]
                        t[i][j] = 3
                        t[i][j+1] = 3
                        dfs(i+1, j, t, A - 1, B)

tatami_map=[[0 for i in range(W)] for j in range(H)]
#tatami_map=[0 for i in range(H)] * W
#print(tatami_map)
dfs(0,0, tatami_map, A, B)
print(ans)


##自力回答ではないので、中身を理解すること。

"""
ans = 0
def dfs(i, bit, A, B):
    print("bit = {}, i = {}".format(bit,i))
    if i == H * W:
        global ans
        ans += 1
        return
    if bit >> i & 1:
        dfs(i + 1, bit, A, B)
        return
    if B:
        dfs(i + 1, bit | 1 << i, A, B - 1)
    if A:
        if i % W != W - 1 and not bit & 1 << (i + 1):
            dfs(i + 1, bit | 1 << i | 1 << (i + 1), A - 1, B)
        if i + W < H * W:
            dfs(i + 1, bit | 1 << i | 1 << (i + W), A - 1, B)
dfs(0, 0, A, B)
print(ans)
"""