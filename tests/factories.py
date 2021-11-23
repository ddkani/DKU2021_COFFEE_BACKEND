import factory
from factory.django import DjangoModelFactory


class FactoryBase(DjangoModelFactory):
    """
    테스트용 ORM 인스턴스 데이터를 생성하기 위한 팩토리 클래스의 기본 설정입니다.
    """
    class Meta:
        strategy = factory.CREATE_STRATEGY
        model = None
        abstract = True
