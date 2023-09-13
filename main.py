import sys
import pygame
from Setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    # 创建一艘飞船
    ship = Ship(screen)
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events()
        bullets.update()
        gf.update_screen(setting, screen, ship)
       

run_game()
