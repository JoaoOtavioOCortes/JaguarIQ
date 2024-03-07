import pygame
import Buttons
from Ingame import *
from options import *


pygame.init()


running = True
menu = True

#Create display window
res = (1200,900)
window = pygame.display.set_mode(res)
color =  (255,255,255) 
pygame.display.set_caption('JaguarIQ')
pygame.surface.Surface(res)
fonte = pygame.font.SysFont('Daydream', 32)

#load button images
start_img = pygame.image.load('images/buttons/Start.png').convert_alpha()
quit_img = pygame.image.load('images/buttons/Quit.png').convert_alpha()
options_img = pygame.image.load('images/buttons/Options.png').convert_alpha()

#create button instances
start_button = Buttons.Button(445, 400, start_img, 0.8)
quit_button = Buttons.Button(445, 700, quit_img, 0.8)
options_button = Buttons.Button(445, 550, options_img, 0.8)


#game loop
while running:
    
    window.fill(color)
    if menu: 
        if start_button.draw(window):
            gametela(res)  
        if options_button.draw(window):
            res = optionstela()
        if quit_button.draw(window):
            running = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()