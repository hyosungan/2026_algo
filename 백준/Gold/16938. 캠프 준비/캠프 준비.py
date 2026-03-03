import sys
input = sys.stdin.readline

N,L,R,X = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
INF = 10**9

def dfs(i, cnt, s, mn, mx):
    global ans

    # 가지치기: 합이 이미 R 넘으면 더 볼 필요 없음 (난이도는 양수라 더 커지기만 함)
    if s > R:
        return

    if i == N:
        if cnt >= 2 and mx - mn >= X and L <= s <= R:
            ans += 1
        return

    # 선택
    v = arr[i]
    if cnt == 0:
        dfs(i+1, 1, s+v, v, v)
    else:
        dfs(i+1, cnt+1, s+v, mn if mn < v else v, mx if mx > v else v)

    # 미선택
    dfs(i+1, cnt, s, mn, mx)

dfs(0, 0, 0, INF, -INF)
print(ans)