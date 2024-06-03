string1=input()
string2=input()

cnt=0

for elem in string1:
    if elem == string2:
        cnt+=1

print(cnt)