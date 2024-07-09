num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1,d1,m2,d2 = map(int,input().split())

dd1=sum(num_of_days[:m1])+d1
dd2=sum(num_of_days[:m2])+d2

print(dd2-dd1+1)