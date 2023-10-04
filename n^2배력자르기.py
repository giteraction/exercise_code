def solution(n, left, right):
    answer = []
    for nn in range(n):
        for j in range(n): 
            answer.append(max(nn,j)+1)
    return answer[left:right+1]
