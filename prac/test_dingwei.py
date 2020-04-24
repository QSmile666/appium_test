# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/12 3:35 下午

from appium import webdriver

desire_caps = {}
desire_caps["platformName"] = "android"
desire_caps["platformVersion"] = "6.0.1"
desire_caps["deviceName"] = "emulator-5554"
desire_caps["appPackage"] = "com.xueqiu.android"
desire_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
desire_caps["noReset"] = "true"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
driver.implicitly_wait(10)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")

driver.quit()
