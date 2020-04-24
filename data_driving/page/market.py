# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/16 2:28 下午
from data_driving.page.base_page import BasePage
from data_driving.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)