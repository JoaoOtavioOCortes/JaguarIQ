import pygame
import Buttons
from Ingame import *
from options import *


pygame.init()


running = True
menu = True

#Criação da tela
res = (1280,720)
window = pygame.display.set_mode(res)
color =  (255,255,255) 
pygame.display.set_caption('JaguarIQ')
pygame.surface.Surface(res)
fonte = pygame.font.SysFont('Daydream', 32)

#Carregamento da imagem do botão
start_img = pygame.image.load('images/buttons/Start.png').convert_alpha()
quit_img = pygame.image.load('images/buttons/Quit.png').convert_alpha()
options_img = pygame.image.load('images/buttons/Options.png').convert_alpha()

#Instanciando o botão
start_button = Buttons.Button(515, 350, start_img, 0.8)
quit_button = Buttons.Button(515, 600, quit_img, 0.8)
options_button = Buttons.Button(515, 475, options_img, 0.8)


#game loop
while running:
    
    window.fill(color)
    if menu: 
        if start_button.draw(window):
            gametela()
            running = False  
        if options_button.draw(window):
            res = optionstela()
        if quit_button.draw(window):
            running = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()