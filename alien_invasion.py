import sys
import pygame
from pygame.sprite import Group

import game_function as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个用于存储外星人的编组
    aliens = Group() 

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建play按钮
    play_button = Button(ai_settings, screen, "Play")


    #创建一个用户存储游戏统计信息的实例,并创建积分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #开始游戏的主循环
    while True:
    
        #监视键盘和鼠标
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        #print(stats.game_active)
        print(stats)
        print(pygame.event)
        if stats.game_active:
            ship.update(ai_settings)
        
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #print(len(bullets))
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)
                       

run_game()