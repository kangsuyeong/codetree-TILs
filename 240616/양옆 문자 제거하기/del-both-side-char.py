string = input()

s = list(string)

s.pop(2)
s.pop(len(s)-2)
print(''.join(s))