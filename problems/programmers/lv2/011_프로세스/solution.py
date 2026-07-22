from collections import deque

def solution(priorities, location):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: priorities(각 프로세스의 우선순위 목록), location(추적할 프로세스의 초기 인덱스).
    - 반환값: 추적하는 프로세스가 몇 번째로 실행되는지(1부터)를 정수로 return 한다.
    """

    # 실행 대기 큐에 담긴 프로세스들을 규칙에 따라 처리
    # 1. 꺼낸 프로세스 보다 우선순위가 높은 프로세스가 큐에 하나라도 남아 있으면, 꺼낸 프로세스를 실행하지 않고 큐의 맨뒤로 보냄
    # 2. 대기 큐에 자신보다 우선순위가 높은 프로세스가 없으면 즉시 실행
    new_number_list = deque([(val, idx) for idx, val in enumerate(priorities)])
    cnt = 0
    while new_number_list:
        max_num = max(new_number_list, key=lambda x: x[0])[0]
        data = new_number_list.popleft()
        # 값 비교 시 제일 큰 값일 경우
        if data[0] >= max_num:
            cnt += 1
            # 지정한 인덱스 값이 경우
            if data[1] == location:
                return cnt
        # 제일 큰 값이 아닐 경우 값 다시 삽입
        else:
            new_number_list.append(data)
# print(solution([1, 1, 9, 1, 1, 1],0))
