import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_frame.black_handle import black_wrapper


class Black:
    def __init__(self):
        pass

class BasePage:
    FIND = "find"
    ACTION = "action"
    FIND_AND_CLICK = "find_and_click"
    FIND_AND_SEND = "find_and_click"
    CONTENT = "content"


    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

        """
        try:
            return self.driver.find_element(by, locator)
        # 捕获元素没找到异常
        except Exception as e:
            # 遍历黑名单中的元素，进行处理
            for black in self.black_list:
                eles = self.finds(*black)
                if len(eles) > 0:
                    # 对黑名单进行点击，可以扩展
                    eles[0].click()
                    return self.find(by, locator)
            raise e
            
        """

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)


    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def swipe_find(self, by, locator):
        # 查找全部元素
        count = 0
        self.driver.implicitly_wait(1)
        elements = self.finds(by, locator)
        while len(elements) == 0 or count <= 3:
            # 一直在滑动
            self.driver.swipe(0, 600, 0, 400)
            elements = self.finds(by, locator)
            count += 1
        self.driver.implicitly_wait(5)
        return elements[0]

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      f'text("{text}").instance(0));')

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def find_and_send(self, by, locator, content):
        self.find(by, locator).send_keys(content)

    def wait_for(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return result

    def load(self, yaml_path):
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.load(f)
            # step find, action
        for step in data:
            xpath_expr = step.get(self.FIND)
            action = step.get(self.ACTION)
            content = step.get(self.CONTENT)
            if action == self.FIND_AND_CLICK:
                self.find_and_click(By.XPATH, xpath_expr)
            elif action == self.FIND_AND_SEND:
                self.find_and_send(By.XPATH, xpath_expr, content)

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)