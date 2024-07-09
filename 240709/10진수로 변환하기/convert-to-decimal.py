# n=list(map(int,input()))

# num=0
# for i in range(len(n)):
#     num=num*2 + n[i]

# print(num)

S=input()
num=0
for digit in S:
    num=num*2+int(digit)
print(num)