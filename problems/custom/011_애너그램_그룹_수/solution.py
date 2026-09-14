def solution(words):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - words: 소문자 영어 문자열들의 리스트.
    - 애너그램끼리 묶었을 때 그룹의 개수를 return 한다.
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.
    """

    # 문자열이 포함된 리스트를 순회하면서 오름 차순 정렬
    # 정렬된 문자열 딕셔너리 작업 없으면 1, 있으면 +1

    word_dict = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        word_dict[sorted_word] = word_dict.get(sorted_word,0)

    return len(word_dict)
