from time import sleep
print('-='*33)
print('BEM VINDOS À FINAL DO CAMPEONATO MUNDIAL DE JOKENPÔ! ')
sleep(2)
print('TEMOS AQUI AS ILUSTRES PRESENÇAS DE NOSSOS FINALISTAS: ')
nome1=str(input(''))
print('E DO OUTRO LADO DO OCTÓGONO: ')
nome2=str(input(''))
print('-='*33)
print('FINAL ENTRE, ',nome1,'e',nome2,' MUITO AGUARDADA, SERÁ REALIZADA AGORA! ')
sleep(2)
print('PORTANTO, SEM MAIS DELONGAS; VAMOS AO JOGO! ')
print('-='*33)
#### escolhas
escolha1=str(input('faça sua escolha! '))
escolha2=str(input('faça sua escolha! '))
print('-=' * 33)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!! ')
print('-=' * 33)
#### escolhas 1 com papel
if escolha1=='papel' and escolha2=='papel':
    print('TEMOS UM EMPATE SENHORAS E SENHORES! ')
if escolha1=='papel' and escolha2=='tesoura':
    print('TESOURA GANHA DE PAPEL!',nome2,'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ')
if escolha1=='papel' and escolha2=='pedra':
    print('PAPEL GANHA DE PEDRA!',nome1,'É O NOSSO NOVO CAMPEÃO MUNDIAL DE JOKENPÔ! ')
#### ESCOLHAS 1  COM PEDRA
if escolha1=='pedra' and escolha2=='pedra':
    print('TEMOS UM EMPATE SENHORAS E SENHORES! ')
if escolha1=='pedra' and escolha2=='papel':
    print('PAPEL GANHA DE PEDRA!',nome2, 'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ')
if escolha1=='pedra' and escolha2=='tesoura':
    print('PEDRA GANHA DE TESOURA!',nome1,'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ')
#### escolhas 1 com tesoura
if escolha1=='tesoura' and escolha2=='tesoura':
    print('TEMOS UM EMPATE SENHORAS E SENHORES! ')
if escolha1=='tesoura' and escolha2=='papel':
    print('TESOURA GANHA DE PAPEL',nome1,'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ')
if escolha1=='tesoura' and escolha2=='pedra':
    print('PEDRA GANHA DE TESOURA!',nome2, 'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ')
