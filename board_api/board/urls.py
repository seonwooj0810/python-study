"""board 앱 URL 라우팅.

DRF 의 DefaultRouter 는 ViewSet 하나를 REST 리소스 URL 로 자동 매핑한다.
자바에서 @RequestMapping("/api/posts") 로 CRUD 경로를 여는 것과 대응하되,
경로를 일일이 선언하지 않아도 되는 점이 다르다.
"""

from rest_framework.routers import DefaultRouter

from .views import PostViewSet

# Java: 라우터가 /posts, /posts/{id} 경로 6종을 PostViewSet 액션에 자동 연결한다.
router = DefaultRouter()
router.register("posts", PostViewSet, basename="post")

urlpatterns = router.urls
