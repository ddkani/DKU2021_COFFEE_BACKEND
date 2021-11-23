from drf_yasg import openapi


def convert_openapi_schema_to_json_schema(schema: openapi.Schema) -> dict:
    """
    API가 작성된 API문서(drf-yasg Redoc)과 일치하는 스키마를 가지는지 여부를 파악하기 위해,
    openapi.Schema로 구성된 인스턴스를 jsonschema 라이브러리의 포맷으로 변경합니다.
    """

    # TODO: 스키마 변경 로직 작성
    pass
