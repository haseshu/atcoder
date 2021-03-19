N, A, B = map(int, input().split())
count =0
for i in range(N+1):
    million = int(i / 10000)
    thousand = int((i - million * 10000) / 1000)
    hundred = int((i - million * 10000 - thousand * 1000) / 100)
    ten = int((i - million * 10000 - thousand * 1000 - hundred * 100) / 10)
    one = int(i % 10)
    #print(i)
    #print("{}{}{}{}{}".format(million, thousand, hundred, ten, one))
    sum = million + thousand + hundred + ten + one
    if sum <= B and sum >= A:
        count = count +i

print(count)
