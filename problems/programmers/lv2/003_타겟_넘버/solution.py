def solution(numbers, target):
    """numbers의 각 원소 앞에 +/- 를 붙여 합이 target이 되는 방법의 수를 반환.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.

    힌트:
      dfs(i, cur) = "i번째 원소부터 부호를 정할 차례, 지금까지 누적합 cur"
        - i == n 이면 cur == target 여부로 성공/실패 판정
        - 그 외    이면 (+numbers[i]) 가지 와 (-numbers[i]) 가지 2갈래
      두 갈래 모두 i+1 로 진행할 것.
    """

    # dfs 재귀 함수로 풀도록 + / - 2개의 경우의 수로 진행. 더한 값을 매개변수로 전달
    answer = 0
    def dfs(i, tot):
      nonlocal answer
      if i == len(numbers) - 1:
        if tot == target:
          answer += 1
        return

      dfs(i + 1, tot + numbers[i+1])
      dfs(i + 1, tot - numbers[i+1])
    dfs(-1,0)
    return answer
# print(solution([4, 1, 2, 1],2))
