import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """管理飞船的类。"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置。"""
      
        super().__init__()
        self.screen = ai_game.screen  # 获取游戏屏幕
        self.settings = ai_game.settings  # 获取游戏设置
        self.screen_rect = ai_game.screen.get_rect()  # 获取屏幕的矩形区域

        # 加载飞船图像并获取其矩形区域。
        self.image = pygame.image.load('alien\images\ship.bmp')  # 加载飞船图像
        self.rect = self.image.get_rect()  # 获取飞船图像的矩形区域

        # 每个新飞船都从屏幕底部中间的位置开始。
        self.rect.midbottom = self.screen_rect.midbottom  # 设置飞船初始位置为屏幕底部中间

        # 存储飞船的精确水平位置（浮动值）。
        self.x = float(self.rect.x)  # 使用浮动值来表示飞船的水平位置

        # 移动标志；初始时飞船不动。
        self.moving_right = False  # 向右移动标志
        self.moving_left = False  # 向左移动标志

    def center_ship(self):
        """将飞船居中于屏幕。"""
        self.rect.midbottom = self.screen_rect.midbottom  # 将飞船位置设置为屏幕底部中间
        self.x = float(self.rect.x)  # 更新飞船的精确水平位置

    def update(self):
        """根据移动标志更新飞船的位置。"""
        # 更新飞船的x值，而不是直接更新rect。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # 向右移动
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed  # 向左移动
            
        # 根据self.x更新rect对象的x值。
        self.rect.x = self.x  # 更新飞船的矩形区域位置

    def blitme(self):
        """在当前位置绘制飞船。"""
        self.screen.blit(self.image, self.rect)  # 在屏幕上绘制飞船
