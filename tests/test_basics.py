"""basics 모듈 테스트 (자바의 JUnit 대응 = pytest)."""

from python_study.basics import User, evens, greet, total


# 자바: @Test void greet_default() { assertEquals("Hello, World!", greet()); }
def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("Seonwoo") == "Hello, Seonwoo!"


def test_evens():
    assert evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_total():
    assert total([1, 2, 3]) == 6


def test_user_dataclass():
    user = User(name="Seonwoo", age=30)
    assert user.is_adult() is True
    # dataclass는 값 동등성 지원 (자바 record의 equals 대응)
    assert user == User(name="Seonwoo", age=30)
