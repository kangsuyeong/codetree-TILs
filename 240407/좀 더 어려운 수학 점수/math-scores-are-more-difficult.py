A=input().split()
A_math = int(A[0])
A_english = int(A[1])

B=input().split()
B_math = int(B[0])
B_english = int(B[1])

if A_math>B_math or(A_math==B_math and A_english>B_english):
    print("A")
else :
    print("B")