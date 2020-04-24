# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/18 8:14 下午
from appium_shizhan.three.page.addressListPage import AddressListPage
from appium_shizhan.three.page.base_page import BasePage

# 应用的首页
class Main(BasePage):
    def goto_message(self):
        pass

    def goto_addressList(self):
        return AddressListPage(self._driver)
        pass

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
