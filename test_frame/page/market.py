from test_frame.base_page import BasePage
from selenium.webdriver.common.by import By
from test_frame.page.search import Search
import yaml

class Market(BasePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        # with open("../page/market.yaml", encoding="utf-8") as f:
        #     data = yaml.load(f)
        #     # step find, action
        # for step in data:
        #     xpath_expr = step.get("find")
        #     action = step.get("action")
        #     if action == "find_and_click":
        #         self.find_and_click(By.XPATH, xpath_expr)
        self.load("../page/market.yaml")
        return Search(self.driver)
