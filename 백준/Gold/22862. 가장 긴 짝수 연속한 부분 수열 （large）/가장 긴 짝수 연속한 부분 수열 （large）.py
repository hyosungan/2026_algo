import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

count = 0     # 짝수 개수 (현재 길이)
delete = 0    # 홀수 개수 (삭제한 횟수)
ans = 0
s = 0

# e는 for문으로 무조건 1칸씩 전진 (복잡한 if/else 제거)
for e in range(N):
    if arr[e] % 2 == 0: # 짝수 만남
        count += 1
    else:               # 홀수 만남
        delete += 1
    
    # [중요] 삭제 횟수가 K를 초과하면, 정상 범위가 될 때까지 s를 당김
    while delete > K:
        if arr[s] % 2 == 0: # 나가는 놈이 짝수면
            count -= 1
        else:               # 나가는 놈이 홀수면
            delete -= 1
        s += 1

    # 여기까지 왔으면 조건(delete <= K)을 만족하는 상태임
    ans = max(ans, count)

print(ans)