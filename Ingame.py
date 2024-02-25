import openpyxl   
import random
import time
import keyboard  
import pygame

def randomize():
    line = random.randint(1,260)
    qstn = str(line)
    return qstn

loop = True
corw = True
cont = randomize()
loopplvr = True
verf = 0
running = True



pygame.init()
pygame.font.init()

planilha = openpyxl.load_workbook('perguntas/planilha.xlsx')
sheet = planilha.active  
pergunta = sheet['A'+cont].value
resposta = sheet['B'+cont].value 

window = pygame.display.set_mode((1200,700))
collor =  (255,255,255) 
pygame.display.set_caption('JaguarIQ')
pygame.surface.Surface((1200,700))
fonte = pygame.font.SysFont('Daydream', 32)

while running:
    window.fill(collor)
    while loopplvr: 
        palavra = ''
        posx = 50
        posy = 50
        posXrect = 50
        posYrect = 50
        rect = pygame.Rect(posXrect,posYrect,20,20)

        for letra in pergunta:
            
            fontela = fonte.render(palavra, 1, (0,0,0))
            window.blit(fontela,(posx,posy))
            

            if keyboard.is_pressed('Space') == True:
                verf = 1
                loopplvr = False         
                break
                
            else:
                print(palavra)
                palavra += letra
                rect.x += 12
            pygame.display.update()    
            time.sleep(0.3)

        if verf == 0:
            timeOut = fonte.render('Tempo Esgotado!', 1, (0,0,0))
            loopplvr = False
            if keyboard.is_pressed('Enter') == True:
                loopplvr = False
    
    window.blit(fontela,(posx,posy))
    window.blit(timeOut,(515,100))
    pygame.draw.rect(window, (255,0,0), rect)
    loopplvr = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()