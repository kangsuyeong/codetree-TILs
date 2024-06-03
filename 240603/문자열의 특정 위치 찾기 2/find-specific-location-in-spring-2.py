arr=[ "apple", "banana", "grape", "blueberry", "orange"]

string1=input()
cnt=0
for elem in arr:
    if elem[2] ==string1 or elem[3]==string1:
        print(elem)
        cnt+=1
print(cnt)