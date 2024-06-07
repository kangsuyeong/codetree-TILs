arr=[input() for _ in range(10)]
n = input()

notfind = False
for elem in arr:
    if n==elem[len(elem)-1]:
        print(elem)
        notfind=True

if notfind == False:
    print("None")