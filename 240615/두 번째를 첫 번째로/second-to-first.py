string = input()

s = list(string)

target=s[1]
for i in range(len(s)):
    if s[i] ==target:
        s[i] =s[0]

print(''.join(s))