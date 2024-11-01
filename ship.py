import pygame  # 导入pygame库

class Ship:
    """管理飞船的类"""
    
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置
        参数:
        ai_game: AlienInvasion类的实例，用于访问屏幕对象
        """
        self.screen = ai_game.screen  # 获取游戏屏幕对象
        self.screen_rect = ai_game.screen.get_rect()  # 获取屏幕的矩形区域
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('python_alien_invasion\images\ship.bmp')  # 加载飞船图像
        # 改变飞船大小
        self.image = pygame.transform.scale(self.image, (80, 60))  # 调整飞船图像大小
        self.rect = self.image.get_rect()  # 获取飞船图像的矩形区域
        
        # 每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom  # 设置飞船的位置为屏幕底部中央

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 在屏幕上绘制飞船