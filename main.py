import sys
import pygame
from Setting import Setting
from ship import Ship


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    # 创建一艘飞船
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环时都重绘屏幕
        screen.fill(setting.bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
