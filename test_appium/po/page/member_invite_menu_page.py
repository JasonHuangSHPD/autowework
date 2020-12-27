from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.contact_add import ContactAdd


class MemberInviteMenuPage(BasePage):

    def add_member_manual(self):

        # todo
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAdd(self.driver)
