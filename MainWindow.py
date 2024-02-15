import pygame
import Buttons

pygame.init()


running = True
menu = True

#Create display window
window = pygame.display.set_mode((1080,920))
collor =  (255,255,255) #white
pygame.display.set_caption('JaguarIQ')
pygame.surface.Surface((1200,700))

#load button images
start_img = pygame.image.load('images/buttons/Start.png').convert_alpha()
quit_img = pygame.image.load('images/buttons/Quit.png').convert_alpha()
options_img = pygame.image.load('images/buttons/Options.png').convert_alpha()

#create button instances
start_button = Buttons.Button(410, 400, start_img, 0.8)
quit_button = Buttons.Button(410, 700, quit_img, 0.8)
options_button = Buttons.Button(410, 550, options_img, 0.8)


#game loop
while running:
    
    window.fill(collor)
    if menu: 
        if start_button.draw(window):
            menu = False    
        if options_button.draw(window):
            menu = False
        if quit_button.draw(window):
            running = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()