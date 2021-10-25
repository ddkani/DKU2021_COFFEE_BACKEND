import os
import sys
import django


def main():
    # TOOD: 필요 모듈 import
    # 아마도 이곳에서 consumer 구현해서 사용할 것으로 보임.
    pass


if __name__ == '__main__':
    sys.path.append(os.getcwd())
    # TODO: warning or use default profile -> DJANGO_SETTINGS_MODULE
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_service_scheduler.settings')
    try:
        django.setup()
    except ModuleNotFoundError:
        print('오류: 프로젝트의 루트 디렉터리에서 실행해 주세요.')
        print(f'ex) python scripts/{os.path.basename(__file__)}')
    main()
