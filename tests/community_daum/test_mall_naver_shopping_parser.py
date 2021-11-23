 import os

import pytest

from community_daum.parsers import DaumCafeParser
from tests.community_daum import RESOURCE_ROOT


@pytest.mark.parametrize(
    'html_file', ['first_page', 'next_n_page', 'with_notice_page']
)
def test_parse_board_post_id_list(html_file):
    html = open(f'{RESOURCE_ROOT}/board_post_id_list/{html_file}.html', 'r', encoding='utf8').read()
    post_ids, first_bbs_depth, last_bbs_depth = DaumCafeParser.parse_board_post_id_list(html)

    # 일반적인 첫번째 페이지 파싱
    if html_file == 'first_page':
        assert post_ids == {230490, 230489, 230488, 230487, 230485, 230484,
                            230483, 230481, 230480, 230478, 230475, 230474,
                            230473, 230472, 230470, 230468, 230465, 230462,
                            230458, 230456}
        assert first_bbs_depth == '00xxazzzzzzzzzzzzzzzzzzzzzzzzz'
        assert last_bbs_depth == '00xx2zzzzzzzzzzzzzzzzzzzzzzzzz'

    # bbs_depth 정보가 있는 N번째 페이지
    elif html_file == 'next_n_page':
        assert post_ids == {230455, 230453, 230452, 230450, 230449, 230446,
                            230445, 230444, 230442, 230439, 230434, 230432,
                            230430, 230429, 230428, 230427, 230425, 230422,
                            230421, 230419}
        assert first_bbs_depth == '00xx1zzzzzzzzzzzzzzzzzzzzzzzzz'
        assert last_bbs_depth == '00xwRzzzzzzzzzzzzzzzzzzzzzzzzz'

    # 공지글이 포함되어 있는 페이지
    elif html_file == 'with_notice_page':
        # NOTI 게시물 제회
        assert post_ids == {41502552, 38298897, 42040323, 42040322, 42040321,
                            42040320, 42040319, 42040318, 42040317, 42040316,
                            42040315, 42040313, 42040312, 42040311, 42040310,
                            42040309, 42040307, 42040306, 42040305, 42040304,
                            42040303, 42040302} - {38298897, 41502552}
        assert first_bbs_depth == '2qObjzzzzzzzzzzzzzzzzzzzzzzzzz'
        assert last_bbs_depth == '2qObOzzzzzzzzzzzzzzzzzzzzzzzzz'


@pytest.mark.parametrize(
    'html_file', ['post_with_image_and_comment']
)
def test_parse_board_post(html_file):
    html = open(f'{RESOURCE_ROOT}/board_post/{html_file}.html', 'r', encoding='uafeParser.parse_tf8').read()
    post, post_attachments, post_body_embedded, comment_and_attachments = DaumCafeParser.parse_board_post(html)
    # TODO: 검증 코드 작성

    if html_file == 'post_with_image_and_comment':
        pass


@pytest.mark.parametrize(
    'html_file', ['comment_page']
)
def test_parse_comment_list(html_file):
    html = open(f'{RESOURCE_ROOT}/comment_list/{html_file}.html', 'r', encoding='utf8').read()
    comment_and_attachments = DaumCafeParser.parse_comment_list(html)
