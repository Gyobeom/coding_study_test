# 완주하지 못한 선수

> 관련 파일: [내 풀이 코드](solution.py) · [풀이노트(회고)](풀이노트.md)

- **출처**: 프로그래머스 lv1 "완주하지 못한 선수"
- **난이도**: ★☆☆ (lv1)
- **분류**: 해시
- **링크**: https://school.programmers.co.kr/learn/courses/30/lessons/42576

## 문제

수많은 마라톤 선수들이 마라톤에 참여했습니다. 단 한 명의 선수를 제외하고는 모든 선수가 완주했습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 `participant`와 완주한 선수들의 이름이 담긴 배열 `completion`이 주어질 때,
**완주하지 못한 선수의 이름**을 반환하세요.

동명이인이 있을 수 있습니다. 즉, 같은 이름이 `participant`에 여러 번 등장할 수 있으며,
`completion`에도 그 이름이 여러 번 있을 수 있습니다.
완주하지 못한 선수는 항상 정확히 한 명입니다.

## 제약 조건

- `participant`의 길이는 1 이상 100,000 이하입니다.
- `completion`의 길이는 `participant`의 길이보다 정확히 1 작습니다.
- 참가자의 이름은 1 이상 20 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

## 입출력 예시

| participant | completion | 반환값 |
|-------------|------------|--------|
| `["leo", "kiki", "eden"]` | `["eden", "kiki"]` | `"leo"` |
| `["marina", "josipa", "nikola", "vinko", "filipa"]` | `["josipa", "filipa", "marina", "nikola"]` | `"vinko"` |
| `["mislav", "stanko", "mislav", "ana"]` | `["stanko", "ana", "mislav"]` | `"mislav"` |

## 함수 시그니처

```python
def solution(participant, completion):
    ...
```

> 풀이 후 회고는 [풀이노트.md](풀이노트.md)에 작성한다.
