import json

class GameStats:
    """跟踪《外星人入侵》游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings  # 获取游戏设置
        self.reset_stats()  # 重置统计信息

        # 加载最高分
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """初始化在游戏过程中可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit  # 剩余的飞船数量
        self.score = 0  # 当前得分
        self.level = 1  # 当前关卡

    def load_high_score(self):
        """从 JSON 文件加载最高分。"""
        try:
            with open("high_score.json", "r") as file:
                data = json.load(file)
                return data.get("high_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0  # 如果文件不存在或者解析出错，则返回默认值 0

    def save_high_score(self):
        """将最高分保存到 JSON 文件。"""
        with open("high_score.json", "w") as file:
            json.dump({"high_score": self.high_score}, file)

    def check_high_score(self):
        """检查是否达到新的最高分，并保存。"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
