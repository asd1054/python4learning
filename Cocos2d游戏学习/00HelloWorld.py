# -*- encoding: utf-8 -*-
'''
@File    :   helloWorld.py
@Time    :   2022/03/26 22:21:46
@Author  :   NMOON 
@Version :   1.0
@Contact :   ay1054@qq.com
@Personal:   应无所往，而生其心
@Function:   
@Desc    :   
'''

# here put the import lib

import cocos

# 自定义层
class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()  # 调用父类方法

        # 创建标签
        label = cocos.text.Label(
            "Hello Nmoon",
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center',
            anchor_y='center',
        )

        # 获取屏幕大小
        width, height = cocos.director.director.get_window_size()
        label.position = width // 2, height // 2

        # 把标签的添加到层
        self.add(label)


if __name__ == '__main__':
    # 创建导演类
    cocos.director.director.init()

    # 创建层对象
    hw_layer = HelloWorld()

    # 创建场景类
    main_screen = cocos.scene.Scene(hw_layer)

    cocos.director.director.run(main_screen)
