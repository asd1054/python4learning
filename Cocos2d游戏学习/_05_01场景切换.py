from cocos.scene import Scene
from cocos.director import director
from cocos.menu import *
from cocos.layer import Layer
from cocos.sprite import Sprite
import pyglet
from cocos.scenes import transitions
import _0502start场景


class GameLayer(Layer):
    is_event_handler = True

    def __init__(self):
        super(GameLayer, self).__init__()

        self.s_width, self.s_height = director.get_window_size()

        # 背景精灵
        background = Sprite('img/background.jpeg')
        background.position = self.s_width // 2, self.s_height // 2
        self.add(background, -1)

    def on_mouse_press(self, x, y, buttons, modifiers):
        print("3 === ", x, y, buttons, modifiers)


class GameMenu(Menu):
    def __init__(self):
        super(GameMenu, self).__init__()

        start_item = ImageMenuItem('img/guide.png', self.on_start_item)

        self.create_menu(
            [start_item], layout_strategy=fixedPositionMenuLayout([(230, 150)])
        )

    def on_start_item(self):
        new_scene = _0502start场景.create_scene()
        director.push(transitions.JumpZoomTransition(new_scene))


if __name__ == '__main__':
    director.init()

    main_scene = Scene(GameLayer())
    main_scene.add(GameMenu())
    director.run(main_scene)

