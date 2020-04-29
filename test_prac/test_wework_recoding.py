# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/15 9:16 下午
from time import sleep
import pytest
from appium import webdriver

'''
作业：使用 Appium Inspector 录制企业微信搜索功能的测试用例，搜索一个存在的联系人。

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
使用录制功能完成上面的功能，
进行简单的重构，使用 pytest 测试框架。
可以加入参数化，实现多条搜索功能的测试用例。
'''


class TestWeworkRecoding():
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
        el8 = self.driver.find_element_by_id("com.tencent.wework:id/gpp")
        el8.click()
        # self.driver.quit()

    @pytest.mark.parametrize('search_key, send_message', [
        ('xiaohua', '测试code'),
        ('李振华', '测试code')
    ])
    def test_search(self, search_key, send_message):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/gq_")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/ffq")
        el2.click()
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/ffq")
        el3.send_keys(search_key)
        el3.click()
        # 这里需要改为 相对定位  绝对定位实际应用中比较少
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.TextView")
        el4.click()
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout")
        el5.click()
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/dtv")
        el6.send_keys(send_message)
        el7 = self.driver.find_element_by_id("com.tencent.wework:id/dtr")
        el7.click()
        sleep(2)
