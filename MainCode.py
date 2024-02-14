import openpyxl   
import random
import time
import keyboard      
   
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

#gerando a pergunta
while loop:
    planilha = openpyxl.load_workbook('perguntas/planilha.xlsx')
    sheet = planilha.active  
    pergunta = sheet['A'+cont]       
    
    #print da pergunta letra por letra
    while loopplvr:      
        palavra = ''
        for letra in pergunta.value:
            if letra == ' ':
                pass

            elif keyboard.is_pressed('Space') == True:
                loopplvr = False         
                break

            elif len(palavra)==len(pergunta.value):
                print('Tempo esgotado!')
                loopplvr = False

            else:
                print(palavra)
            palavra += letra     
            time.sleep(0.5)

    print(f'A resposta é: {sheet['B'+cont].value}',)
    loop = False
           


