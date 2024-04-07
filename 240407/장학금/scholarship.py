arr = input().split()

mid = int(arr[0])
fin = int(arr[1])

if mid >=90:
    if fin>=95:
        print(100000)
    elif fin>=90:
        print(50000)
else :
    print(0)