from abc import ABCMeta, abstractmethod
from typing import Optional, List

from requests import Session, Response


# TODO: 웹 요청의 경우, 문서 파싱과는 다르게 하나의 세션을 가지고 반복적으로 요청할 수 있으며,
# TODO: 이 경우 기존 커넥션과 리소스를 재사용하게 되므로, 인스턴스 가능 일반 클래스로 생성합니다.
# TODO: Requester 가 어디까지의 정보를 가지고 있을것인가? ex - 실행 컨텍스트의 정보 일부 등에 대한 내용
# TODO: 필요한 경우 요청 전/후로 로깅
# TODO: 프로젝트 설정 등에 따른 User-Agent와 같은 정적 헤더와 쿠키와 같은 동적 헤더 사용 지원

class RequesterBase(metaclass=ABCMeta):
    """
    requests.Session 라이브러리를 기반으로 한 요청을 위한 클래스 베이스입니다.
    """

    # 외부 데이터 요청에 필요한 세션 인스턴스입니다.
    session = None  # type: Session

    # 전체 URL 제공을 위한 schema://domain 의 형태를 작성합니다.
    url_home = None  # type Optional[str]

    def __init__(self, sess: Optional[Session] = None):
        self.session = sess if sess else Session()

    def __get_full_url(self, url: str, full_url: Optional[str]) -> str:
        """
        사용자 코드 작성 편의를 위해 지정된 규칙에 따라 요청 URL을 빌드합니다.
        """
        if full_url:
            return full_url
        else:
            assert self.url_home, "full_url이 제공되지 않은 경우, url_home (schema://domain) 이 제공되어야 합니다."
            assert not url.startswith('/'), 'url은 \'/\'로 시작해야 합니다.'
            return f'{self.url_home}{url}'

    def get(
            self, url: str, full_url: Optional[str] = None, check_expected_response: bool = True, **kwargs
    ) -> Response:
        _url = self.__get_full_url(url, full_url)
        response = self.session.get(url=_url, **kwargs)

        if check_expected_response:
            self.check_abnormal_response_routine(response)
        return response

    def post(
            self, url: str, full_url: Optional[str] = None, check_expected_response: bool = True, **kwargs
    ) -> Response:
        _url = self.__get_full_url(url, full_url)
        response = self.session.post(url=_url, **kwargs)

        if check_expected_response:
            self.check_abnormal_response_routine(response)
        return response

    @abstractmethod
    def check_abnormal_response_routine(self, response: Response):
        """
        반환된 데이터가 사용 가능한 데이터인지 확인합니다
        포맷 자체의 오류는 검증하지 않으며, 인증, 스로들링 등의 문제가 발생했는지 확인합니다.

        잘못된 응답을 수신했을 경우, RequesterException 또는 상속 오류를 발생합니다.
        """
        pass
