N = int(input())

#10^15 =100,000,000,000,000なので、max4つ
#1,000以上1,000,000未満の数×1
#1,000,000以上、1,000,000,000未満の数×2
#1,000,000,000以上、1,000,000,000,000未満の数×3
#1,000,000,000,000以上の数×4
thousand = 1000
million = 1000000
billion = 1000000000
trillion = 1000000000000
count = 0
if N >= trillion:
    count = count + (N - trillion +1)
if N >= billion:
    count = count + (N - billion +1)
if N >= million:
    count = count + (N - million +1)
if N >= thousand:
    count = count + (N - thousand +1)
print(count)

