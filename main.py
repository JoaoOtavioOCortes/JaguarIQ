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

#gerando a pergunta
while loop:
    planilha = openpyxl.load_workbook('perguntas/planilha.xlsx')
    sheet = planilha.active  
    pergunta = sheet['A'+cont]       
    
    #print da pergunta letra por letra
    while True:      
        palavra = ''
        for letra in pergunta.value:     
            palavra += letra     
            time.sleep(0.5)
            print(palavra)
        print('Tempo esgotado.')
        break
    loop = False
           
#resposta
print(f'A resposta é: {sheet['B'+cont].value}',)

#comando de certo ou errado
print('Se sua resposta está certa aperte = "C"\nSe sua resposta está errada aperte = "E"')
while True:
    if keyboard.is_pressed('C'):
        print('Você acertou! :)')
        False
    
    elif keyboard.is_pressed('E'):
        print('Você errou ;(')
        False
    
    else:
        pass
