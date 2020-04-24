# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/15 10:55 上午
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import pytest

"""
作业：使用 Appium 编写企业微信搜索功能的测试用例，搜索一个存在的联系人。

用例步骤：
打开企业微信（提前登录）
进入通讯录
点击搜索按钮
输入 已存在的联系人姓名, 例如“aa”，
点击联系人，进入聊天页面
输入“测试code”
点击发送
退出应用

注意：
提前登录，绕过登录功能
进行简单的重构，使用 pytest 测试框架。
可以加入参数化，实现多条搜索功能的测试用例。
"""


class TestWeixin():
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'android'
        desire_caps['deviceName'] = 'emulator-5554'
        desire_caps['deviceVersion'] = '6.0.1'
        desire_caps['appPackage'] = 'com.tencent.wework'
        desire_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        desire_caps['noReset'] = 'True'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gpp")
        # self.driver.quit()

    @pytest.mark.parametrize('search_key, send_message', [
        ('xiaohua', '测试code'),
        ('李振华', '测试code')
    ])
    def test_search(self, search_key, send_message):
        # self.driver.find_element(MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        # self.driver.find_element(MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq_").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ffq").send_keys(search_key)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.tencent.wework:id/bgh' and @text='生而孤独']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dtv").send_keys(send_message)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/dtr").click()
        # 发送消息也需要强制等待，网络不好时等待消息发出
        sleep(2)
