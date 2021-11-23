"""
외부 데이터 요청 과정에서 발생할 수 있는 보편적인 오류들에 대해 정의합니다.
"""

# TODO: 필요한 경우, 해당 상황을 설명하는데 필요한 exception 페이로드를 추가합니다.


class RequesterException(Exception):
    """
    Requester에서 발생하는 오류의 최상위 클래스입니다.
    """

    kwargs = None  # type: dict

    def __init__(self, **kwargs):
        super().__init__()
        self.kwargs = kwargs


class ResourceNotFoundException(RequesterException):
    """
    요청한 데이터가 존재하지 않거나 삭제된 경우입니다.
    """
    pass


class SessionNotAuthenticatedException(RequesterException):
    """
    사용자의 세션이 인증되지 않은 것으로 확인되었을 때 발생합니다.
    """
    pass


class LimitTemporaryReachedException(RequesterException):
    """
    사용자의 요청이 일시적으로 차단되었을 때 발생합니다.
    """
    pass


class LimitPermanentlyReachedException(RequesterException):
    """
    사용자의 요청이 영구적으로 차단되었을 때 발생합니다.
    - 반드시 영구적이 아니더라도, 약 하루 이상의 당장 해결할 수 없는 차단이 발생한 경우도 포함됩니다.
    """
    pass
