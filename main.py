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
            palavra += letra     
            time.sleep(0.5)

            if letra == ' ':
                pass
            else:
                print(palavra)

            if letra == len(pergunta.value):
                print('Tempo esgotado.')
                loopplvr = False
            elif keyboard.is_pressed('Space') == True:
                loopplvr = False          
                break  
        
        loop = False

           
#resposta
print(f'A resposta é: {sheet['B'+cont].value}',)

#comando de certo ou errado
print('Se sua resposta está certa aperte = "C"\nSe sua resposta está errada aperte = "E"')
if keyboard.is_pressed('C'):
    False
    print('Você acertou! :)')
    
elif keyboard.is_pressed('E'):
    False
    print('Você errou ;(')

else:
    pass
