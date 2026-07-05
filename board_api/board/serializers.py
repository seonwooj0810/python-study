"""직렬화(Serializer) 계층.

DRF 의 Serializer 는 자바의 DTO + Jackson(직렬화/역직렬화) + Bean Validation 을
합쳐 놓은 역할이다. 모델 ↔ JSON 변환과 입력 검증을 담당한다.
"""

from rest_framework import serializers

from .models import Post


# Java:
#   public record PostDto(Long id, String title, String content,
#                         String author, Instant createdAt, Instant updatedAt) {}
#   + ModelMapper/MapStruct 로 Entity ↔ DTO 변환
class PostSerializer(serializers.ModelSerializer):
    """Post 엔티티용 DTO (자바 DTO + Jackson + Validation 대응).

    ModelSerializer 는 모델 필드를 읽어 직렬화 규칙을 자동 생성한다.
    (MapStruct 가 매핑 코드를 자동 생성하는 것과 비슷하다.)
    """

    # Java: 기본 CharField 는 앞뒤 공백을 잘라낸 뒤(trim_whitespace) 검증하므로,
    #       공백-only 입력이 아래 validate_title 에 닿기 전에 걸러진다.
    #       커스텀 검증기가 직접 공백을 판단하도록 자동 trim 을 끈다.
    title = serializers.CharField(max_length=200, trim_whitespace=False)

    class Meta:
        model = Post
        # Java: DTO 에 노출할 필드 목록.
        fields = ["id", "title", "content", "author", "created_at", "updated_at"]
        # Java: 서버가 채우는 값이라 클라이언트 입력은 무시(읽기 전용)한다.
        read_only_fields = ["id", "created_at", "updated_at"]

    # Java: @AssertTrue 등 커스텀 검증 메서드에 대응. 필드 단위 검증은 validate_<필드명>.
    def validate_title(self, value: str) -> str:
        """제목 공백 검증 (자바 @NotBlank 대응)."""
        if not value.strip():
            raise serializers.ValidationError("제목은 공백일 수 없습니다.")
        return value
