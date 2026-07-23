def solution(people, limit):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자:
        people (list[int]) : 각 사람의 몸무게 목록.
        limit  (int)       : 보트 한 대의 무게 제한.
    - 반환값: 모든 사람을 구출하는 데 필요한 보트 개수의 최솟값(int)을 return 한다.
    """
    sorted_people = sorted(people, reverse=True)
    shipped_count = 0

    while sorted_people:
        if len(sorted_people) > 1 and (sorted_people[0] + sorted_people[-1]) <= limit:
            shipped_count += 1
            sorted_people.pop(0)
            sorted_people.pop(-1)
        else:
            shipped_count += 1
            sorted_people.pop(0)
    return shipped_count

