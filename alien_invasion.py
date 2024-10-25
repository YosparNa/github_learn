import sys

import pygame

class AlienInvasion:
    # 管理游戏资源和行为的类
    def __init__(self):
        # 初始化游戏，创建游戏资源
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
    def run_game(self):
        # 开始游戏的主循环
        while True:
            # 侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 更新屏幕上的图像，并切换到新屏幕
            pygame.display.flip()
            # 控制游戏帧率
            self.clock.tick(60)

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()