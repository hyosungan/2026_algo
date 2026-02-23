import sys

input=sys.stdin.readline
N=int(input())

arr=[list(map(int,input().rstrip())) for _ in range(N)]

def divide(x,y,n):
    if n==1:
        print(arr[x][y],end="")
        return 
    
    check=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=check:
                print("(",end="")
                divide(x, y, n//2)                      # 왼쪽 위
                divide(x, y + n//2, n//2)               # 오른쪽 위
                divide(x + n//2, y, n//2)               # 왼쪽 아래
                divide(x + n//2, y + n//2, n//2)        # 오른쪽 아래
                print(")",end="")
                return
    
    print(arr[x][y],end="")
    

    
divide(0,0,N)
                