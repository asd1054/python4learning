from cocos.scene import Scene
from cocos.director import director
from cocos.menu import *
from cocos.layer import Layer
from cocos.sprite import Sprite
import pyglet
from cocos.text import Label

#
class GmaerLayer(Layer):
    def __init__(self):
        super(GmaerLayer, self).__init__()

        # 创建精灵图片
        bg = Sprite('img/background.jpeg')
        w, h = director.get_window_size()
        bg.position = w // 2, h // 2

        # 把精灵图片添加层
        self.add(bg)


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__()

        # self.font_item['font_size'] = 120
        # self.font_item_selected['font_size'] = 120

        start_item = ImageMenuItem('img/guide.png', self.on_start_item_callback)
        setting_item = ImageMenuItem('img/guide.png', self.on_setting_item_callback)

        self.create_menu(
            [start_item, setting_item],
            layout_strategy=fixedPositionMenuLayout([(560, 470), (340, 440)]),
        )

    def on_start_item_callback(self):
        print('Game starting !!!')

    def on_setting_item_callback(self):
        print('on_setting_item_callback starting !!!')


if __name__ == '__main__':
    # 初始化导演对象
    director.init(width=700, height=800, caption='图片案例')

    gl = GmaerLayer()

    # 创建场景实例
    main_scene = Scene(gl)

    # 把菜单添加层
    main_scene.add(MainMenu())

    # 运行
    director.run(main_scene)
