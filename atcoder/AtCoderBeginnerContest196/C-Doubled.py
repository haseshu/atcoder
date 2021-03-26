N = int(input())

def fact(x , y):
    if y == 0:
        return 1
    else:
        return x * fact(x, y-1)

if N<10:
    print(0)
else:
    digit = len(str(N))
    #print("digit ={}".format(digit))
    be_odd = False
    if (digit % 2 ==1):
        digit = digit -1
        be_odd = True
        #print("be_odd")
    digit_half = int(digit/2)
#print(digit_half)
#print(str(N))
#print(str(N)[:digit_half])
    N_before_half = int(str(N)[:digit_half])
    N_after_half = int(str(N)[digit_half:])
    if be_odd:
        N_before_half = fact(10, len(str(N)[:digit_half]))-1
    else:
        if N_before_half > N_after_half:
            N_before_half = N_before_half -1
#print(N_before_half)
#print(N_after_half)


#1000 : digit = 4,
#10000000 :digit =8,

    print(N_before_half)