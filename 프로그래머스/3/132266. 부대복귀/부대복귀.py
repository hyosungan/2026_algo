import heapq,sys

def solution(n, roads, sources, destination):
    link=[[] for _ in range(n+1)]
    for a,b in roads:
        link[a].append(b)
        link[b].append(a)
    
    pq=[]
    INT_MAX=sys.maxsize
    dist=[INT_MAX]*(n+1)
    dist[destination]=0
    heapq.heappush(pq,(0,destination)) #cost,x
    
    while pq:
        cost,x=heapq.heappop(pq)
        if dist[x]!=cost:
            continue
        
        for next in link[x]:
            if dist[next]>cost+1:
                dist[next]=cost+1
                heapq.heappush(pq,(cost+1,next))
    ans=[]
    for s in sources:
        if dist[s]==INT_MAX:
            ans.append(-1)
        else:
            ans.append(dist[s])
    
    return ans