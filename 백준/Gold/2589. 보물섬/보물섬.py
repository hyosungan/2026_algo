from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(N)]
q=deque()
visited=[[-1]*M for _ in range(N)]
ans=-1

def bfs():
    global ans
    while q:
        x,y=q.popleft()
        for dx,dy in zip([1,-1,0,0],[0,0,-1,1]):
            nx,ny=dx+x,dy+y
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==-1 and arr[nx][ny]=='L':
                visited[nx][ny]=visited[x][y]+1
                ans=max(ans,visited[nx][ny])
                q.append((nx,ny))


for i in range(N):
    for j in range(M):
        if arr[i][j]=="L":
            visited[i][j]+=1
            q.append((i,j))
            bfs()
            visited=[[-1]*M for _ in range(N)]

print(ans)

