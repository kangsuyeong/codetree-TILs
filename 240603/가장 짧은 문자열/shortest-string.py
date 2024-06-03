string1=input()
string2=input()
string3=input()

len1=len(string1)
len2=len(string2)
len3=len(string3)

maxNum = max(len1,len2,len3)
minNum = min(len1,len2,len3)

print(maxNum-minNum)