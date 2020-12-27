from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.address_list_page import AddresssListPage
from test_appium.po.page.base_page import BasePage


class MainPage(BasePage):
    def goto_address(self):
        # todo
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']")
        return AddresssListPage(self.driver)