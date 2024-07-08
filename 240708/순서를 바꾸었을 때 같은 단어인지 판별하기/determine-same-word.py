A=list(input())
B=list(input())
A.sort()
B.sort()
if ''.join(A) == ''.join(B):
    print("Yes")
else :
    print("No")