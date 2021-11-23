import pytest
from faker import Faker

fake = Faker()
pytestmark = pytest.mark.django_db

# TODO: 테스트 데이터베이스 판단 여부를 위한 임시 테스트 코드입니다.


def test_dump():
    assert True
