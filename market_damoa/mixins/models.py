import uuid
from django.db import models

# TODO: 작업 지정용 공통 테이블 정의


class GenericModelBase(models.Model):
    """
    관리형 내부 데이터 모델에 대한 Base 필드와 기능을 정의합니다.
    """
    class Meta:
        abstract = True

    # ! primary_key 인자값 넣어주어야 합니다. IDE에서 인식 못함.
    id = models.BigAutoField(primary_key=True)

    # 데이터 생성 시각
    created_at = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    # 데이터 업데이트 시각
    updated_at = models.DateTimeField(auto_now=True)


class ScrapedModelBase(models.Model):
    """
    외부로부터 수집되는 데이터 모델에 대한 Base 필드와 기능을 정의합니다.
    """
    class Meta:
        abstract = True

    # 외부로부터 수집된 데이터에는 항상 collected_id 로써 키 명칭을 고정합니다.
    collected_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 마찬가지로, 현재 서버로 해당 정보가 언제 수집되었는지의 시점도 지정되어야 합니다.
    collected_at = models.DateTimeField(auto_now_add=True, null=False, editable=False)


# TODO: Application 단위에서 하나씩 사용하고 type에 컬럼을 지정하거나, 또는 각 엔티티 단위로 사용
class ScrapedErrorModelBase(models.Model):
    """
    외부로부터 수집되는 데이터 중 오류가 발생한 정보에 대한 Base 필드와 기능을 정의합니다.
    """

    class Meta:
        abstract = True

    # 필수적인 오류 해결 원인 등? 을 넣어서 관리가 필요해 보임.