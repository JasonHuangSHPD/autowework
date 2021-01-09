from selenium.webdriver.common.by import By

from test_frame.base_page import BasePage

class Search(BasePage):
    def search(self):
        self.find_and_send(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", 'alibaba')

        return True