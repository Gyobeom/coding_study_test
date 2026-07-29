import math
def solution(n, times):
    """모든 사람이 심사를 받는 데 걸리는 시간의 최솟값(분)을 반환한다.

    - n: 심사를 받아야 하는 사람 수 (int).
    - times: 각 심사관이 한 명을 심사하는 데 걸리는 시간 리스트.
    - 반환: 모든 사람 심사에 필요한 최소 시간(int).
    - print 가 아니라 return 으로 돌려준다.
    """
    # 단조성 성립 시간을 증가시키고, 각 심사관이 심사할 수 있는 시간으로 나누어서 최종적으로 반환 값과 일치하면 반환

    # 시간 정렬
    times.sort()
    left, right = 1, min(times) * n
    ans = right

    def check_spped(times, goal_time):
        return sum(math.ceil(goal_time // time) for time in times)

    while left <= right:
        mid = (left + right) // 2
        if check_spped(times,mid) >= n:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

print(solution(6,[7,10]))