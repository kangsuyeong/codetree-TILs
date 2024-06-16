string = input()

s = list(string)

s.pop(1)
s.pop(len(s)-2)
print(''.join(s))