import yaml
from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage
from test_frame.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")

        # with open("../page/main.yaml", encoding="utf-8") as f:
        #     data = yaml.load(f)
        #     # step find, action
        # for step in data:
        #     xpath_expr = step.get("find")
        #     action = step.get("action")
        #     if action == "find_and_click":
        #         self.find_and_click(By.XPATH, xpath_expr)
        self.load("../page/main.yaml")
        return Market(self.driver)




