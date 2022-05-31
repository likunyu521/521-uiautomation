# -*- coding: utf-8 -*-
from base.action import ElementActions
from lib.pages.set import PlantTreePages
from base.verify import NotFoundTextError
# 测试用例demo，pytest框架自动加载执行

class Test_demo():
    def get_screen_size(self, action: ElementActions):
        x = action.driver.get_window_size()['width']  # 获取屏幕宽度
        y = action.driver.get_window_size()['height']  # 获取屏幕高度
        return (x, y)
    def tap_alone(self, action: ElementActions,x,y,duration=1000):
        l = self.get_screen_size(action)
        width = int(l[0])  # 获取屏幕宽度
        height = int(l[1])  # 获取屏幕高度
        tap_x1 = int((int(x) / width) * width)
        tap_y1 = int((int(y) / height) * height)
        print('点击坐标:['+str(tap_x1)+', '+str(tap_y1)+']')
        action.driver.tap([(tap_x1, tap_y1), (tap_x1, tap_y1)], duration)

    def tap_next(self, action: ElementActions,x=1000,y=1600,duration=1000):
        l = self.get_screen_size(action)
        width = int(l[0])  # 获取屏幕宽度
        height = int(l[1])  # 获取屏幕高度
        tap_x1 = int((int(x) / width) * width)
        tap_y1 = int((int(y) / height) * height)
        print('点击【找能量】')
        action.driver.tap([(tap_x1, tap_y1), (tap_x1, tap_y1)], duration)


    def tap_get_energy(self, action: ElementActions):
        # 能量球可能出现的区域坐标
        start_x = 200
        start_y = 560
        end_x = 920
        end_y = 870

        print('开始收取能量>>>')
        # 依次点击指定区域内的等距离坐标点
        for i in range(start_y,end_y,80):
            for j in range(start_x,end_x,80):
                print('['+str(j)+', '+str(i)+']',"\t", end="")
                self.tap_alone(action,j,i)
            print()
    def test_home(self, action: ElementActions):
        action.click(PlantTreePages.plant_tree_home_page.plant_tree_entrance)
        # 点击找能量
        print("收集自己能量")
        self.tap_get_energy(action)
        self.tap_next(action)
        action.sleep(5)

        # 找能量按钮点击
        # action.click(PlantTreePages.my_tree_page.find_energy_button)

        while not action.is_text_displayed("返回我的森林"):
            print("收集朋友能量")
            self.tap_get_energy(action)
            self.tap_next(action)

        #         break
        action.sleep(1)

