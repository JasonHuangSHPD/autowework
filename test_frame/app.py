from appium import webdriver

from test_frame.base_page import BasePage
from test_frame.page.main import Main


class App(BasePage):
    def start(self):
        if self.driver is None:
            # 启动app
            # 定义一个字典
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            # caps["ensureWebviewsHavePages"] = True
            # 不停止应用，直播运行测试用例
            # caps["dontStopAppOnReset"] = "true"
            # 设置页面等待空闲状态的时间
            # caps["skipDeviceInitialization"] = "true"
            # caps["skipServerInstallation"] = "true"
            # caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待，面向全局，只针对find方法
            self.driver.implicitly_wait(6)

        else:
            self.driver.launch_app()
            # self.driver.start_activity(package, activity)
        return self

    def restart(self):
        #重启APP
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        self.driver.quit()


    def goto_main(self):
        return Main(self.driver)