# 진행 이력 (PROGRESS)

풀이·채점 결과를 누적 기록하는 대시보드. 채점이 끝날 때마다 Claude가 갱신한다.

## 요약

| 항목 | 값 |
|------|----|
| 총 출제 | 38 |
| 풀이 완료 | 30 |
| 통과 | 30 |

## 이력

| 날짜 | 출처 | 문제 | 난이도 | 상태 | 채점 | 비고 |
|------|------|------|--------|------|------|------|
| 2026-07-09 | custom | [001_두_수의_합](problems/custom/001_두_수의_합/) | ★☆☆ | 🟢 통과 | 6/6 | 브루트포스 O(n²). 개선: 해시 O(n) |
| 2026-07-09 | programmers | [lv1/001_계단_오르기](problems/programmers/lv1/001_계단_오르기/) | ★☆☆ | 🟢 통과 | 8/8 | DFS 입문(nonlocal 누적). 개선: return 합산/메모이제이션 |
| 2026-07-09 | programmers | [lv2/001_부분_수열의_합](problems/programmers/lv2/001_부분_수열의_합/) | ★★☆ | 🟢 통과 | 10/10 | 완전탐색 DFS(넣는다/뺀다 2갈래) |
| 2026-07-09 | programmers | [lv2/002_이어붙여_만든_수](problems/programmers/lv2/002_이어붙여_만든_수/) | ★★☆ | 🟢 통과 | 9/9 | 완전탐색 DFS+방문배열(순열) |
| 2026-07-10 | programmers | [lv2/003_타겟_넘버](problems/programmers/lv2/003_타겟_넘버/) | ★★☆ | 🟢 통과 | 8/8 | 완전탐색 DFS(+/− 2갈래), return형+메모 학습 |
| 2026-07-10 | programmers | [lv2/004_섬의_개수](problems/programmers/lv2/004_섬의_개수/) | ★★☆ | 🟢 통과 | 8/8 | 격자 DFS(플러드필, 4방향+in-place 방문). O(R×C) |
| 2026-07-10 | programmers | [lv2/005_가장_큰_섬](problems/programmers/lv2/005_가장_큰_섬/) | ★★☆ | 🟢 통과 | 8/8 | 격자 DFS 반환형(넓이 집계, area=1+사방합, max 갱신) |
| 2026-07-20 | programmers | [lv3/001_네트워크](problems/programmers/lv3/001_네트워크/) | ★★★ | 📎 예제 | - | 인접 행렬 그래프 DFS(연결 요소). Claude가 답안 제시 → 자력 풀이 아님(예제). 07-20 BFS로 자력 재풀이(주석 보관, `visited[j] = True` 오탈자 1건은 Claude가 수정) |
| 2026-07-13 | custom | [002_섬_넓이_목록](problems/custom/002_섬_넓이_목록/) | ★★☆ | 🟢 통과 | 8/8 | 격자 DFS 복습(넓이 전부 모아 정렬, max→append) |
| 2026-07-13 | custom | [003_가장_큰_네트워크](problems/custom/003_가장_큰_네트워크/) | ★★★ | 🟢 통과 | 8/8 | 인접 행렬 그래프 DFS 자력 연습(크기 반환+max, 격자→그래프 전이) |
| 2026-07-14 | custom | [004_네트워크_크기_목록](problems/custom/004_네트워크_크기_목록/) | ★★★ | 🟢 통과 | 8/8 | 그래프 DFS 자력 연습(크기 전부 모아 정렬, max→append 변형) |
| 2026-07-14 | programmers | [lv3/002_단어_변환](problems/programmers/lv3/002_단어_변환/) | ★★★ | 🟢 통과 | 8/8 | 실전 1단계: 암시적 그래프 DFS, 최솟값형 반환 학습(min 연결 3줄은 Claude 보조) |
| 2026-07-20 | programmers | [lv2/006_게임_맵_최단거리](problems/programmers/lv2/006_게임_맵_최단거리/) | ★★☆ | 🟢 통과 | 8/8 | 실전 2단계: 격자 BFS 자력 첫 통과(deque, 넣는 순간 방문 표시, cnt 큐에 동반) |
| 2026-07-20 | programmers | [lv3/003_여행경로](problems/programmers/lv3/003_여행경로/) | ★★★ | 🟢 통과 | 8/8 | 실전 3단계: DFS 백트래킹 자력 통과(간선 방문+실패 시 반납, dfs 내 후보 순회, 사전순 정렬) |
| 2026-07-20 | programmers | [lv1/002_완주하지_못한_선수](problems/programmers/lv1/002_완주하지_못한_선수/) | ★☆☆ | 🟢 통과 | 7/7 | 2주차: 해시 입문. Counter 2개 대조로 개수 다른 선수 반환(동명이인 처리, O(n)) |
| 2026-07-20 | programmers | [lv1/003_폰켓몬](problems/programmers/lv1/003_폰켓몬/) | ★☆☆ | 🟢 통과 | 7/7 | 2주차: 집합으로 종류 수 세고 N/2와 min 비교 |
| 2026-07-20 | programmers | [lv1/004_신고_결과_받기](problems/programmers/lv1/004_신고_결과_받기/) | ★☆☆ | 🟢 통과 | 7/7 | 2주차: 해시+구현. set 중복신고 제거→피신고자별 신고자 집계→정지자 신고자 Counter |
| 2026-07-20 | programmers | [lv2/007_의상](problems/programmers/lv2/007_의상/) | ★★☆ | 🟢 통과 | 7/7 | 2주차: 해시 응용. 종류별 개수 세고 (개수+1) 곱한 뒤 -1(전부 안 입는 경우 제외) |
| 2026-07-20 | programmers | [lv1/005_K번째수](problems/programmers/lv1/005_K번째수/) | ★☆☆ | 🟢 통과 | 7/7 | 3주차: 정렬(구간 자르기→sort→k-1 인덱스) |
| 2026-07-20 | programmers | [lv2/008_가장_큰_수](problems/programmers/lv2/008_가장_큰_수/) | ★★☆ | 🟢 통과 | 7/7 | 3주차: 정렬(key=str(x)*3 내림차순, 결과 0 시작이면 '0') |
| 2026-07-20 | programmers | [lv2/009_올바른_괄호](problems/programmers/lv2/009_올바른_괄호/) | ★★☆ | 🟢 통과 | 7/7 | 3주차: 스택(여는 괄호 push, 닫는 괄호 pop, 빈 스택에 pop이면 False) |
| 2026-07-20 | programmers | [lv2/010_기능개발](problems/programmers/lv2/010_기능개발/) | ★★☆ | 🟢 통과 | 9/9 | 3주차: 배포 묶음. 시뮬레이션→완성일수(math.ceil) O(N) 리팩터. 올림 누락 반례(같은 날 완성) test에 추가 |
| 2026-07-20 | programmers | [lv2/011_프로세스](problems/programmers/lv2/011_프로세스/) | ★★☆ | 🟢 통과 | 7/7 | 3주차: 큐(꺼낸 뒤 더 급한 게 남았으면 재삽입, (val,idx)로 추적) |
| 2026-07-20 | programmers | [lv1/006_체육복](problems/programmers/lv1/006_체육복/) | ★☆☆ | 🟢 통과 | 8/8 | 4주차: 그리디(겹침 제거 후 앞→뒤 순 대여). set 차집합·discard로 O(N) 리팩터. 완전탐색 3000건 대조 일치 |
| 2026-07-20 | programmers | [lv2/012_큰_수_만들기](problems/programmers/lv2/012_큰_수_만들기/) | ★★☆ | 🟢 통과 | 10/10 | 4주차: 단조 스택 그리디(뒤가 크면 앞 작은 것 pop, 남은 k 뒤에서 절단). 골격 힌트 후 자력 완성, 완전탐색 2000건 대조 |
| 2026-07-20 | programmers | [lv2/013_구명보트](problems/programmers/lv2/013_구명보트/) | ★★☆ | 🟢 통과 | 8/8 | 4주차: 그리디(정렬 후 최중량+최경량 짝짓기). pop(0) O(N²)→투포인터 O(N log N) 리팩터(N=5만 1.19s→0.005s). 3000건 대조 |
| 2026-07-20 | programmers | [lv2/014_소수_찾기](problems/programmers/lv2/014_소수_찾기/) | ★★☆ | 🟢 통과 | 8/8 | 4주차: 완전탐색(permutations 전체 길이+√N 소수판정+set 중복제거). 리딩제로 스킵 안전성 3000건 대조 |
| 2026-07-20 | programmers | [lv2/015_카펫](problems/programmers/lv2/015_카펫/) | ★★☆ | 🟢 통과 | 8/8 | 4주차: 완전탐색(넓이 약수 √N 순회+역산). 초기 O(N²)·print 버그→√N return 수정. 5000건 대조 |
| 2026-07-20 | programmers | [lv2/016_더_맵게](problems/programmers/lv2/016_더_맵게/) | ★★☆ | 🟢 통과 | 9/9 | 5주차: 최소 힙(가장 안 매운 두 개 섞기 반복, 남은 1개<K면 -1). 참조 5000건 대조 |
| 2026-07-20 | programmers | [lv3/004_이중우선순위큐](problems/programmers/lv3/004_이중우선순위큐/) | ★★★ | 🟢 통과 | 16/16 | 5주차: 두 힙+지연삭제. 재작성 중 stale 버그 반복(D 연산도 pop_number로 stale 스킵해야, 대칭 2곳). 반례 7건 test, 참조 7만건 대조 |
| 2026-07-20 | programmers | [lv3/005_입국심사](problems/programmers/lv3/005_입국심사/) | ★★★ | 🟢 통과 | 9/9 | 5주차: 파라메트릭 서치(답 t를 이분탐색, Σ(t//time)≥n 최소 t). 참조 2만건 대조, 10만·10억 0.48s |
| 2026-07-20 | programmers | [lv2/017_멀리_뛰기](problems/programmers/lv2/017_멀리_뛰기/) | ★★☆ | 🟡 출제됨 | - | 6주차: DP(1·2칸, 피보나치 꼴, mod) |
| 2026-07-20 | programmers | [lv2/018_피보나치_수](problems/programmers/lv2/018_피보나치_수/) | ★★☆ | 🟡 출제됨 | - | 6주차: DP(피보나치, 반복+mod) |
| 2026-07-20 | programmers | [lv3/006_정수_삼각형](problems/programmers/lv3/006_정수_삼각형/) | ★★★ | 🟡 출제됨 | - | 6주차: DP(경로 최대합, 위→아래 누적) |
| 2026-07-20 | programmers | [lv1/007_키패드_누르기](problems/programmers/lv1/007_키패드_누르기/) | ★☆☆ | 🟡 출제됨 | - | 구현 복습: 좌표 거리·손 규칙 |
| 2026-07-20 | programmers | [lv1/008_크레인_인형뽑기_게임](problems/programmers/lv1/008_크레인_인형뽑기_게임/) | ★★☆ | 🟡 출제됨 | - | 구현·스택 복습: 뽑아 쌓고 짝 터뜨리기 |
| 2026-07-20 | programmers | [lv2/019_주차_요금_계산](problems/programmers/lv2/019_주차_요금_계산/) | ★★☆ | 🟡 출제됨 | - | 구현 복습: 조건 분해·시간 정산·올림 |
| 2026-07-20 | programmers | [lv2/020_행렬_테두리_회전하기](problems/programmers/lv2/020_행렬_테두리_회전하기/) | ★★☆ | 🟡 출제됨 | - | 시뮬레이션 복습: 테두리 시계 회전 |

<!-- 상태 범례: 🟡 출제됨 · 🟠 풀이중 · 🟢 통과 · 🔴 실패(재도전) · 📎 예제(Claude가 답안 제시, 자력 풀이 아님) -->
