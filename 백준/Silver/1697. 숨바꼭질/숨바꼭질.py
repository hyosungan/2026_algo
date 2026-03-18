import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().split())

if K<=N:
    print(N-K)
    exit()
else: #N<K
    q=deque()
    visited=[-1]*(2*K)
    q.append(N)
    visited[N]=0
    while q:
        now=q.popleft()
        if now==K:
            print(visited[K])
            break
        else:
            one,two,three=now-1,now+1,now*2
            if 0<=one<(2*K) and visited[one]==-1:
                q.append(one)
                visited[one]=visited[now]+1
            if 0<=two<(2*K) and visited[two]==-1:
                q.append(two)
                visited[two]=visited[now]+1
            if 0<=three<(2*K) and visited[three]==-1:
                q.append(three)
                visited[three]=visited[now]+1

 