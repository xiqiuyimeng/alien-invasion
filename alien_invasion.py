# -*- coding: utf-8 -*-
import pygame
from my_game.settings import Settings
from my_game.ship import Ship
from my_game.game_states import GameStates
from my_game import game_functions as gf
from pygame.sprite import Group
from my_game.button import Button
from my_game.scoreboard import Scoreboard
_author_ = 'luwt'
_date_ = '2018/8/29 22:25'


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStates(ai_settings)
    score = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一群外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, score, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, score, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets,
                             score)
        gf.update_screen(ai_settings, screen, stats, score, ship, aliens, bullets,
                         play_button)


run_game()
