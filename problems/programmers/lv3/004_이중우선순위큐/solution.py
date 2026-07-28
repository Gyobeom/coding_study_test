import heapq
from collections import defaultdict

def solution(operations):
    """명령을 모두 처리한 뒤 [최댓값, 최솟값]을 반환한다.

    - operations: 명령어 문자열 리스트. 각 원소는 "I n" / "D 1" / "D -1".
    - 반환: [최댓값, 최솟값] (int 2개짜리 리스트). 큐가 비면 [0, 0].
    - print 가 아니라 return 으로 돌려준다.
    """

    # 두가지 삭제 연산 큰값 삭제, 작은 값 삭제
    # 명령어 배열 n 정수|음수 삽입, 1 최댓값 삭제. -1 최솟값 삭제
    # 명령대로 처리한 후 큐에 남아있는 원소중 최댓값, 최솟값을 반환 하시오.
    # 큐가 비어 있으면 0,0 반환

    # 조건
    # 삭제 명령이 주어졌을 때 큐가 비어있으면 명령 무시
    # 모든 값에 2,000,000,000 을 더하면 전부 다 0 이상이 됨
    # 최솟값, 최댓값 관리를 하기 위해서 별도의 큐 카운트를 보유해야 할 것으로 보임.

    asc_number_list = []
    desc_number_list = []
    asc_deleted_dict = defaultdict(int)
    desc_deleted_dict = defaultdict(int)
    insert_number_count = 0
    standard_number = 20000000001

    # 배열에서 값 추출 할 때
    def extract_number(type):
        while True:
            if type == 'asc':
                if asc_number_list:
                    pop_number = heapq.heappop(asc_number_list)
                    # 최솟 값 배열에서 빼고, 만약 이미 최댓값에서 뺀 수라면, 제거 후 다시 뽑음
                    if desc_deleted_dict[pop_number] != 0:
                        desc_deleted_dict[pop_number] -= 1
                    # 신규로 등장한 최솟값 뺴야 한다면, 최댓값 배열에서 뺄 수 있도록 사전 추가
                    else:
                        return pop_number
                else:
                    return 0
            elif type == 'desc':
                if desc_number_list:
                    pop_number = heapq.heappop(desc_number_list)
                    # 최댓 값 배열에서 빼고, 만약 이미 최솟값에서 뺀 수라면, 제거 후 다시 뽑음
                    if asc_deleted_dict[pop_number] != 0:
                        asc_deleted_dict[pop_number] -= 1
                    # 신규로 등장한 최댓값 뺄 때, 최소 값 배열에서 뺄 수 있도록 사전 추가
                    else:
                        return pop_number
                else:
                    return 0

    for operation in operations:
        operate, number = operation.split()
        if operate == 'I':
            number = int(number) + standard_number
            heapq.heappush(asc_number_list, number)
            heapq.heappush(desc_number_list,-number)
            insert_number_count += 1
        else:
            # 아무것도 배열에 없을 때
            if insert_number_count == 0:
                continue
            else:
                # 최솟값 빼야 할 때,
                if number == '-1':
                    extracted_number = extract_number('asc')
                    asc_deleted_dict[-extracted_number] += 1
                    insert_number_count -= 1
                # 최댓값 빼야 할 때
                else:
                    extracted_number = extract_number('desc')
                    desc_deleted_dict[-extracted_number] += 1
                    insert_number_count -= 1

    min_number = 0
    max_number = 0


    # 최솟 값 배열에 값이 존재할 때 최종 정리
    if asc_number_list:
        extracted_number = extract_number('asc')
        if extracted_number != 0:
            min_number = extracted_number - standard_number
        else:
            min_number = extracted_number

    # 최댓 값 배열에 값이 존재할 때 최종 정리
    if desc_number_list:
        extracted_number = extract_number('desc')
        if extracted_number != 0:
            max_number = extracted_number + standard_number
        else:
            max_number = extracted_number

    if insert_number_count > 0:
        return[-max_number,min_number]

    if len(asc_number_list) == 0 and len(desc_number_list) == 0:
        return [0, 0]
