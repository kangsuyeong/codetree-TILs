string = input()

new=[]

for i in range(len(string)):
    if i%2!=0:
        new.append(string[i])

for elem in new[::-1]:
    print(elem,end="")