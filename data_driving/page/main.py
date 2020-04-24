# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/16 9:21 上午
from data_driving.page.base_page import BasePage
from data_driving.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 为什么要用上一个目录呢？因为最终是在 testcase这个目录下调用的，并不是在page这个目录下调用。
        self.steps("../page/main.yaml")
        return Market(self._driver)
