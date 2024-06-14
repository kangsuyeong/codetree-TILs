first_input = input().split()
first_input[1] = int(first_input[1])
s=list(first_input[0])

second_input = [input().split() for _ in range(first_input[1])]


for elem in second_input:
    if elem[0]=='1':
        elem[1]=int(elem[1])
        elem[2]=int(elem[2])
        s[elem[1]-1],s[elem[2]-1]=s[elem[2]-1],s[elem[1]-1]
        print(''.join(s))
    elif elem[0]=='2':
        for i in range(len(s)):
            if s[i]==elem[1]:
                s[i]=elem[2]
        print(''.join(s))