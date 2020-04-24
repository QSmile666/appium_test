# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/12 3:35 下午

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    # 测试用例前执行一次
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = "android"
        desire_caps["platformVersion"] = "6.0.1"
        desire_caps["deviceName"] = "emulator-5554"
        desire_caps["appPackage"] = "com.xueqiu.android"
        # desire_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
        desire_caps[
            "appActivity"] = "com.xueqiu.android.stockmodule.quotecenter.activity.QuoteCenterHotStockListActivity"
        desire_caps["noReset"] = "true"
        # 输入中文时调用unicode键盘，使用完成后重置键盘
        desire_caps["unicodeKeyBoard"] = "true"
        desire_caps["resetKeyBoard"] = "true"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        print("搜索测试用例")
        """
        1. 打开雪球app
        2. 点击搜索框
        3. 输入"阿里巴巴"
        4. 搜索结果里选择"阿里巴巴"，然后进行点击
        5. 获取这只 阿里巴巴的股价，并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    @pytest.mark.skip
    def test_attr(self):
        '''
        * 打开【雪球】应用首页
        * 定位首页的搜索框
        * 判断搜索框的是否可用，并查看搜索框name属性值
        * 打印搜索框这个元素的左上角坐标和它的宽高
        * 向搜索框输入：alibaba
        * 判断【阿里巴巴】是否可见
        * 如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        '''
        ele_search = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = ele_search.is_enabled()
        print(ele_search.text)
        print(ele_search.location)
        print(ele_search.size)
        if search_enabled == True:
            ele_search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_ele = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # print(alibaba_ele.is_displayed())    # 结果为  bool值的True
            ele_displayed = alibaba_ele.get_attribute("displayed")  # 结果为  字符串的true
            if ele_displayed == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchAction(self):
        action = TouchAction(self.driver)
        # # print(self.driver.get_window_rect())
        # window_rect = self.driver.get_window_rect()
        # width = window_rect["width"]
        # height = window_rect["height"]
        # x1 = int(width/2)
        # y_start = int(height * 0.8)
        # y_end = int(height * 0.2)
        action.press(x=725, y=2229).wait(2000).move_to(x=725, y=350).release().perform()
        # action.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).release().perform()

        # self.driver.swipe(725, 2229, 725, 350)


if __name__ == '__main__':
    pytest.main()
