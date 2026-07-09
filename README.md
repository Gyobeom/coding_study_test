# coding_study

코딩 테스트 학습 저장소. **Claude가 문제를 제시 → 내가 풀이 → Claude가 채점 → git 이력 관리** 흐름으로 진행한다.

- 언어: **Python 3**
- 문제 출처: **프로그래머스**, **직접 출제(custom)**
- 원격 저장소: https://github.com/Gyobeom/coding_study_test.git

## 디렉터리 구조

```
coding_study/
├── README.md              # 이 문서
├── PROGRESS.md            # 풀이 이력/채점 결과 대시보드
├── .gitignore
├── lib/
│   └── judge.py           # 공용 채점기(테스트 케이스 실행·출력)
├── templates/             # 새 문제 생성 시 복사되는 원본
│   ├── README.md
│   ├── solution.py
│   └── test.py
└── problems/
    ├── programmers/       # 프로그래머스 문제 (레벨별)
    │   ├── lv1/
    │   ├── lv2/
    │   └── lv3/
    └── custom/            # Claude가 직접 출제한 문제
```

## 문제 한 개의 구성

각 문제는 폴더 하나로 관리한다.

```
problems/<출처>/<분류>/<번호>_<문제이름>/
├── README.md      # 문제 설명·제약·입출력 예시 (Claude가 작성)
├── solution.py    # 풀이 (내가 작성)
└── test.py        # 채점 테스트 (Claude가 작성)
```

> **출제·채점 규격의 원본은 [`CLAUDE.md`](CLAUDE.md)** 다. 새 세션에서 자동으로 읽혀 동일한 형식으로 문제를 만들도록 하는 운영 규약이므로, 형식을 바꾸고 싶으면 그 문서를 수정한다.

## 진행 방식(워크플로우)

1. **출제** — Claude가 새 문제 폴더를 만들고 `README.md`(문제) + `solution.py`(빈 템플릿) + `test.py`(테스트 케이스)를 생성한다.
2. **풀이** — 내가 `solution.py`의 `solution(...)` 함수를 구현한다.
3. **채점** — Claude가 `python test.py`를 실행해 케이스별 통과 여부를 확인한다.
4. **학습 정리** — 필요 시 문제 `README.md`에 풀이 접근법·시간복잡도·배운 점을 덧붙인다.
5. **이력 관리** — `PROGRESS.md`를 갱신하고 git 커밋 → (opt-in) push.

## 로컬에서 직접 채점하기

```bash
# 특정 문제 채점
python problems/custom/001_두_수의_합/test.py

# 전체 문제 일괄 채점
python lib/run_all.py
```

## 커밋 컨벤션

- `문제: <출처> <이름> 출제` — 새 문제 추가
- `풀이: <출처> <이름> (통과 N/N)` — 풀이 및 채점 결과
- `학습: <주제>` — 학습 노트 추가
- `구성: <내용>` — 프로젝트 구조/설정 변경
