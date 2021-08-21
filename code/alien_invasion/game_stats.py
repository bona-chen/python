import json

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 让游戏刚启动时属于非活动状态
        self.game_active = False

        # 加载最高得分
        try:
            with open("high_score", "r+") as file:
                self.high_score = json.load(file)
        except FileNotFoundError:
            self.high_score = 0
            with open("high_score", "w") as file:
                json.dump(self.high_score, file)

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
