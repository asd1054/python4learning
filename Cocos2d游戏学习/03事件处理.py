from cocos.scene import Scene
from cocos.director import director
from cocos.layer import Layer
from cocos.text import Label
import pyglet


class LLayer(Layer):
    is_event_handler = True  # 开启键盘监听

    def __init__(self):
        super(LLayer, self).__init__()

        label = Label(
            "Hello Nmoon",
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center',
            anchor_y='center',
        )

        label.position = 300, 400
        self.add(label)

    def on_key_press(self, key, modifiers):
        print("键盘释放", key, '   ---', modifiers)
        if key == pyglet.window.key.SPACE:
            print("你按下了空格键")

    def on_key_release(self, key, modifiers):
        print("键盘释放", key, '   ---', modifiers)

    def on_mouse_motion(self, x, y, dx, dy):  # 可用来在屏幕上定位
        print("1 === ", x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print("2 === ", x, y, dx, dy, buttons, modifiers)

    def on_mouse_press(self, x, y, buttons, modifiers):
        print("3 === ", x, y, buttons, modifiers)


if __name__ == '__main__':

    director.init(width=800, height=600, caption='事件处理')
    layer1 = LLayer()
    main_scene = Scene(layer1)
    director.run(main_scene)
