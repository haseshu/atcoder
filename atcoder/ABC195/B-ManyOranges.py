A,B,W = list(map(int, input().split()))

W = W * 1000

min_num = int(W / B)
max_num = int(W / A)

count_min = 100000
count_max = 1
UNSATISFIABLE =True
#print("{} {}".format(min_num, max_num))
        
for i in range(1, W+1):
    if i * A <= W and i * B >= W:
        if count_min >= i:
            UNSATISFIABLE = False
        if count_max <= i:
            UNSATISFIABLE = False

        count_min = min(count_min, i)
        count_max = max(count_max, i)

if UNSATISFIABLE:
    print("UNSATISFIABLE")
else:
    print("{} {}".format(count_min, count_max))

"""
for i in range (max_num):
    if W - i * A == 0:
        if count_min > i:
            count_min = i
            UNSATISFIABLE =True
        if count_max < i:
            count_max = i
            UNSATISFIABLE =True
    elif W - i * A > A and W - i * A <= B:
"""
"""
def saiki (w, g):
    if w-g==0:
        return 1
    elif w - g >0:
        return saiki(w-g,g) + 1
    pass

for i in range(max_num):
    

if UNSATISFIABLE == True:
    print("UNSATISFIABLE")
else:
    print("{} {}".format(count_min, count_max))


"""