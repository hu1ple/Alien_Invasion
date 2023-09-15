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
            check_keydown_events(event, ship, ai_settings, bullets=bullets, screen=screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_bullets(bullets, aliens, ai_settings, screen, ship):
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹集中了外星人
    # 如果是这哦哟昂，就删除对应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings=ai_settings, screen=screen, aliens=aliens, ship=ship)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_y(ai_settings, alien_height, ship_height):
    """计算可以容纳多少行外星人"""
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人的间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    number_alien_x = get_number_aliens_x(ai_settings, alien_width)
    number_alien_y = get_number_aliens_y(ai_settings, alien_height, ship.rect.height)
    # 创建第一行外星人
    # create_alien(ai_settings, screen, aliens, 1, 1)
    for alien_number in range(number_alien_x):
        for row_number in range(number_alien_y):
            # 创建一个外星人并将其加入到当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(aliens):
    """更新外星人群中外星人的位置"""
    aliens.update()


def update_screen(ai_settings, screen, ship, bullets, aliens):
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
