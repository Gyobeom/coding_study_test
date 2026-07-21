from collections import Counter
def solution(clothes):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: clothes(각 원소가 [의상 이름, 의상 종류]인 2차원 리스트).
    - 반환값: 서로 다른 옷의 조합으로 입을 수 있는 경우의 수(정수)를 return 한다.
    """

    # 경우의 수 조합 해야함.
    # 각각의 종류만 입는 경우, 모든 종류를 다 입는 경우
    # 종류 별 의상을 배열 형태로 분류 해야함.

    cloth_counter = Counter([kind for name, kind in clothes])

    answer = 1

    for count in cloth_counter.values():
        answer *= (count + 1)

    return answer - 1
