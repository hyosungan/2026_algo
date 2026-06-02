def solution(book_time):
    book_time.sort()
    length=len(book_time)
    visited=[0]*length
    ans=0
    for i in range(length):
        if visited[i]==0:
            ans+=1
            visited[i]=1
            e=book_time[i][1]
            temp=e.split(":")
            time=int(temp[0])*60+int(temp[1])+10
            for j in range(i+1,length):
                s=book_time[j][0]
                tmp=s.split(":")
                start=int(tmp[0])*60+int(tmp[1])
                if start>=time and visited[j] == 0:
                    visited[j]=1
                    a=book_time[j][1].split(":")
                    time=int(a[0])*60+int(a[1])+10
    return ans