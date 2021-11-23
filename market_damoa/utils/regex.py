"""
파싱을 위한 라이브러리 (regex 등) 에 대한 유틸리티성 메서드를 제공합니다.
"""

import re
from typing import Optional, List, Tuple


def __try_to_convert(value: str, convert_type: Optional[type], ignore_fail_to_none: bool):
    """
    입력값과 type을 바탕으로 명시적 형변환을 시도합니다.
    """
    if convert_type:
        try:
            return convert_type(value)
        except ValueError as e:
            if ignore_fail_to_none:
                return None
            else:
                raise e
    else:
        return value


def rx_find_single_group(
        source: str, regex: str, convert_type: Optional[type] = None, ignore_fail_to_none: bool = False
) -> Optional:
    """
    re.search (단일 검사) 실행으로 일치하는 데이터의 단일 그룹을 지정한 타입으로 변환합니다.

    @source: 파싱 대상 문서
    @regex: 파싱 regex
    @convert_type: 추출한 문자의 변환 타입. 변환하지 않을 경우 None 입니다.
    @ignore_fail_to_none: 추출이 실패했을 경우, True 라면 오류를 무시하고 None을 입력합니다.
    """
    match = re.search(regex, source)
    return __try_to_convert(match.groups()[0], convert_type, ignore_fail_to_none) if match else None


def rx_find_multiple_group(
        source: str, regex: str, convert_groups: List[Optional[type]], ignore_fail_to_none: bool = False
) -> Optional[List]:
    """
    re.search (단일 검사) 실행으로 일치하는 데이터의 다중 그룹을 지정한 타입으로 변환합니다.

    @source: 파싱 대상 문서
    @regex: 파싱 regex
    @convert_type: 추출한 문자의 변환 타입. 변환하지 않을 경우 None 입니다.
    @ignore_fail_to_none: 추출이 실패했을 경우, True 라면 오류를 무시하고 None을 입력합니다.
    """
    extract_group_size = len(convert_groups)
    assert extract_group_size, "추출 그룹이 지정되어야 합니다."

    match = re.search(regex, source)
    if not match:
        return None
    
    results = []
    groups = match.groups()
    for idx in range(extract_group_size):
        value = groups[idx]
        convert_type = convert_groups[idx]
        results.append(__try_to_convert(value, convert_type, ignore_fail_to_none))

    return results


def rx_findall_single_group(
        source: str, regex: str, convert_type: Optional[type] = None, ignore_fail_to_none: bool = False
) -> List:
    """
    re.findall(전체 검사) 실행으로 일치하는 데이터들의 단일 그룹을 지정한 타입으로 변환합니다.

    @source: 파싱 대상 문서
    @regex: 파싱 regex
    @convert_type: 추출한 문자의 변환 타입. 변환하지 않을 경우 None 입니다.
    @ignore_fail_to_none: 추출이 실패했을 경우, True 라면 오류를 무시하고 None을 입력합니다.
    """
    results = []
    matches = re.findall(regex, source)
    for match in matches:
        results.append(__try_to_convert(match, convert_type, ignore_fail_to_none))

    return results


def rx_findall_multiple_groups(
        source: str, regex: str, convert_groups: List[Optional[type]], ignore_fail_to_none: bool = False
) -> List[List]:
    """
    re.findall(전체 검사) 실행으로 일치하는 데이터들의 다중 그룹을 지정한 타입으로 변환합니다.

    @source: 파싱 대상 문서
    @regex: 파싱 regex
    @convert_groups: 추출한 문자의 각 그룹별 변환 타입. 변환하지 않을 경우 None 입니다.
    @ignore_fail_to_none: 추출이 실패했을 경우, True 라면 오류를 무시하고 None을 입력합니다.
    """
    extract_group_size = len(convert_groups)
    assert extract_group_size, "추출 그룹이 지정되어야 합니다."

    # N개 이상의 그룹 파싱을 시도하면, 해당 N개와 매칭되지 않은 경우 findall 결과에 포함되지 않음에 유의한다.

    results = []
    matches = re.findall(regex, source)
    for match in matches:  # type: Tuple
        bucket = []
        for idx in range(extract_group_size):
            value = match[idx]
            convert_type = convert_groups[idx]
            bucket.append(__try_to_convert(value, convert_type, ignore_fail_to_none))

        results.append(bucket)

    return results
