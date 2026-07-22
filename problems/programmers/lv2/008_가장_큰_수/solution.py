def solution(numbers):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: numbers(0 이상의 정수 배열).
    - 반환값: 이어 붙여 만들 수 있는 가장 큰 수를 문자열로 return 한다.
    """

    # 양의 점수가 담긴 배열 존재 이 정수들을 순서만 바꿔 이어붙였을 때, 가장 큰수를 구해야함.

    new_numbers = sorted(
        numbers,
        key=lambda x:(str(x) * 3),reverse=True)
    result = "".join(map(str,new_numbers))
    if int(result) <= 0:
        return '0'
    else:
        return str(result)

# print(solution([6,10,2]))
