import pytest

from test_requests.rep_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        self.userid = "dingding"
        self.name = "hello_today"

    @pytest.mark.parametrize("corpid, corpsecret, result", [(None, None, 0), ('XXX', None, 40013), (None, 'XXX', 40001)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get('errcode') == result
        # r = self.contact.get_toden()

    def test_create(self):
        userid = "dingding"
        name = "hello_today"
        self.contact.create_member(userid=self.userid, name=self.name, mobile="17899998888", department=[1], alias="XXX")
        try:
            find_result = self.contact.find_member(userid)
        finally:
            self.contact.delete_member(userid)
        assert find_result["name"] == name

    def test_update(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile="17899998888", department=[1], alias="XXX")
        changed_mobile = "13311112222"
        r = self.contact.update_member(self.userid, self.name, changed_mobile)
        print(r)
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        print(find_result)
        assert find_result["mobile"] == changed_mobile


    def test_delete(self):
        pass

    def test_find(self):
        r = self.contact.find_member("999aaaa")
        print(r)


