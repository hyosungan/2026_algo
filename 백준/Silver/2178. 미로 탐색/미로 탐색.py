import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())

arr=[list(map(int,input().rstrip())) for _ in range(n)]
q=deque()

visited=[[0]*m for _ in range(n)]

visited[0][0]=1
q.append((0,0))

while q:
    cx,cy=q.popleft()
    if cx==n-1 and cy==m-1:
        break
    for dx,dy in zip([0,0,1,-1],[1,-1,0,0]):
        nx,ny=dx+cx,dy+cy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny]=visited[cx][cy]+1
            q.append((nx,ny))

print(visited[n-1][m-1])