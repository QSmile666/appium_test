# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/16 2:46 下午
from data_driving.page.app import App


class TestSearch():
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")
