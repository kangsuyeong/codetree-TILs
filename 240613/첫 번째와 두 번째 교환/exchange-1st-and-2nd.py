s=input()
list_s = list(s)

s1=list_s[0]
s2=list_s[1]

for i in range(len(list_s)):
    if list_s[i] == s1:
        list_s[i]=s2
    elif list_s[i] ==s2:
        list_s[i]=s1

s3=''.join(list_s)
print(s3)