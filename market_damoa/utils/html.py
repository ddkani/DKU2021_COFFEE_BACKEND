"""
XPath를 이용한 파싱을 위해, 옵션을 지정해 XPath를 빠르게 작성할 수 있도록 돕습니다.
"""

# TODO: 하지만 지정해야 하는 옵션들이 너무 많고 부모 노드 -> 자식 노드의 규격까지 생각한다면 구성이 매우 번거로워질듯
from typing import List

from lxml.html import HtmlElement
from lxml import etree


def get_html_element_inner_html(element: HtmlElement) -> str:
    return etree.tostring(element_or_tree=element, pretty_print=True, method='html').decode(encoding='utf-8')


def get_img_elements_src(element: HtmlElement, attrib_name: str = 'src') -> List[str]:
    src_list = []
    for img_element in element.xpath('//img'):  # type: HtmlElement
        if attrib_name in img_element.keys():
            src_list.append(img_element.attrib[attrib_name])
    return src_list
