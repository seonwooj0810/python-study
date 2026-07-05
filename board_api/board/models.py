"""게시판 도메인 모델.

Django 의 Model 은 자바 JPA 의 @Entity 에 대응한다.
필드 선언이 곧 테이블 컬럼 매핑이며, ORM 이 SQL 을 대신 생성한다.
"""

from django.db import models


# Java:
#   @Entity
#   @Table(name = "post")
#   public class Post {
#       @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
#       private Long id;
#       ...
#   }
class Post(models.Model):
    """게시글 엔티티 (자바 JPA @Entity 대응).

    Django 는 명시하지 않으면 자동 증가 PK(id)를 자동으로 추가한다
    (자바의 @Id @GeneratedValue 를 안 써도 되는 셈).
    """

    # Java: @Column(nullable = false, length = 200) private String title;
    title = models.CharField("제목", max_length=200)

    # Java: @Lob @Column(nullable = false) private String content;
    content = models.TextField("내용")

    # Java: @Column(nullable = false, length = 50) private String author;
    author = models.CharField("작성자", max_length=50)

    # Java: @CreationTimestamp private LocalDateTime createdAt;
    created_at = models.DateTimeField("작성일시", auto_now_add=True)

    # Java: @UpdateTimestamp private LocalDateTime updatedAt;
    updated_at = models.DateTimeField("수정일시", auto_now=True)

    class Meta:
        # Java: 리포지토리 조회 시 기본 정렬. 최신 글이 먼저 오도록 id 역순.
        ordering = ["-id"]

    # Java: @Override public String toString() { return "Post(...)"; }
    def __str__(self) -> str:
        return f"Post(id={self.id}, title={self.title!r})"
