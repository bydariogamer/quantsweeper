#code for python3 licensed under GNU GPL 3.0+, made by bydariogamer

#import module and make it run
import pygame
pygame.init()

#set mesures, clock and images
disp_wid=600
disp_hei=800
miner=pygame.image.load('res/miner.png') #image under CC-BY-SA
ender=pygame.image.load('res/ender.png') #image under CC-BY-SA
clock = pygame.time.Clock()

#set window mesures and title
game = pygame.display.set_mode((disp_wid,disp_hei))
pygame.display.set_caption('QUANTSWEEPER')

#improvement code
'''
#define classes
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True    
        return False
'''

#the game works until you want to exit
run=True
switch=True

while run:
    game.fill((255,255,255))
    if switch:
        game.blit(miner,(0,0))
    else:
        game.blit(ender,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            switch=not switch
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
    clock.tick(60)
    
#if the game finish, we just close everything:
pygame.quit()
print('bye')
quit()
