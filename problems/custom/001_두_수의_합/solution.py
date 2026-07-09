def solution(numbers, target):
    """배열에서 합이 target이 되는 두 원소의 인덱스 쌍 [i, j] (i < j) 를 반환.

    여기에 풀이를 구현하세요. (지금은 빈 템플릿이라 채점 시 실패합니다.)
    """

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                answer = [i,j]
                break
    return answer
