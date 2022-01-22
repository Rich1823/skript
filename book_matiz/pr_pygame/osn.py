import sys
import pygame
import igrok


def run_game():
    pygame.init()
    ig = igrok.Igrok()
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (140, 140, 160)
    pygame.display.set_caption("Zadanie")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ig.blitme()
        pygame.display.flip()


run_game()
