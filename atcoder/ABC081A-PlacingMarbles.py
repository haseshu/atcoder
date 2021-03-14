s = input()
v = [s[i: i+3] for i in range(0, len(s), 3)]
#print(s[0],s[1],s[2])

print(int(s[0]) + int(s[1]) + int(s[2]))