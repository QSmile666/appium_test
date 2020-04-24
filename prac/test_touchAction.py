# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/13 10:53 上午
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction():
    # 测试用例前执行一次
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["platformVersion"] = "6.0.1"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "com.xueqiu.android"
        desire_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        desire_caps["noReset"] = "true"
        # 输入中文时调用unicode键盘，使用完成后重置键盘
        desire_caps["unicodeKeyBoard"] = "true"
        desire_caps["resetKeyBoard"] = "true"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touchAction_unlock(self):
        action = TouchAction(self.driver)
        # press后多次移动坐标点 release perform
