import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

# 가장 먼 노드랑 거리 찾는 DFS
def dfs(start):
    visited = [False] * (n + 1)
    max_dist = 0
    far_node = start

    def go(cur, dist):
        nonlocal max_dist, far_node

        # 여기서 계속 최대 갱신
        if dist > max_dist:
            max_dist = dist
            far_node = cur

        for nxt, w in tree[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                go(nxt, dist + w)

    visited[start] = True
    go(start, 0)
    return far_node, max_dist


a, _ = dfs(1)

b, diameter = dfs(a)

print(diameter)
