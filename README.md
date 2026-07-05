# python-study

자바 개발자를 위한 Python 학습 프로젝트.

## 설정

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 테스트 (자바의 JUnit → Python은 pytest)

```bash
pytest
```

## 린트/포맷 (자바의 Checkstyle/Spotless → Python은 ruff)

```bash
ruff check .    # 린트
ruff format .   # 포맷
```

## 자바 ↔ Python 빠른 대응표

| 개념        | Java                          | Python                     |
|-------------|-------------------------------|----------------------------|
| 빌드/의존성 | Maven/Gradle (`pom.xml`)      | pip + `pyproject.toml`     |
| 패키지 격리 | JVM classpath                 | 가상환경 (`.venv`)         |
| DTO         | `record`                      | `@dataclass`               |
| 스트림 필터 | `stream().filter()`           | 리스트 컴프리헨션          |
| 테스트      | JUnit `@Test`                 | pytest `test_*` 함수       |
| 문자열 포맷 | `String.format` / `+`         | f-string (`f"{x}"`)        |
| 정적 타입   | 컴파일 타임 강제              | 타입 힌트(선택) + mypy     |

## 구조

```
python-study/
├── pyproject.toml
├── README.md
├── src/
│   └── python_study/
│       ├── __init__.py
│       └── basics.py     # 자바 대응 주석이 달린 학습 예제
└── tests/
    └── test_basics.py
```

## 학습 순서 제안

1. `src/python_study/basics.py`를 열어 자바 대응 주석과 비교
2. `tests/test_basics.py`로 pytest 사용법 익히기
3. 예제를 직접 수정하며 `pytest`로 확인
