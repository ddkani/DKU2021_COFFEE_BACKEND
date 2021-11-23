from market_damoa.mixins.parsers import HTMLParserBase
from market_damoa.utils.html import get_html_element_inner_html, get_img_elements_src
from market_damoa.utils.regex import rx_find_single_group, rx_findall_single_group, rx_find_multiple_group, rx_findall_multiple_groups


class MallNaverShoppingParser(HTMLParserBase):
    pass