def solution(routes):
    routes.sort(key=lambda x: x[1])
    cnt=1
    flag=routes[0][1]
    for a,b in routes[1:]:
        if a<=flag<=b:
            continue
        else:
            cnt+=1
            flag=b
    return cnt