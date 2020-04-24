# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/16 8:22 下午

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAddContract():
    def setup(self):
        _appPackage = "com.tencent.wework"
        _appActivity = "com.tencent.wework.launch.WwMainActivity"
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["deviceVersion"] = "6.0.1"
        desire_caps["appPackage"] = _appPackage
        desire_caps["appActivity"] = _appActivity
        desire_caps["noReset"] = "True"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        pass

    def test_addcontract(self):
        # 进入到通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 滚动查找 添加成员

