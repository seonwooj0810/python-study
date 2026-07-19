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
├── board_api/            # Django REST Framework 게시판 CRUD 예제 (아래 참고)
│   ├── board/            # models / serializers / views / urls
│   ├── config/           # settings / urls (Spring의 application.yml 대응)
│   └── manage.py
└── tests/
    └── test_basics.py
```

## Django REST Framework 게시판 (board_api)

기초 문법 예제(`basics.py`) 외에, Spring MVC로 REST API를 만들던 경험을
Django/DRF로 대응시켜 익히는 **게시판 CRUD 예제**가 `board_api/`에 포함되어 있다.
`ModelViewSet` 하나로 목록/생성/단건조회/수정/부분수정/삭제 5종 CRUD가 자동 제공된다.

| 메서드 | 경로 | Spring Data 대응 |
| --- | --- | --- |
| GET | `/api/posts/` | `findAll(Pageable)` |
| POST | `/api/posts/` | `save` |
| GET | `/api/posts/{id}/` | `findById` |
| PUT / PATCH | `/api/posts/{id}/` | `save` / 부분수정 |
| DELETE | `/api/posts/{id}/` | `deleteById` |

```bash
pip install -e ".[web,dev]"
cd board_api
python manage.py migrate
python manage.py runserver   # http://127.0.0.1:8000/api/posts/
```

자세한 계층 대응표(Java/Spring ↔ Django/DRF)와 실행/테스트 방법은
[`board_api/README.md`](board_api/README.md) 참고.

## 학습 순서 제안

1. `src/python_study/basics.py`를 열어 자바 대응 주석과 비교
2. `tests/test_basics.py`로 pytest 사용법 익히기
3. 예제를 직접 수정하며 `pytest`로 확인
