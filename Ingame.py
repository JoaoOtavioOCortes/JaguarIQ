import openpyxl   
import random
import time
import keyboard  
import pygame

def randomize():
    line = random.randint(1,260)
    qstn = str(line)
    return qstn

def renderL1(cont, posy = 50): 
    global fontela 
    fontela = fonte.render(linha1, 1, (0,0,0))
    window.blit(fontela,(50,posy))


loop = True
corw = True
cont = randomize()
loopplvr = True
verf = 0
running = True
posy = 50

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
        linha1 = ''
        linha2 = ''
        cont = 0

        for letra in pergunta:
            if keyboard.is_pressed('Space') == True:
                verf = 1
                loopplvr = False         
                break
                
            else:
                cont += 1
                renderL1(cont, posy)
                linha1 += letra
                if cont%32 == 0:
                    linha1 = ''
                    linha1 += letra
                    posy += 50
                elif cont > 32:
                    renderL1(cont, posy)
                else: 
                    pass
            pygame.display.update()    
            time.sleep(0.3)

        if verf == 0:
            timeOut = fonte.render('Tempo Esgotado!', 1, (0,0,0))
            loopplvr = False
            if keyboard.is_pressed('Enter') == True:
                loopplvr = False

    loopplvr = False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()