# -*- coding: utf-8 -*-
from base.action import ElementActions
from lib.pages.set import ProductPages
from base.verify import NotFoundTextError
# 测试用例demo，pytest框架自动加载执行

class Test_demo():

    def test_home(self, action: ElementActions):

        # up.登录页.login(action,'13550234762','tmhrush2233')

        action.click(ProductPages.sale_home_page.search_box)

        # 因为调用action的大部分公用方法是返回self，所以可以一条语句执行多次不同方法
        action.text(ProductPages.category_list_search_page.search_box, "口红") \
            .click(ProductPages.category_list_search_page.search_button)

        # action.click(ProductPages.search_result_list_page.第一个商品项)

        # 循环下拉，检查是否有对应关键字，找到后终止
        for count in range(3):
            if action.swip_down().is_text_displayed("商品参数"):
                break

        # 没有对应关键字抛出错误
        if not action.is_text_displayed("口红"):
            raise NotFoundTextError

        action.sleep(1)
