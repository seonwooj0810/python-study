"""게시판 CRUD API 통합 테스트.

DRF 의 APIClient 는 자바 Spring 의 MockMvc / TestRestTemplate 에 대응한다.
실제 HTTP 요청을 흉내 내 엔드포인트를 호출하고 상태코드/본문을 검증한다.

@pytest.mark.django_db 는 자바 @DataJpaTest 처럼 테스트마다 트랜잭션을
열고 끝나면 롤백해, 테스트 간 DB 상태를 격리한다.
"""

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from board.models import Post


# Java: @BeforeEach 로 MockMvc/픽스처를 준비하는 것에 대응 (pytest fixture).
@pytest.fixture
def client() -> APIClient:
    return APIClient()


@pytest.fixture
def sample_post() -> Post:
    """DB 에 게시글 하나를 미리 생성 (자바 given 절의 테스트 데이터 준비)."""
    return Post.objects.create(title="첫 글", content="본문입니다", author="정선우")


# --- Create (POST /api/posts/) --------------------------------------------
@pytest.mark.django_db
def test_create_post(client: APIClient) -> None:
    """게시글 생성 → 201 Created 와 생성된 리소스 반환."""
    payload = {"title": "새 글", "content": "내용", "author": "홍길동"}

    res = client.post("/api/posts/", payload, format="json")

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["id"] is not None
    assert res.data["title"] == "새 글"
    # 서버가 채우는 타임스탬프가 응답에 포함된다.
    assert res.data["created_at"] is not None
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_create_post_blank_title_returns_400(client: APIClient) -> None:
    """공백 제목은 검증 실패 → 400 (자바 @Valid 검증 실패에 대응).

    커스텀 validate_title 이 실제로 동작함을 메시지로 확인한다
    (CharField 기본 trim 을 꺼서 공백-only 입력이 검증기까지 도달).
    """
    res = client.post(
        "/api/posts/",
        {"title": "   ", "content": "내용", "author": "홍길동"},
        format="json",
    )

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert "title" in res.data
    assert str(res.data["title"][0]) == "제목은 공백일 수 없습니다."


# --- Read (GET) ------------------------------------------------------------
@pytest.mark.django_db
def test_list_posts_is_paginated(client: APIClient, sample_post: Post) -> None:
    """목록 조회 → 200 과 페이지네이션 구조 (자바 Page<T> 응답에 대응)."""
    res = client.get("/api/posts/")

    assert res.status_code == status.HTTP_200_OK
    # PageNumberPagination 은 count/next/previous/results 형태로 감싼다.
    assert res.data["count"] == 1
    assert res.data["results"][0]["title"] == "첫 글"


@pytest.mark.django_db
def test_retrieve_post(client: APIClient, sample_post: Post) -> None:
    """단건 조회 → 200 과 해당 리소스."""
    res = client.get(f"/api/posts/{sample_post.id}/")

    assert res.status_code == status.HTTP_200_OK
    assert res.data["id"] == sample_post.id
    assert res.data["author"] == "정선우"


@pytest.mark.django_db
def test_retrieve_missing_post_returns_404(client: APIClient) -> None:
    """존재하지 않는 id → 404 (자바 EntityNotFoundException → 404 매핑에 대응)."""
    res = client.get("/api/posts/9999/")

    assert res.status_code == status.HTTP_404_NOT_FOUND


# --- Update (PUT / PATCH) --------------------------------------------------
@pytest.mark.django_db
def test_update_post_put(client: APIClient, sample_post: Post) -> None:
    """전체 수정(PUT) → 200 과 갱신된 값."""
    payload = {"title": "수정된 제목", "content": "수정된 본문", "author": "정선우"}

    res = client.put(f"/api/posts/{sample_post.id}/", payload, format="json")

    assert res.status_code == status.HTTP_200_OK
    assert res.data["title"] == "수정된 제목"
    sample_post.refresh_from_db()
    assert sample_post.content == "수정된 본문"


@pytest.mark.django_db
def test_partial_update_post_patch(client: APIClient, sample_post: Post) -> None:
    """부분 수정(PATCH) → 제목만 바꾸고 나머지는 유지."""
    res = client.patch(
        f"/api/posts/{sample_post.id}/", {"title": "제목만 변경"}, format="json"
    )

    assert res.status_code == status.HTTP_200_OK
    assert res.data["title"] == "제목만 변경"
    assert res.data["author"] == "정선우"  # 그대로 유지


# --- Delete (DELETE) -------------------------------------------------------
@pytest.mark.django_db
def test_delete_post(client: APIClient, sample_post: Post) -> None:
    """삭제 → 204 No Content 와 실제 삭제 반영."""
    res = client.delete(f"/api/posts/{sample_post.id}/")

    assert res.status_code == status.HTTP_204_NO_CONTENT
    assert Post.objects.count() == 0
