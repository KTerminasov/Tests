s = input()
a_before = 0
c_after = s.count('c')
res = 0

for letter in s:
    if letter == 'a':
        a_before += 1
    elif letter == 'b':
        res += a_before * c_after
    elif letter == 'c':
        c_after -= 1

print(res)
