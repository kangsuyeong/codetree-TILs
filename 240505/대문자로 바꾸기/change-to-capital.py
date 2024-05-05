arr_2D = [input().split() for i in range(5)]

for i in range(5):
    for j in range(3):
        print(arr_2D[i][j].upper(),end=" ")
    print("")