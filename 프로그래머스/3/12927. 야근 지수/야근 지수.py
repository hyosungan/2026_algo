import heapq
def solution(n, works):
    answer = 0
    pq=[]
    for i in range(len(works)):
        heapq.heappush(pq,-works[i])
    
    while pq:
        if n<=0:
            break
        a=heapq.heappop(pq)
        if -a-1>0:
            heapq.heappush(pq,-(-a-1))
        
        n-=1
    ans=0
    for i in pq:
        ans+=(i*i)
        
    
    return ans