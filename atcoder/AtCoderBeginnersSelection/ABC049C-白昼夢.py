import re

S = input()
T_type =["dream", "dreamer", "erase", "eraser"]
T=""
S_now = S
can_match = True
while can_match == True:
    can_match = False
#    print(S_now[-5:])
#    print(S_now[-7:])
    if S_now[-5:]=="dream":
        S_now = S_now[:-5]
        can_match = True
#        print(S_now +","+"dream")
    if S_now[-7:]=="dreamer":
        S_now = S_now[:-7]
        can_match = True
#        print(S_now +","+"dreamer")
    if S_now[-5:]=="erase":
        S_now = S_now[:-5]
        can_match = True
#        print(S_now +","+"erase")
    if S_now[-6:]=="eraser":
        S_now = S_now[:-6]
        can_match = True
#        print(S_now +","+"eraser")


if S_now == "":
    print("YES")
else:
    print("NO")