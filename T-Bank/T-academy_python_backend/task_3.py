a = [0]
len_s = int(input())
s = input().upper()

pos = 0

for i in range(1, len_s + 1):
    if s[i-1] == 'L':
        a.insert(pos, i)
    else:
        a.insert(pos+1, i)
        pos += 1

print(*a)