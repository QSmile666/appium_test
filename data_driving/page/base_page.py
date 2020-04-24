# _*_ coding:utf-8 _*_
# @author: zhenhualee
# @time: 2020/4/16 9:21 上午

from time import sleep
from typing import List, Dict

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage():
    # 黑名单设置的是页面的弹窗
    _black_list = [(By.ID, "image_cancel")]
    _error_count = 0
    _error_max = 10
    _params = {}

    # 初始化时设置的必须传入一个driver，可以设置为 不传
    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    # find((By.ID, "name"))  这种就是传了一个tuble (By.ID, "name")
    def find(self, by, locator=None):
        try:
            # 如果传的是一个tuble则使用 find_elements方法 ；非tuble则使用find_element方法
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                              locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            else:
                for black in self._black_list:
                    elements = self._driver.find_elements(*black)
                    if len(elements) > 0:
                        elements[0].click()
                        return self.find(by, locator)
                raise e
    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            # 如果找到了就把次数重置为0
            self._error_count = 0
        except Exception as e:
            self._error_count += 1
            if self._error_count >= self._error_max:
                raise e
            else:
                for black in self._black_list:
                    elements = self._driver.find_elements(*black)
                    if len(elements) > 0:
                        elements[0].click()
                        return self.send(value, by, locator)
                raise e

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps: List[Dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self._driver.find_element(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content: str = step["value"]
                        for param in self._params:
                            # 如果定义的字典里面的值命中了yaml文件中的"{value}"，那么就将字典里面的值替换为"{value}"
                            content = content.replace("{%s}" % param, self._params[param])
                        self.send(content, step["by"], step["locator"])
