import pygame
display_width=480
display_height=480
gameDisplay=pygame.display.set_mode((display_width,display_height))
alienImg=pygame.image.load('alien1.jpg')
alien1Img=pygame.image.load('alien.png')
def alienHit(x,y):
    gameDisplay.blit(alien1Img,(x,y))
def alien(x,y):
    gameDisplay.blit(alienImg,(x,y))
class aliens:
  def __init__(self,myClock,x,y,hit=0):
    self.hit=hit
    self.clock=myClock
    self.x=x
    self.y=y
