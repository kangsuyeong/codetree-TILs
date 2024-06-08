string = input()

Encoding=""
target = string[0]
cnt=1

for elem in string[1:]:
    if target == elem:
        cnt+=1
    else :
        Encoding+=target
        Encoding+=str(cnt)

        target=elem
        cnt=1
Encoding+=target
Encoding+=str(cnt)

print(len(Encoding))
print(Encoding)