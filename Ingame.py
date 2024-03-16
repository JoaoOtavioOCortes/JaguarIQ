import openpyxl   
import random
import time
import keyboard  
import pygame

#seleciona uma pergunta aleatória
def randomize():
    line = random.randint(1,260)
    qstn = str(line)
    return qstn

#renderiza a pergunta
def renderL1(cont, posy = 50): 
    global fontela 
    fontela = fonte.render(linha1, 1, (0,0,0))
    window.blit(fontela,(50,posy))

#funcionamento do jogo
def gametela():
    #variaveis globais
    global window, fonte, linha1
    loopplvr = True
    ingame = True

    pygame.init()
    pygame.font.init()

    #carregando planilha de perguntas
    planilha = openpyxl.load_workbook('perguntas/planilha.xlsx')
    sheet = planilha.active  

    #abrindo tela do jogo
    window = pygame.display.set_mode((1280,720))
    color =  (255,255,255) 
    pygame.display.set_caption('JaguarIQ')
    pygame.surface.Surface((1280,720))
    fonte = pygame.font.SysFont('Daydream', 32)

    while ingame:
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
            timer = 5


            #inicia o jogo
            if keyboard.is_pressed('Enter') == True:
                for letra in pergunta:
                    if keyboard.is_pressed('Space') == True:
                        loopplbr = False
                        break         
                    #printando a pergunta   
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
                #Funcionamento do timer
                while wait:
                    for x in range(timer, -1, -1):
                        timertxt = f'timer: {timer}'
                        rendertimer = fonte.render(timertxt, False, (0,0,0))
                        window.blit(rendertimer,(800,50))
                        
                        #timer esgotado
                        if x <= 0:
                            fontela = fonte.render('tempo esgotado!', 1, (255,0,0))
                            resp = fonte.render(f'Resposta: {resposta}', 1, (255,0,0))
                            window.blit(resp,(275,600))
                            window.blit(fontela,(275,500))   

                        pygame.display.update()
                        time.sleep(1)
                        rendertimer = fonte.render(timertxt, False, (255,255,255))
                        window.blit(rendertimer,(800,50))
                        timer -= 1

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
                ingame = False
        pygame.display.update()