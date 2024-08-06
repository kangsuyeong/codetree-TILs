# # 재귀 함수 - 함수 정의
# # get_sum(n) : 1~ n 까지의 합을 반환하는 함수

# n=3
# answer=[]

# def choose(curr_num):
#     # 종료조건(초기값)
#     if curr_num == n+1:
#         print(*answer,sep="")
#         return
    
#     #다음 내용 호출

#     for i in range(3):
#         answer.append(i)
#         choose(curr_num+1)
#         answer.pop()




# choose(1)

# K,N= map(int,input().split())
# answer=[]

# # 첫 번째부터 curr_num-1까지 선택을 했고, curr_num번째 수를 이제 고를 차례
# def choose(curr_num):
#     # 종료 조건
#     if curr_num==N+1:
#         print(*answer,sep=" ")
#         return
#     # 다음 호출
#     for i in range(1,K+1):
#         answer.append(i)
#         choose(curr_num+1)
#         answer.pop()

# choose(1)


K,N=map(int,input().split())
answer=[]

def choose(curr_num):
    if curr_num==N+1:
        print(*answer,sep=" ")
        return
    
    for i in range(1,K+1):
        answer.append(i)
        choose(curr_num+1)
        answer.pop()

 

choose(1)