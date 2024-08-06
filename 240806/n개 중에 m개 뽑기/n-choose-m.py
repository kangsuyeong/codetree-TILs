# n=4
# m=2
# answer=[]

# def choose(curr_num,one):
#     if curr_num==n+1:
#         if one==m:
#             print(*answer,sep="")
#         return
    
#     answer.append(0)
#     choose(curr_num+1,one)
#     answer.pop()

#     if one <m:
#         answer.append(1)
#         choose(curr_num+1,one+1)
#         answer.pop()

# choose(1,0)

N,M = map(int,input().split())
answer=[]
def choose(curr_num):
    if curr_num==M+1:
        print(*answer,sep=" ")
        return
    
    for i in range(1,N+1):
        if curr_num==1 or i>answer[-1]:
            answer.append(i)
            choose(curr_num+1)
            answer.pop()

choose(1)