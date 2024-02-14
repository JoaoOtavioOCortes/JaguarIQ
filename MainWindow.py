import pygame
import Buttons

pygame.init()


running = True

#Create display window
window = pygame.display.set_mode((1080,920))
collor =  (255,255,255) #white
pygame.display.set_caption('JaguarIQ')
pygame.surface.Surface((1200,700))

#load button images
start_img = pygame.image.load('images/buttons/Start.png').convert_alpha()
quit_img = pygame.image.load('images/buttons/Quit.png').convert_alpha()
options_img = pygame.image.load('images/buttons/Options.png').convert_alpha()

#create button instancesS
start_button = Buttons.Button(377, 400, start_img)
quit_button = Buttons.Button(377, 700, quit_img)
options_button = Buttons.Button(377, 550, options_img)


#game loop
while running:
    
    window.fill(collor)

    start_button.draw(window)
    options_button.draw(window)
    quit_button.draw(window)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()