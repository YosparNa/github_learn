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
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("退出事件被触发")
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    print("Q键被按下")
                    pygame.quit()
                    sys.exit()
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        
        
# 创建游戏实例并运行游戏
if __name__ == '__main__':
    print("游戏开始运行")  # 测试打印是否正常
    ai = AlienInvasion()
    ai.run_game()