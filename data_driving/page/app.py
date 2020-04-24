# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/16 11:15 上午
from appium import webdriver

from data_driving.page.base_page import BasePage
from data_driving.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = "com.xueqiu.android.common.MainActivity"

        if self._driver is None:
            desire_caps = {}
            desire_caps["platformName"] = "android"
            desire_caps["deviceName"] = "emulator-5554"
            desire_caps["deviceVersion"] = "6.0"
            desire_caps["appPackage"] = _package
            desire_caps["appActivity"] = _activity
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_caps)
            self._driver.implicitly_wait(5)

        else:
            # 复用driver进行启动
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)
