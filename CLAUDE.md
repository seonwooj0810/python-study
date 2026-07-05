# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 성격

자바 개발자를 위한 Python 학습 프로젝트다. 코드의 목적은 프로덕션 기능 구현이 아니라 **자바 ↔ Python 개념 대응을 예제로 익히는 것**이다. 따라서:

- 예제 함수/클래스에는 대응되는 자바 코드를 주석(`# Java: ...`)으로 병기하는 컨벤션을 유지한다.
- 새 예제를 추가할 때도 같은 방식(자바 대응 주석 + docstring에 개념 설명)을 따른다.
- docstring과 주석은 한국어로 작성한다.

## 명령어

가상환경이 `.venv`에 이미 있으므로 활성화 후 사용한다.

```bash
source .venv/bin/activate

pytest                          # 전체 테스트
pytest tests/test_basics.py     # 단일 파일
pytest tests/test_basics.py::test_greet_default   # 단일 테스트

ruff check .                    # 린트
ruff format .                   # 포맷
```

> 참고: 전역 규칙의 `./gradlew` 빌드/테스트 명령은 이 프로젝트(Python)에는 적용되지 않는다.

## 구조

- `src/python_study/` — 학습 모듈 (src 레이아웃). `pyproject.toml`의 `pythonpath = ["src"]` 설정으로 테스트에서 `from python_study.basics import ...` 형태로 import한다.
- `tests/` — pytest 테스트. `test_*` 함수 규칙을 따른다.
- 의존성은 런타임 없음(`dependencies = []`), 개발용으로 pytest·ruff만 사용한다.

## 코드 스타일

ruff 설정(`pyproject.toml`)을 따른다: line-length 100, target py311, lint 룰 `E/F/I/UP/B`. Python 3.11+ 문법(`list[int]` 등 내장 제네릭)을 사용한다.
