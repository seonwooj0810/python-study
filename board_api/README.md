# board_api — Django REST Framework 게시판 CRUD 예제

자바 개발자를 위한 Django REST Framework(DRF) 학습 예제다.
Spring MVC 로 REST API 를 만들던 경험을 Django/DRF 로 대응시켜 익히는 것이 목적이다.

## 계층 대응표 (Java/Spring ↔ Django/DRF)

| 역할 | Java / Spring | Django / DRF | 파일 |
| --- | --- | --- | --- |
| 엔티티 | `@Entity` (JPA) | `models.Model` | `board/models.py` |
| DTO + 검증 | DTO + Jackson + Bean Validation | `ModelSerializer` | `board/serializers.py` |
| 컨트롤러 + 리포지토리 | `@RestController` + Spring Data Repository | `ModelViewSet` | `board/views.py` |
| 라우팅 | `@RequestMapping` | `DefaultRouter` | `board/urls.py` |
| 설정/프로파일 | `application.yml` | `config/settings.py` | `config/settings.py` |

`ModelViewSet` 하나로 아래 5종 CRUD 가 자동 제공된다.

| 메서드 | 경로 | 액션 | Spring Data 대응 |
| --- | --- | --- | --- |
| GET | `/api/posts/` | list (페이지네이션) | `findAll(Pageable)` |
| POST | `/api/posts/` | create | `save` |
| GET | `/api/posts/{id}/` | retrieve | `findById` |
| PUT | `/api/posts/{id}/` | update (전체) | `save` |
| PATCH | `/api/posts/{id}/` | partial_update (부분) | — |
| DELETE | `/api/posts/{id}/` | destroy | `deleteById` |

## 실행

```bash
# 프로젝트 루트에서 (의존성은 web extra 로 관리)
source .venv/bin/activate
pip install -e ".[web,dev]"

cd board_api
python manage.py migrate         # DB 스키마 생성 (Flyway/Hibernate ddl-auto 대응)
python manage.py runserver       # http://127.0.0.1:8000/api/posts/

# 관리자 화면을 쓰려면 (선택)
python manage.py createsuperuser # 이후 /admin/ 접속
```

## 테스트

루트의 pytest 진입점을 그대로 사용한다(`pytest-django` 로 통합).

```bash
pytest tests/test_board_api.py   # 게시판 API 통합 테스트만
pytest                           # 전체 (basics + board API)
```
