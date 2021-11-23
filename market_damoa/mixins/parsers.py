import lxml.html
from lxml.html import HtmlElement


class HTMLParserBase:
    """
    HTML 문서 데이터 파싱을 위한 클래스 베이스입니다.
    """

    # 파서의 경우, 매 메서드의 호출마다

    @classmethod
    def prepare_html(cls, html: str) -> HtmlElement:
        return lxml.html.document_fromstring(html)

    # TODO: 이외에도 lxml 라이브러리에 대한 유틸성 메서드가 필요할 것임. 해당 메서드들을 작성한다.
    # ex) lxml - xpath 데이터 로드하는 부분?
    # 먼저 데이터 파일 로드
