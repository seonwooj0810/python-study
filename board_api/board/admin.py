"""Django 관리자(admin) 등록.

Django admin 은 모델을 등록하면 CRUD 관리 화면을 자동 생성해 준다.
자바 진영에는 정확히 대응하는 표준 기능이 없지만, 굳이 비유하면
스프링부트 백오피스 성격의 자동 관리 UI 에 가깝다.
"""

from django.contrib import admin

from .models import Post


# Java: 관리 화면 목록에 노출할 컬럼 지정.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author", "created_at"]
    search_fields = ["title", "author"]
