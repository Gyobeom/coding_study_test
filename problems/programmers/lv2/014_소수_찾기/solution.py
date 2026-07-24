from itertools import permutations

def solution(numbers):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자:
        numbers (str) : 한 자리 숫자 조각들이 이어진 문자열.
    - 반환값: 조각으로 만들 수 있는 서로 다른 수 중 소수의 개수(int)를 return 한다.
    """

    # 모든 숫자들에 대해서 소수가 될 수 잇는 수를 구해야함.

    # 소수점 구하는 함수
    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:      # √n 까지만 확인하면 충분
            if n % i == 0:
                return False   # 하나라도 나눠지면 소수 아님
            i += 1
        return True

    number_list = list(map(int,numbers))
    answer = set()

    for i in range(1,len(number_list) + 1):
        for p in permutations(number_list, i):
            # 2자리 이상이면서 0인 경우 무시
            if i > 1 and p[0] == 0:
                continue

            num = int(''.join(map(str,p)))
            if is_prime(num) == True:
                answer.add(num)
    return len(answer)

# print(solution('011'))
