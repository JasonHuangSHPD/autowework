from selenium.webdriver.remote.mobile import Mobile

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.member_invite_menu_page import MemberInviteMenuPage


class AddresssListPage(BasePage):

    def click_addmember(self):
        self.scroll_find_click("添加成员")
        return MemberInviteMenuPage(self.driver)
