from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webdriver import WebDriver


class TestContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        # 设置页面等待空闲状态的时间
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 隐式等待，面向全局，只针对find方法
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()


    def test_contact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/elq']").click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']").send_keys('aaaa')
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()


        def wait_ele_for(driver: WebDriver):
            eles = driver.find_elements(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys('15678909870')
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
