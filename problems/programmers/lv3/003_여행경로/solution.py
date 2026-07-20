def solution(tickets):
    """여행경로를 구현한다.

    - "ICN"에서 출발해 주어진 tickets(항공권 [출발지, 도착지])를 모두 사용하는
      방문 공항 경로를 리스트로 return 한다.
    - 가능한 경로가 여러 개면 알파벳 순서가 앞서는 경로를 return 한다.
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.
    """

    # 전체를 순회 하면서 완전히 종료되는 경로를 반환 해야함.
    # ICN 공항에서 항상 출발
    # DFS를 활용해서 풀어야 함. 끝까지 파봐야 하기에.
    # 방문 횟수에 대한 초기화가 필요 함. 기존 첫번째에서 실패할 경우, 다음에서 다시 방문할 수 있기에

    # 리스트 알파벳 정렬
    tickets.sort(key=lambda x:x[1])

    def dfs(ticket_idx):
      vistied[ticket_idx] = True

      for j in range(len(tickets)):
        # 아직 방문하지 않았고, 도착지가 방문할 출발지와 동일한 경우
        if not vistied[j] and tickets[j][0] == tickets[ticket_idx][1]:
          history.append(tickets[j][1])
          # new_history = [*history, tickets[j][1]]
          if len(history) == len(tickets) + 1:
            return history
          result = dfs(j)
          if result:
            return result
          vistied[j] = False
          history.pop()

    if len(tickets) == 1:
      return [tickets[0][0],tickets[0][1]]
    else:
      for i in range(len(tickets)):
        vistied = [False] * len(tickets)
        history = ['ICN']
        if tickets[i][0] == 'ICN':
          history.append(tickets[i][1])
          result = dfs(i)
          if result:
            return result

print(solution([['ICN', 'AAA'], ['ICN', 'BBB'], ['BBB', 'ICN']]))
