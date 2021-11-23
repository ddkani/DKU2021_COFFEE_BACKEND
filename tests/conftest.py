import os
import platform

# from django.core.cache import cache
# django cache management 등 삭제 필요 데이터 있을 시 적용합니다.

# TODO: 설정을 적용해서 전체 테스트에 Requester에 대한 테스트는 제외하고, 특정 환경에서 실행했을 때 Requester에 대한 테스트만 별도로 실행할 수 있도록 구성 필요


def pytest_sessionstart(session):
    # 테스트 환경에서 리소스 파일을 로드하기 위해 작업 경로를 일괄적으로 변경합니다.
    dir_char = '\\' if platform.system() == 'Windows' else '/'
    dirs = os.getcwd().split(dir_char)
    dirs_len = len(dirs)

    if 'tests' in dirs:
        last_idx = 0
        for idx in range(1, dirs_len + 1):
            if dirs[-idx] == 'tests':
                last_idx = dirs_len - idx
        os.chdir(dir_char.join(dirs[:last_idx]))


def pytest_sessionfinish(session, exitstatus):
    pass

