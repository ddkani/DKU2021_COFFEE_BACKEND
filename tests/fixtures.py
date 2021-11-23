import pytest
from django.contrib.auth.models import User


# fixture default scope: function

@pytest.fixture
def client():
    """
    RestAPI 테스트를 위한 목업 클라이언트를 반환합니다.
    - 상황에 따라 로그인 여부가 변경되므로, 각 테스트 메서드마다 새로운 인스턴스가 생성되어야 합니다.
    """
    from rest_framework.test import APIClient

    class _Client(APIClient):
        def login(self, user: User):
            self.force_authenticate(user, None)

    return _Client()
