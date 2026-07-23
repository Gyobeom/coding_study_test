def solution(n, lost, reserve):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자:
        n      (int)       : 전체 학생 수.
        lost   (list[int]) : 체육복을 도난당한 학생 번호 목록.
        reserve(list[int]) : 여벌 체육복을 가져온 학생 번호 목록.
    - 반환값: 체육 수업을 들을 수 있는 학생 수의 최댓값(int)을 return 한다.
    """

    # 학생들에거 1~n 번까지의 체육복 존재 * 일부 학생 체육복 도난
    # 여벌 체육복을 가져온 학생들은 바로 앞 번호 또는 바로 뒤 번호 학생 중 체육복이 없는 학생에게 빌려줄 수 있음

    # 조건
    # 한 학생은 자기 바로 앞 또는 바로 뒤 번호의 학생에게만 빌려줄 수 있음
    # 여벌을 가진 학생이 여러명에게 빌려줄 수 없음. 오로지 한명 한테만 빌려줄 수 있음
    # 여벌을 가져왔지만 자기 자신이 체육복을 도난당했을 경우 빌려줄 수 없음.

    # 결과
    # 체육 수업을 들을 수 있는 학생의 최대 값 반환

    # 먼저 reserve에 lost 값이 있는 확인 필요 (도난 당했지만 여벌 가져온 거 체크)
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)

    # 전체 반복문 순회 하면서 안가져온 배열에 값이 있는지 확인하고, 있다면,
    # reserve에서 +1,-1로 있는지 확인하고 있으면 reserve 값 없애고 카운트 증가

    cnt = n - len(new_lost)
    for i in range(1, n + 1):
        if i in new_lost:
            if i - 1 in new_reserve:
                new_reserve.discard(i - 1)
                cnt += 1
            elif i + 1 in new_reserve:
                new_reserve.discard(i + 1)
                cnt += 1
    return cnt

# print(solution(3,[3],[1]))

