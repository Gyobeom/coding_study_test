from collections import Counter

def solution(participant, completion):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: participant(참가자 이름 리스트), completion(완주자 이름 리스트).
    - 반환값: 완주하지 못한 선수의 이름(문자열) 하나를 return 한다.
    """
    # 완주하지 못한 선수의 이름을 반환 (찾아햠) -> 해시 풀이
    # 완주하지 못한 선수는 항상 정확히 한명, 그외에는 동명이인 존재

    # 완주자 개수 정리
    participant_list = Counter(participant)
    completion_list = Counter(completion)
    for player in participant:
        if completion_list[player] != participant_list[player]:
            return player

print(solution(['test','a','b'],['a','b']))
