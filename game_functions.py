import sys
import pygame
from bullet import Bullet
from Alien import Alien


def check_keydown_events(event, ship, ai_settings, bullets, screen):
    """响应按键"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 如果数量未超过限制则创建一颗子弹，并将其加入到编组bullets中
        fire_bullet(ai_settings, bullets, screen, ship)


def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen=screen, ship=ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_events(ship, screen, ai_settings, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, bullets = bullets, screen = screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets):
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人的间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))

    #创建第一行外星人
    for alien_number in range(number_alien_x):
        # 创建一个外星人并将其加入到当前行
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def update_screen(ai_settings, screen, ship, bullets,aliens):
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
