from enum import Enum
from typing import Optional, List


class EnumBase(Enum):
    """
    데이터베이스 필드 및 컬렉션 Enum 지정을 위한 클래스입니다.
    """
    def __init__(self, code: int, val: str):
        self.code = code
        self.val = val

    def __str__(self):
        return self.val

    @classmethod
    def get_items(cls, field_name: Optional[str] = None):
        # 필드명이 있다면 해당 값, 그렇지 않으면 기본 val 데이터를 반환한다.
        if field_name:
            return [(item.code, getattr(item, field_name)) for item in cls]
        else:
            return [(item.code, item.val) for item in cls]

    @classmethod
    def get_codes(cls) -> List[int]:
        # 전체 선택가능한 코드 가져오기
        return [item.code for item in cls]

    @classmethod
    def get_vals(cls) -> List[str]:
        # 전체 선택가능한 이름 가져오기 
        return [item.val for item in cls]
