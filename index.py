import random
import os

listaBot = ['PAPEL', 'TESOURA', 'PEDRA']

#contador
contagem = 0
contagemBot = 0
print('Bem vindo ao jogo Pedra, Papel e Tesoura!')
def placar():
    print('-------------------------------------------')
    print('Placar:\nBot:{}\nVocê: {}'.format(contagemBot, contagem))
    print('-------------------------------------------')
    

def bot():
    escolhaBot = random.choice(listaBot)
    print(f'O bot escolheu:{escolhaBot}')
    escolha = input('Escolha o seu lance:\n 1 - Papel | 2 - Pedra | 3 - Tesoura\n')

    #derrotas
    if escolha == '1' and escolhaBot == 'TESOURA':
        global contagemBot
        contagemBot += 1
        print('Você Perdeu')
        return
    
    if escolha == '2' and escolhaBot == 'PAPEL':
        print('Você Perdeu')
        contagemBot += 1
        return        
    
    if escolha == '3' and escolhaBot == 'PEDRA':
        print('Você Perdeu')
        contagemBot += 1
        return
    #vitórias
    if escolha == '1' and escolhaBot == 'PEDRA':
        print('Você Ganhou')
        global contagem
        contagem += 1
        return
    
    if escolha == '2' and escolhaBot == 'TESOURA':
        print('Você Ganhou')
        contagem += 1
        return    
    
    if escolha == '3' and escolhaBot == 'PAPEL':
        print('Você Ganhou')
        contagem += 1
        return

    #empate
    else:
        print('Empate!')

execucao = True

while execucao:
    placar()
    bot()
    reset = str(input('Deseja jogar novamente?:\n[S/N]\n')).upper().strip()
    if reset == 'N':
        execucao = False
        exit('Obrigado por jogar!')
    else:
         os.system('cls')


