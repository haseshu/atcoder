N = int(input())

d=list()
d.append(int(input()))

for i in range(N-1):
    d.append(int(input()))

d_sorted=sorted(d, reverse = True)
now = 1000
count = 0

#print(d_sorted)

for i in range(N):
#    print("{} = {}".format(i,d_sorted[i]))
    if d_sorted[i] < now :
        count += 1
        now = d_sorted[i]
  #      print(d[i])

print(count)