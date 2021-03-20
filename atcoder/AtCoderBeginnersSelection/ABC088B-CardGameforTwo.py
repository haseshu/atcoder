N = int(input())
A = list(map(int, input().split()))

Alice = 0
Bob = 0

A_sorted = sorted(A, reverse = True)
#print(A_sorted)
for i in range(N):
    if i % 2 is 0:
        Alice = Alice + A_sorted.pop(0)
    else:
        Bob += A_sorted.pop(0)
#print(Alice)
#print(Bob)
print(Alice - Bob)