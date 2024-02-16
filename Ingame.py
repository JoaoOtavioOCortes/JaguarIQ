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

window = pygame.display.set_mode()
collor =  (255,255,255) 
pygame.display.set_caption('JaguarIQ')
pygame.surface.Surface((1200,700))
fonte = pygame.font.SysFont('Daydream', 32)

while running:
    window.fill(collor)
    while loopplvr: 
        palavra = ''

        for letra in pergunta:
            posx = 50
            posy = 50
            fontela = fonte.render(palavra, 1, (0,0,0))
            window.blit(fontela,(posx,posy))
            pygame.display.update()  

            if keyboard.is_pressed('Space') == True:
                verf = 1
                loopplvr = False         
                break
                
            else:
                print(palavra)
            
            palavra += letra     
            time.sleep(0.3)

        if verf == 0:
            fontela = fonte.render('Tempo Esgotado!', 1, (0,0,0))
            window.blit(fontela,(515,100))
            pygame.display.update()  
            if keyboard.is_pressed('Enter') == True:
                loopplvr = False

        else:
            loopplvr = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()