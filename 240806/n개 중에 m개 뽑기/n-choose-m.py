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

#0 혹은 1로 채울건데,
# 첫번째 부터 curr_num-1번째까지 이미 채운 상태에서 ...
# curr_num번째를 채울거고
# 지금 상태는 1의 개수가 one_cnt인 상황
def choose(curr_num,one_cnt):
    # 종료 조건
    if curr_num==N+1:
        if one_cnt == M:
            print(*answer,sep=" ")
        return
    
    # 호출
    answer.append(curr_num)
    choose(curr_num+1,one_cnt+1)
    answer.pop()

  
    choose(curr_num+1,one_cnt)
    



choose(1,0)