# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/14 5:14 下午
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to
import pytest


class TestWebDriverWait():
    def setup(self):
        desire_caps = {}
        desire_caps['platformName'] = 'android'
        desire_caps['platformVersion'] = '6.0.1'
        desire_caps['deviceName'] = 'emulator-5554'
        desire_caps['appPackage'] = 'com.xueqiu.android'
        desire_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    @pytest.mark.parametrize('search_key, type, expect_price', [
        ('alibaba', 'BABA', 190),
        ('xiaomi', '01810', 10)
    ])
    def test_search(self, search_key, type, expect_price):
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(search_key)
        # self.driver.find_element(MobileBy.XPATH, f"//*[@text='{type}']").click()
        price_element = self.driver.find_element(MobileBy.XPATH,
                                                 f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(price_element.text)
        # expected_price = 190
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))
