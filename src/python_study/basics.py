"""자바 ↔ Python 대응 개념 학습용 예제 모음.

각 함수 옆 주석에 대응되는 자바 코드를 적어 두었습니다.
"""

from dataclasses import dataclass


# Java: public String greet(String name) { return "Hello, " + name + "!"; }
def greet(name: str = "World") -> str:
    """f-string으로 문자열 포매팅 (자바의 String.format / + 연산 대응)."""
    return f"Hello, {name}!"


# Java: List<Integer> evens = nums.stream().filter(n -> n % 2 == 0).toList();
def evens(numbers: list[int]) -> list[int]:
    """리스트 컴프리헨션 (자바 Stream.filter 대응)."""
    return [n for n in numbers if n % 2 == 0]


# Java: int sum = nums.stream().mapToInt(Integer::intValue).sum();
def total(numbers: list[int]) -> int:
    """내장 함수 sum (자바 Stream.sum 대응)."""
    return sum(numbers)


# Java: record User(String name, int age) {}
@dataclass(frozen=True)
class User:
    """@dataclass는 자바 record와 유사 (생성자/equals/toString 자동 생성)."""

    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 19
