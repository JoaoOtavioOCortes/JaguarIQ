import pygame
import Buttons
import keyboard

def optionstela(res):
    
    pygame.init()
    pygame.font.init()
    run = True
    while run:
        pygame.display.update()
        window = pygame.display.set_mode(res)
        color =  (255,255,255) 
        pygame.display.set_caption('JaguarIQ')
        pygame.surface.Surface(res)
        fonte = pygame.font.SysFont('Daydream', 32)
        botao = pygame.draw.rect(window, (0,0,0), (50,50), (100,100))
        window.fill(color)

        resolutions = [(1920,1080),(1366,768),(1280,720),(1200,900)]
        resatual = 0

        if botao.draw(window):
            resatual += 1
            resolutions[resatual]
            pygame.display.update()
            if resatual == 4:
                resatual = 0

        else:
            pass
        
        if keyboard.is_pressed('Esc') == True:
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ingame = False

        pygame.display.update()

        return resolutions[resatual]



