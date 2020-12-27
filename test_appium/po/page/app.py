from appium import webdriver

from test_appium.po.page.base_page import BasePage
from test_appium.po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
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
        else:
            self.driver.launch_app()
        # 隐式等待，面向全局，只针对find方法
        self.driver.implicitly_wait(6)

    def goto_main(self):
        return MainPage(self.driver)