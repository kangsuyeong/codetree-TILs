A = input().split()
A_age = int(A[0])
A_sex = A[1]

B = input().split()
B_age = int(B[0])
B_sex = B[1]

if (A_sex=="M" and A_age>=19) or (B_sex=="M" and B_age>=19):
    print(1)
else :
    print(0)