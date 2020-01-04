import pygame as pg

from settings import (
    lattice_size,
    black_image,
    gray_image
)
from global_func import (
    collision_detection
)


class Snake(object):

    def __init__(self, screen):
        self.screen = screen
        # 蛇每格大小
        self.width = lattice_size
        self.height = lattice_size
        # 速度
        self.speed = 20
        # 下一个小蛇对象
        self.next = None
        # 上一个
        self.front = None

    def return_surface(self):
        return self.snake

    def up(self):
        self.y -= self.speed

    def down(self):
        self.y += self.speed

    def left(self):
        self.x -= self.speed

    def right(self):
        self.x += self.speed


class SnakeOne(Snake):

    def __init__(self, screen):
        super().__init__(screen)
        # 图片
        self.snake = pg.image.load(black_image)
        # 主蛇初始位置
        self.direction = 'right'
        self.x = 60
        self.y = 60
        # 分数
        self.score = 0

    def change_direction(self, direction):
        # 自己的方向改变
        self.direction = direction
        # 下个蛇
        if self.next:
            self.next.start_flag = True

    def draw(self, point_obj):
        # 点的碰撞检测
        flag = collision_detection(self, point_obj)
        if flag is True:
            # 加分
            self.score += 10
            # 点位重置
            point_obj.init_position()
            # 添加蛇
            if self.next is not None:
                obj = self.next
                while obj.next is not None:
                    obj = obj.next
                obj.next = SnakeTwo(obj)
            else:
                self.next = SnakeTwo(self)
        # 根据方向移动
        getattr(self, self.direction)()
        # 渲染
        self.screen.blit(self.snake, (self.x, self.y))


class SnakeTwo(Snake):

    def __init__(self, front_obj):
        # 父类的初始化
        super().__init__(front_obj.screen)
        # 图片
        self.snake = pg.image.load(gray_image)
        # 上一段蛇
        self.front = front_obj
        # 使用两层锁，达到一帧一帧改变
        # 开始改变标志
        self.start_flag = False
        # 改变方向标志
        self.change_flag = False
        # 记录位置，有可能连续改变两次，使用列表方式存放
        self.temp_direction = []
        # 初始位置
        self.direction = front_obj.direction
        if self.direction is 'up':
            self.x = front_obj.x
            self.y = front_obj.y + self.height
        elif self.direction is 'down':
            self.x = front_obj.x
            self.y = front_obj.y - self.height
        elif self.direction is 'left':
            self.x = front_obj.x + self.width
            self.y = front_obj.y
        else:
            self.x = front_obj.x - self.width
            self.y = front_obj.y

    def change_direction(self):
        # 先记录位置
        self.temp_direction.append(self.front.direction)

        if self.change_flag:
            # 自己的方向跟随上个蛇方向
            self.direction = self.temp_direction.pop(0)
            # 告知下个蛇需要改变位置
            if self.next:
                self.next.start_flag = True
            if not self.temp_direction:
                # 自己的方向改变完毕，重置标志位
                self.start_flag = False
                self.change_flag = False
        else:
            self.change_flag = True

    def draw(self, point_obj):
        # 改变位置
        if self.start_flag:
            self.change_direction()
        # 根据方向移动
        getattr(self, self.direction)()
        # 渲染
        self.screen.blit(self.snake, (self.x, self.y))
