s=input()
list_s = list(s)

s1=list_s[0]
s2=list_s[1]

list_s[0]=s2
list_s[1]=s1

for i in range(2,len(list_s)):
    if list_s[i] == s1:
        list_s[i] = s2

s3=''.join(list_s)
print(s3)