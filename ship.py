import pygame
display_width=480
display_height=480
gameDisplay=pygame.display.set_mode((display_width,display_height))
shipImg=pygame.image.load('ship.png')
def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))
