from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.po.page.base_page import BasePage


class ContactAdd(BasePage):

    def add_contact(self):

        # todo

        self.find_and_send(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']", '999aaaa')
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")

        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']", '15678909870')

        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        return True
