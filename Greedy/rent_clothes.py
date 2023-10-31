#n명의 학생이 lost배열의 학생들에게 옷을 빌려줌 단 reserve배열의 학생들만 자신의 값 +-1 의 학생들에게만 빌려 줄 수 있음
def solution(n, lost, reserve):
    count = 0
    student = list(range(1,n+1))
    lost_reserve = list(set(lost) & set(reserve))
    for l in lost:
        if l not in lost_reserve:
            student.remove(l)
    print('student:',student)
    
    for lr in lost_reserve:
        reserve.remove(lr)
    print('r:',reserve)
    print('l:',lost)
    for l in lost:
        for r in reserve:
            if l == r+1 or l == r-1:
                if l not in student:
                    student.append(l)
                    count += 1
        if count == len(reserve):
            break
        
    print(student)
    return len(set(student))