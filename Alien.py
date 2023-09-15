import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像， 并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 存储外星人的运动方向
        self.direction = 1


    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新外星人位置"""
        next_x = self.rect.x + self.direction * self.ai_settings.alien_speed_factor
        if next_x > self.ai_settings.screen_width or next_x < 0:
            self.y = self.rect.y + self.ai_settings.fleet_drop_speed
            self.direction = -self.direction

        else:
            self.x = next_x
        self.rect.x = self.x
        self.rect.y = self.y

