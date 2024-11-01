import sys

import pygame

from settings import Settings

from ship import Ship

# 管理游戏资源和行为的类
class AlienInvasion:
    # 初始化游戏，创建游戏资源
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # 创建一个窗口，设置其大小和标题
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星人入侵")
        # 设置背景色
        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)
        
    # 开始游戏的主循环
    def run_game(self):
        while True:
            # 侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 让最近绘制的屏幕可见
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # 控制游戏帧率
            self.clock.tick(60)
            # 更新屏幕上的图像，并切换到新屏幕
            pygame.display.flip()

# 创建游戏实例并运行游戏
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()