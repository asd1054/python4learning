from cocos.scene import Scene
from cocos.director import director
from cocos.menu import *


# 自定义菜单
class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__()

        self.font_item['font_size'] = 32
        self.font_item_selected['font_size'] = 40

        item1 = MenuItem('开始', self.on_item1_callback)
        item2 = ToggleMenuItem('开始', self.on_item2_callback, False)

        self.create_menu(
            [item1, item2], selected_effect=shake(), unselected_effect=shake_back()
        )

    def on_item1_callback(self):
        print('on_item1_callback')

    def on_item2_callback(self, V):
        print('on_item2_callback', V)


if __name__ == '__main__':
    # 初始化导演对象
    director.init()
    main_menu = MainMenu()
    # 创建场景实例
    main_scene = Scene(main_menu)

    # 运行
    director.run(main_scene)
