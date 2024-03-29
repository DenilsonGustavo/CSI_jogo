# main.py
import pygame
from settings import Settings
from entities.player import Player
from entities.enemy import Enemy

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height)
    )
    player = Player(screen)
    enemy = Enemy(screen)

    while True:
        # Game loop code here

if __name__ == '__main__':
    run_game()
