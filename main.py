import pygame as pg
from snake import SnakeOne
from point import Point

from settings import (
    width,
    height,
    frame_num,
    speed_frame_num
)
from global_func import (
    collision_detection
)


class Main(object):

    def __init__(self):
        self.exit_flag = False

        pg.init()
        pg.display.init()
        pg.font.init()
        # 屏幕对象
        self.screen = pg.display.set_mode(size=(width, height))
        # 帧率对象
        self.clock_obj = pg.time.Clock()
        # 点对象
        self.point_obj = Point()
        # 第一节蛇对象
        self.snake_obj = SnakeOne(self.screen)

    def draw(self):
        # 背景图
        self.screen.fill((200, 248, 254))
        # 点
        self.point_obj.draw(self.screen)
        # 主蛇渲染
        self.snake_obj.draw(self.point_obj)
        # 副蛇渲染
        obj = self.snake_obj.next
        while obj:
            obj.draw()
            obj = obj.next
        # 得分
        font = pg.font.SysFont("font1", size=30)
        text = font.render("Score: %s" % self.snake_obj.score, 1, (0, 0, 0))
        self.screen.blit(text, (3, 3))
        # 渲染画面
        pg.display.update()
        # 主蛇得边界的碰撞检测
        if self.snake_obj.x > width or self.snake_obj.x < 0 or self.snake_obj.y > height or self.snake_obj.y < 0:
            # 游戏重新开始
            self.__init__()
        # 主蛇和身体的碰撞检测
        if self.snake_obj.next:
            body_obj = self.snake_obj.next
            while body_obj.next:
                flag = collision_detection(self.snake_obj, body_obj)
                if flag:
                    # 游戏重新开始
                    self.__init__()
                    break
                body_obj = body_obj.next

    def run(self):
        frame = frame_num

        while not self.exit_flag:
            # 帧率
            self.clock_obj.tick(frame)
            # 事件
            for event in pg.event.get():
                # 退出事件
                if event.type == pg.QUIT:
                    self.exit_flag = True
                elif event.type == pg.KEYDOWN:
                    # 蛇的上下左右
                    if event.key == pg.K_UP:
                        if self.snake_obj.direction != 'down':
                            self.snake_obj.change_direction('up')
                    elif event.key == pg.K_DOWN:
                        if self.snake_obj.direction != 'up':
                            self.snake_obj.change_direction('down')
                    elif event.key == pg.K_LEFT:
                        if self.snake_obj.direction != 'right':
                            self.snake_obj.change_direction('left')
                    elif event.key == pg.K_RIGHT:
                        if self.snake_obj.direction != 'left':
                            self.snake_obj.change_direction('right')
            # 持续监测按键
            if pg.key.get_pressed()[pg.K_SPACE]:
                frame = speed_frame_num
            else:
                frame = frame_num
            # 渲染
            self.draw()


if __name__ == '__main__':
    Main().run()
