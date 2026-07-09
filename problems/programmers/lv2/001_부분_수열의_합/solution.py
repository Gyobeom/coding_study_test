

def solution(nums, target):
    n = len(nums)
    answer = 0

    def dfs(i, cur_sum):
        nonlocal answer
        if i == n:
            if cur_sum == target:
                  answer += 1
            # TODO: cur_sum이 target이면 answer 증가
            #  (주의) 공집합은 세지 않지만, target>=1 이라 빈 조합 합은 0 → 자동 제외됨
            return
        # TODO ①: i번째를 고르는 경우로 재귀
        dfs(i + 1, cur_sum + nums[i])
        # TODO ②: i번째를 안 고르는 경우로 재귀
        dfs(i + 1, cur_sum)

    dfs(0, 0)
    return answer

print(solution([1,2,3,4,5,6,7],8))  # 정답 (1,2,6), (1,3,4), (1,7), (3,5)