class GameStats:
    """跟踪《外星人入侵》游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings  # 获取游戏设置
        self.reset_stats()  # 重置统计信息

        # 最高分不应该被重置。
        self.high_score = 0  # 初始化最高分

    def reset_stats(self):
        """初始化在游戏过程中可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit  # 剩余的飞船数量
        self.score = 0  # 当前得分
        self.level = 1  # 当前关卡
