n=int(input())
answer=[]
visited=[False]*(n+1)

def choose(curr_num):
    if curr_num==n+1:
        print(*answer,sep=" ")
        return
    
    # 순열돌기
    for i in range(1,n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)

        choose(curr_num+1)
        
        visited[i]=False
        answer.pop()
        
        

choose(1)