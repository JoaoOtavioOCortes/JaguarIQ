import pygame

class Button():
    #Cria o botão com suas caracteristicas
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    #Desenha o botão na tela e o torna clicavel
    def draw(self, x):
        action = False
        #pega a posição do mouse
        mousepos = pygame.mouse.get_pos()

        #checa a posição e o clique do mouse
        if self.rect.collidepoint(mousepos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Desenha o botão na tela
        x.blit(self.image,(self.rect.x, self.rect.y))
    
        return action