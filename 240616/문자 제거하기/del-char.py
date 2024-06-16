string=input()
s=list(string)

lens=len(s)
while 1:
    n=int(input())
    if lens<=n:
        s.pop(lens-1)
    else:
        s.pop(n)
    print(''.join(s))
    lens-=1
    
    if lens==1:
        break