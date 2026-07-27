import heapq

def solution(scoville, K):
    """모든 스코빌 지수를 K 이상으로 만드는 최소 섞기 횟수를 반환한다.

    - scoville: 각 음식의 스코빌 지수 리스트 (길이 2 이상).
    - K: 목표 스코빌 지수 (정수).
    - 반환: 최소 섞기 횟수(int). 불가능하면 -1, 이미 모두 K 이상이면 0.
    - print 가 아니라 return 으로 돌려준다.
    """

    # 이미 존재하는 배열에서, 최소,두번째 최소를 계속 꺼내서 신규 만듬
    # 조건 - K 이상으로 반복.
    # K 이상으로 만들 수 없을 경우 -1 반환 가능할 경우 최소 횟수 반환

    # 배열 heaqp으로 변경
    heapq.heapify(scoville)
    count = 0

    while len(scoville) > 1:
        if scoville[0] >= K:
            break

        first_min_food = heapq.heappop(scoville)
        second_min_food = heapq.heappop(scoville)

        new_food_scoville = first_min_food + (second_min_food * 2)
        heapq.heappush(scoville,new_food_scoville)
        count += 1

    # 마지막 남은 스코빌 지수가 결국에는 목표 값보다 작을 때
    if scoville[0] < K:
        return -1
    # 최종적으로 카운트 반환
    else:
        return count

# print(solution([5, 5, 5, 5], 10))
