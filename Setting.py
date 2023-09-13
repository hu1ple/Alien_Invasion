
class Setting:
    """"存储《外星人入侵》所有设置的类"""
    def __init__(self):
        """"初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞行速度
        self.ship_speed_factor = 1.5
