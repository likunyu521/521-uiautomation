# -*- coding: utf-8 -*-

from base.page import BasePage
from base.action import ElementActions
from base.utils import log


# 元素定位方式尽量不要xpath，容易很慢(Appium对于xpath定位执行效率是比较低的)
# 已通过find_elements_by_android_uiautomator实现通过name元素定位


class PlantTreeHomePage(BasePage):
    name = "种树首页"

    def pageinto(self, action: ElementActions):
        action.start_activity(self.activity)

    def load_android(self):
        self.activity = "AlipayLogin"
        self.plant_tree_entrance = self.get_locator('蚂蚁森林入口', 'name', '蚂蚁森林')

    def load_ios(self):
        self.search_box = "4455"


class MyTreePage(BasePage):
    name = "我的树页"

    def load_android(self):
        # 元素通过坐标位置点击
        self.energy_positon = self.get_locator('能量位置', 'tap', '987,1483')

        # 找能量button
        self.find_energy_button = self.get_locator('找能量', 'name', '找能量')


class OtherTreePage(BasePage):
    name = "找能量页"

    def load_android(self):
        # 元素通过坐标位置点击
        self.energy_positon = self.get_locator('能量位置', 'tap', '987,1483')
        # 找能量button
        self.return_my_tree_btn = self.get_locator('返回我的树btn', 'name', '返回我的森林')
