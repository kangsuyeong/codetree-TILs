arr_2D = [input().split() for i in range(5)]

for i in range(5):
    for j in range(3):
        arr_2D[i][j]=chr(ord(arr_2D[i][j])+ ord('A')-ord('a'))
        print(arr_2D[i][j],end=" ")
    print("")