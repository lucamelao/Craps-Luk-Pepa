#importando as bibliotecas necessárias
import random
#definindo as variáveis que serão utilizadas
DADO1 = random.randint(1,6)
DADO2 = random.randint(1,6)
SOMA1 = DADO1 + DADO2 = POINT
SOMA2 = random.randint(1,6) + random.randint(1,6)
fichas = 100
PLB = Pass_Line_Bet
F = Field
AC = Any_Craps
T = Twelve


#SEMPRE PRINTAR QUAL FASE E QUAIS APOSTAS PODE FAZER

#início do jogo
#fase "Come out"
print('Você está na fase: Come out')
APOSTA = input('Qual a opção de aposta escolhida? (PLB/F/AC/T)')
while APOSTA == 'PLB' and fichas > 0:
    VALOR_APOSTA = int(input('Qual o valor da aposta: '))
    if SOMA1 == 7 or 11:
        print('Parabéns, você ganhou!')
        fichas = fichas + VALOR_APOSTA
    elif SOMA1 == 2 or 3 or 12:
        print('Que pena, você perdeu!')
        fichas = fichas - VALOR_APOSTA
    else:
        print('Agora vamos mudar de fase')
        print('Você está na fase: Point')    
        while SOMA2 != POINT or SOMA2 != 7:
            SOMA2 = random.randint(1,6) + random.randint(1,6)
        if SOMA2 == POINT:
            print('Parabéns, você ganhou!')
            fichas = fichas + VALOR_APOSTA
        elif SOMA2 == 7:
            print('Que pena, você perdeu!')
        fichas = fichas - VALOR_APOSTA        
else:  
    APOSTA == 'F' or 'AC' or 'T'
    if APOSTA == 'F' and fichas > 0: 
        print('Você está na fase: Come out')
        if SOMA1 == 5 or 6 or 7 or 8:
            print('Que pena, você perdeu!')
            fichas == fichas - VALOR_APOSTA
        elif SOMA1 == 2 or 3 or 4 or 9 or 10 or 11 or 12:
            print('Parabéns, você ganhou!')
            if SOMA1 == 2:
                fichas == fichas + (VALOR_APOSTA)*2
            elif SOMA1 == 12:
                fichas == fichas + (VALOR_APOSTA)*3
            else:
                fichas == fichas + VALOR_APOSTA
    if APOSTA == 'AC' and fichas > 0:
        print('Você está na fase: Come out')
    if SOMA1 == 2 or 3 or 12:
        print('Parabéns, você ganhou!')
        fichas == fichas + (VALOR_APOSTA)*7
    else:
        print('Que pena, você perdeu!')
        fichas == fichas - VALOR_APOSTA
        
        if APOSTA == 'T' and fichas > 0: 


