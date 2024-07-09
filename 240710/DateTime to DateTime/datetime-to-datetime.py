a,b,c = map(int,input().split())

m1 = 11*60*24+11*60+11
m2 = a*60*24 + b*60 + c

print(m2-m1)