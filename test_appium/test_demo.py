# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
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
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demmo(self):
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/"
            "android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/"
            "android.widget.TextView")
        el3.click()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.
                                 ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
#        print(self.driver.page_source)
        # 显示等待，如果10S内找到这个元素，则直接断言，否则需要等待10S，匿名函数
        WebDriverWait(self.driver, 10, 0.5).until(lambda x:"外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source


if __name__ == '__main__':
    pytest.main(['test_demo.py'], '-v')

