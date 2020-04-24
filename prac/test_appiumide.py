# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/12 8:31 上午

from appium import webdriver

desire_cap = {
    "platformName": "android",
    "deviceName": "emulator-5554",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
driver.implicitly_wait(10)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
