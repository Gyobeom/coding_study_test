import heapq
from collections import defaultdict

def solution(operations):
    asc_number_heapq = []
    desc_number_heapq = []
    asc_delete_dict = defaultdict(int)
    desc_delete_dict = defaultdict(int)
    input_count = 0
    standard_num = 2000000001

    def pop_number(kind):
        if kind == 'asc':
            while True:
                if asc_number_heapq:
                    popped_number = heapq.heappop(asc_number_heapq)
                    if desc_delete_dict[popped_number] > 0:
                        desc_delete_dict[popped_number] -= 1
                    else:
                        return popped_number
                else:
                    return 0
        else:
            while True:
                if desc_number_heapq:
                    popped_number = heapq.heappop(desc_number_heapq)
                    if asc_delete_dict[popped_number] > 0:
                        asc_delete_dict[popped_number] -= 1
                    else:
                        return popped_number
                else:
                    return 0


    for i in range(len(operations)):
        operate, number = operations[i].split()
        # 신규 삽입
        if operate == 'I':
            heapq.heappush(asc_number_heapq, int(number) + standard_num)
            heapq.heappush(desc_number_heapq, -(int(number) + standard_num))
            input_count += 1
        else:
            if input_count == 0:
                continue
            else:
                # 최솟값 제거
                if number == '-1':
                    popped_number = pop_number('asc')
                    asc_delete_dict[-popped_number] += 1
                else:
                    popped_number = pop_number('desc')
                    desc_delete_dict[-popped_number] += 1
            input_count -= 1


    # 최솟값, 최댓값 배열에서 각자 뺀 나머지들 제거 후 최종적으로 반환 진행 필요
    # 삽입된 카운트가 있을 경우에만 없으면 0,0 반환
    if input_count > 0:
        min_number = pop_number('asc')
        max_number = pop_number('desc')
        if min_number != 0:
            min_number = min_number - standard_num
        if max_number != 0:
            max_number = -max_number -  standard_num
        return [max_number, min_number]
    else:
        return [0,0]
