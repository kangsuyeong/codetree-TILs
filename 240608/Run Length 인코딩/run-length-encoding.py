string = input()
new=[]
cnt=1

for i in range(len(string)):
    if i == len(string)-1:
        new.append(string[i])
        new.append(cnt)
        break;

    if string[i] == string[i+1]:
        cnt+=1
    else:
        new.append(string[i])
        new.append(cnt)
        cnt=1

print(len(new))
for elem in new:
    print(elem,end="")