def rotate(stamp):
    rotate_stamp = [[0 for _ in range(len(stamp[i]))] for i in range(len(stamp))]
    for j in range(len(stamp)):
        for i in range(len(stamp[j])):
            rotate_stamp[j][i] = stamp[len(stamp[j])-1-i][j]

    return rotate_stamp


def sum(stamp, stamp2):
    new = [[0 for _ in range(len(stamp[i]))] for i in range(len(stamp))]
    for j in range(len(stamp)):
        for i in range(len(stamp[j])):
            new[j][i] = stamp[j][i] + stamp2[j][i]

    return new


def solution(stamp, times):
    
    result = [[0 for _ in range(len(stamp[i]))] for i in range(len(stamp))]
    result = sum(result, stamp)

    for N in range(times):
        stamp = rotate(stamp)
        result = sum(result, stamp)

        # 회전 하는 동안 결과 보기
        print(N+1, '번 회전 현재 스템프 모양')
        for i in range(len(stamp)):
            print(stamp[i])
        print(N+1, '번 회전 결과')
        for i in range(len(stamp)):
            print(result[i])
        print(N+1, '번 실행 완료')
        print()
        
    return result


stamp = [
[1,1,1,2],
[2,0,0,0],
[1,1,1,1],
[0,0,0,0]
]

times = 3

print(solution(stamp, times))


# 풀이95-2

N = int(input())
stamp = []
for i in range(N):
    stamp.append(list(map(int,input().split(' '))))
k = int(input())

def solution2(stamp,n):
    N = len(stamp)
    # 0으로 만들어진 배열 생성 
    # [[0]*N]*N으로 하면 안됨!!!!
    p = [[0] * N for _ in range(N)]
    
    # 회전시키기 전 최초 1번찍어주기
    p = sum_matrix(p,stamp)
    #회전시키며 도장찍기
    for _ in range(n):
        stamp = rotate2(stamp)
        p=sum_matrix(p,stamp)
    return p

#배열(도장) 회전시키기
def rotate2(stamp):
    N = len(stamp)
    rot = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            rot[j][N-1-i] = stamp[i][j]
    return rot

#행렬 더하기 즉 도장이 찍히는 정도를 더한다.
def sum_matrix(p,stamp):
    for i in range(len(p)):
        for j in range(len(p[0])):
            p[i][j] = p[i][j]+stamp[i][j]
    return p

print(solution2(stamp,k))
