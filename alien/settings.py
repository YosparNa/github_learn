class Settings:
    """一个类，用于存储《外星人入侵》游戏的所有设置。"""

    def __init__(self):
        """初始化游戏的静态设置。"""
        # 屏幕设置
        self.screen_width = 1200  # 屏幕宽度
        self.screen_height = 800  # 屏幕高度
        self.bg_color = (230, 0, 230)  # 背景颜色

        # 飞船设置
        self.ship_limit = 0  # 飞船的数量限制

        # 子弹设置
        self.bullet_width = 3  # 子弹宽度
        self.bullet_height = 15  # 子弹高度
        self.bullet_color = (60, 60, 60)  # 子弹颜色
        self.bullets_allowed = 3  # 允许的最大子弹数量

        # 外星人设置
        self.fleet_drop_speed = 40  # 外星舰队下降速度

        # 游戏加速的速度
        self.speedup_scale = 1.1  # 游戏加速的比例
        # 外星人得分增加的速度
        self.score_scale = 1.5  # 得分增加的比例

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏中动态变化的设置。"""
        self.ship_speed = 1.5  # 飞船的速度
        self.bullet_speed = 2.5  # 子弹的速度
        self.alien_speed = 1.0  # 外星人移动的速度

        # fleet_direction 为 1 时代表右移；-1 代表左移。
        self.fleet_direction = 1  # 外星舰队的移动方向

        # 得分设置
        self.alien_points = 50  # 每个外星人的得分

    def increase_speed(self):
        """增加速度设置和外星人的得分值。"""
        self.ship_speed *= self.speedup_scale  # 飞船速度增加
        self.bullet_speed *= self.speedup_scale  # 子弹速度增加
        self.alien_speed *= self.speedup_scale  # 外星人速度增加

        self.alien_points = int(self.alien_points * self.score_scale)  # 外星人得分增加
