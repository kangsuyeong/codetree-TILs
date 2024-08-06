# n=3
# answer = []

# def choose(curr_num):
#     if curr_num==n+1:
#         print(*answer)
#         return

#     # 첫 번째 값을 넣는 순간 이거나
#     # 이전 값이 0이 아닌 경우(1인 경우)
#     if curr_num == 1 or answer[-1]==1:
#         answer.append(0)
#         choose(curr_num+1)
#         answer.pop()

#     answer.append(1)
#     choose(curr_num+1)
#     answer.pop()

# choose(1)

K,N=map(int,input().split())
answer=[]

def choose(curr_num):
    if curr_num==N+1:
        print(*answer)
        return
    for i in range(1,K+1):
        # 
        if curr_num==1 or curr_num==2 or answer[-1]!=i or answer[-2]!=i:
            answer.append(i)
            choose(curr_num+1)
            answer.pop()

choose(1)