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
loopplvr = True
verf = 0
running = True

pygame.init()
pygame.font.init()

planilha = openpyxl.load_workbook('perguntas/planilha.xlsx')
sheet = planilha.active  

window = pygame.display.set_mode((1200,700))
color =  (255,255,255) 
pygame.display.set_caption('JaguarIQ')
pygame.surface.Surface((1200,700))
fonte = pygame.font.SysFont('Daydream', 32)

while running:
    window.fill(color)

    while loopplvr:
        posy = 50
        geraplvr = randomize()
        pergunta = sheet['A'+geraplvr].value
        resposta = sheet['B'+geraplvr].value 
        window.fill(color)
        pygame.display.update() 
        linha1 = ''
        linha2 = ''
        cont = 0

        #inicia o jogo
        if keyboard.is_pressed('Enter') == True:
            for letra in pergunta:
                if keyboard.is_pressed('Space') == True:
                    verf = 1
                    loopplbr = False
                    break         
                    
                else:
                    cont += 1
                    renderL1(cont, posy)
                    linha1 += letra
                    if cont%38 == 0:
                        linha1 = ''
                        linha1 += letra
                        posy += 50
                    elif cont > 38:
                        renderL1(cont, posy)
                    else: 
                        pass
                pygame.display.update()    
                time.sleep(0.1)
            wait = True
            while wait:
                fontela = fonte.render('tempo esgotado!', 1, (0,0,0))
                window.blit(fontela,(200,300))   
                pygame.display.update()
                if keyboard.is_pressed('Esc'):
                    wait = False
                elif keyboard.is_pressed('Enter'):
                    break
                else:
                    pass


        else:
            pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()