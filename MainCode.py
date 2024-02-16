import openpyxl   
import random
import time
import keyboard  
import pygame

 
#função para randomizar as perguntas
def randomize():
    line = random.randint(1,260)
    qstn = str(line)
    return qstn

#variaveis globais
loop = True
corw = True
cont = randomize()
loopplvr = True
verf = 0
running = True

#gerando a pergunta
while loop:
    planilha = openpyxl.load_workbook('perguntas/planilha.xlsx')
    sheet = planilha.active  
    pergunta = sheet['A'+cont].value
    resposta = sheet['B'+cont].value 
    
    #print da pergunta letra por letra
    while loopplvr:      
        palavra = ''
        for letra in pergunta:

            if keyboard.is_pressed('Space') == True:
                verf = 1
                loopplvr = False         
                break
                
            else:
                print(palavra)
            
            palavra += letra     
            time.sleep(0.3)

        if verf == 0:
            print('Tempo esgotado!')
            loopplvr = False

        else:
            loopplvr = False
        
    print(f'A resposta é: {resposta}')
    loop = False
           


