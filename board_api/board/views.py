"""API 뷰 계층.

DRF 의 ViewSet 은 자바 Spring 의 @RestController 에 대응한다.
ModelViewSet 하나만 상속하면 list/create/retrieve/update/partial_update/destroy
(= 목록/생성/단건조회/수정/부분수정/삭제) 5종 CRUD 가 자동으로 제공된다.
Spring Data JPA 의 기본 CRUD 리포지토리를 상속받는 것과 비슷한 개념이다.
"""

from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


# Java:
#   @RestController
#   @RequestMapping("/api/posts")
#   public class PostController {
#       // GET "" / POST "" / GET "/{id}" / PUT "/{id}" / PATCH "/{id}" / DELETE "/{id}"
#   }
class PostViewSet(viewsets.ModelViewSet):
    """게시글 CRUD 컨트롤러 (자바 @RestController + Spring Data Repository 대응).

    - GET    /api/posts/         → 목록 (list)      = findAll (+ 페이지네이션)
    - POST   /api/posts/         → 생성 (create)    = save
    - GET    /api/posts/{id}/    → 단건 (retrieve)  = findById
    - PUT    /api/posts/{id}/    → 전체수정 (update)
    - PATCH  /api/posts/{id}/    → 부분수정 (partial_update)
    - DELETE /api/posts/{id}/    → 삭제 (destroy)   = deleteById
    """

    # Java: 리포지토리의 조회 대상. QuerySet 은 지연 평가되는 쿼리 빌더다.
    queryset = Post.objects.all()

    # Java: 요청/응답 변환에 사용할 DTO 매퍼 지정.
    serializer_class = PostSerializer
