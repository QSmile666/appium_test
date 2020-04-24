# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/16 2:37 下午
from data_driving.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps("../page/search.yaml")
        return
