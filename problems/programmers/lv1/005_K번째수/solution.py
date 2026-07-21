def solution(array, commands):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: array(정수 배열), commands([i, j, k] 명령들의 배열).
    - 반환값: 각 명령의 결과 값을 commands 순서대로 담은 리스트를 return 한다.
    """
    result = []
    for command in commands:
        # i ~ j 배열로 slice
        new_arr = []
        if command[0] == command[1]:
            new_arr.append(array[command[0] - 1])
        else:
            new_arr = array[command[0] - 1 : command[1]]
        # 오름 차순 정렬
        new_arr.sort()
        result.append(new_arr[command[2]-1])
    return result
# solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])