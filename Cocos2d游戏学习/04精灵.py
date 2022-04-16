from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite


class L(Layer):
    def __init__(self):
        super(L, self).__init__()

        self.s_width, self.s_height = director.get_window_size()

        # 背景精灵
        background = Sprite('img/background.jpeg')
        # 设置在窗口什么位置
        background.position = self.s_width // 2, self.s_height // 2
        self.add(background, -1)

        sp1 = Sprite('img/guide.png', position=(360, 300), scale=0.8)  # scale 缩小的尺寸
        self.add(sp1, 1)

        sp2 = Sprite('img/guide.png', position=(160, 200), scale=1.2)  # scale 缩小的尺寸
        self.add(sp2, 2)


if __name__ == "__main__":
    director.init(width=600, height=600, caption='精灵')

    main_scene = Scene(L())

    director.run(main_scene)
