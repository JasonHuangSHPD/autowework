import pytest
import requests


def get_token():
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwf06a4f12f22063c3&corpsecret=7B8FtCTSp0JHsZq1d_l2_tp78eLSVwqLAK4x9IBlJoY')
    return r.json()['access_token']


@pytest.mark.parametrize("tmp", range(20))
def test_defect_member(tmp):
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=999aaaa'
    r = requests.get(get_member_url)
    print(r.json())
    assert '张三' == r.json()['name']


def test_update_member():
    update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}'
    date = {
        "userid": "999aaaa",
        "name": "张三",
        "mobile": "13300009999"
    }
    r = requests.post(update_member_url, json=date)
    print(r.json())


def test_create_member():
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    date = {
        "userid": "zhangsan00121",
        "name": "张三好",
        "mobile": "+86 13800006789",
        "department": [1, 1]
    }
    r = requests.post(create_member_url, json=date)
    print(r.json())


def test_delete_member():
    delete_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan00121'
    r = requests.get(delete_member_url)
    print(r.json())

