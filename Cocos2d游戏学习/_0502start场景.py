from cocos.scene import Scene
from cocos.director import director
from cocos.menu import *
from cocos.layer import Layer
from cocos.sprite import Sprite
import pyglet


class StartLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super().__init__()

        self.s_width, self.s_height = director.get_window_size()

        # 背景精灵
        start_background = Sprite('img/night.png')
        start_background.position = self.s_width // 2, self.s_height // 2
        self.add(start_background, 1)


class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        chushi = MenuItem('返回初始页面', self.on_chushi_callback)
        chushi2 = MenuItem('return chushi!!!!!!', director.pop)

        self.create_menu(
            [chushi, chushi2],
            selected_effect=shake(),
            unselected_effect=shake_back(),
            layout_strategy=fixedPositionMenuLayout([(230, 230), (320, 320)]),
        )

    def on_chushi_callback(self):
        # print('on_item1_callback')
        director.pop()


def create_scene():
    # 创建场景
    scene = Scene(StartLayer())
    scene.add(MainMenu())
    return scene

