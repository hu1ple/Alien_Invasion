
import pygame
from Setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Alien import Alien


def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    # 创建一艘飞船
    ship = Ship(screen, setting)
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人群
    aliens = Group()
    gf.create_fleet(setting, screen, aliens)
    # 开始游戏的主循环
    while True:
        gf.check_events(ship, ai_settings=setting, bullets=bullets, screen=screen)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(setting, screen, ship, bullets,aliens)


run_game()
