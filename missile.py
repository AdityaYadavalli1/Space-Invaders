import pygame
display_width=480
display_height=480
gameDisplay=pygame.display.set_mode((display_width,display_height))
redmissImg=pygame.image.load('triangle.png')
gmissImg=pygame.image.load('gtriangle.png')
class miss:
	def __init__(self,x,y):
		self.x=x
		self.y=y
class redmiss(miss):
	def __init__(self,x,y):
		miss.__init__(self,x,y)
class gmiss(miss):
    def __init__(self,x,y):
    	miss.__init__(self,x,y)

def missile1(x,y):#just for display
    gameDisplay.blit(redmissImg,(x,y))
def missile2(x,y):
    gameDisplay.blit(gmissImg,(x,y))
