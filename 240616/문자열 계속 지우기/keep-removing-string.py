A=input()
B=input()


while True:
    target = A.find(B)
    if target != -1:
        A=A[:target] + A[target+len(B):]
    else :
        break;

print(A)