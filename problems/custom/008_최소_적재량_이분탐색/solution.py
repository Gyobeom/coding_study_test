def solution(weights, D):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - weights: 물건 무게 배열(순서 고정), D: 트럭 대수.
    - 물건을 순서대로 연속으로 담아 D대 이내로 모두 나를 수 있는
      최소 적재 용량을 return 한다.
    """

    # 최소 적재 용량
    max_val = sum(weights)
    min_val = max(weights)

    def count_truck(mid):
      cnt = 0
      sum_val = 0
      for weight in weights:
        if sum_val + weight > mid:
          cnt += 1
          sum_val = weight
        else:
          if cnt == 0:
            cnt += 1
          sum_val += weight
      return cnt

    while min_val < max_val:
      mid = (max_val + min_val) // 2
      truck_cnt = count_truck(mid)
      if truck_cnt <= D:
        max_val = mid
      else:
        min_val = mid + 1
    return min_val