from time import sleep
print('\033[31m'+'-='*33 +'\033[0;0m')
print('\033[36m'+'BEM VINDOS À FINAL DO CAMPEONATO MUNDIAL DE JOKENPÔ!'+'\033[0;0m')
sleep(2)
print('\033[36m'+'TEMOS AQUI AS ILUSTRES PRESENÇAS DE NOSSOS FINALISTAS: '+'\033[0;0m')
nome1=input('')
print('\033[36m'+'E DO OUTRO LADO DO OCTÓGONO: '+'\033[0;0m')
nome2=input('')
print('\033[31m'+'-='*33 +'\033[0;0m')
print('\033[36m'+'FINAL ENTRE, ',nome1,'e',nome2,' MUITO AGUARDADA, SERÁ REALIZADA AGORA! '+'\033[0;0m')
sleep(2)
print('\033[36m'+'PORTANTO, SEM MAIS DELONGAS; VAMOS AO JOGO! '+'\033[0;0m')
print('\033[31m'+'-='*33 +'\033[0;0m')
#### escolhas
import getpass
escolha1=getpass.getpass('\033[36m'+'FAÇA SUA ESCOLHA! '+'\033[0;0m')
escolha2=getpass.getpass('\033[36m'+'FAÇA SUA ESCOLHA! '+'\033[0;0m')
print('\033[31m'+'-='*33 +'\033[0;0m')
print('\033[36m'+'JO '+'\033[0;0m')
sleep(1)
print('\033[36m'+'KEN '+'\033[0;0m')
sleep(1)
print('\033[36m'+'PÔ!!! '+'\033[0;0m')
print('\033[31m'+'-='*33 +'\033[0;0m')
#### escolhas 1 com papel
if escolha1=='papel' and escolha2=='papel':
    print('\033[36m' + 'TEMOS UM EMPATE SENHORAS E SENHORES! ' + '\033[0;0m')
if escolha1=='papel' and escolha2=='tesoura':
    print('\033[36m' + 'TESOURA GANHA DE PAPEL!',nome2,'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ' + '\033[0;0m')
if escolha1=='papel' and escolha2=='pedra':
    print('\033[36m' + 'PAPEL GANHA DE PEDRA!',nome1,'É O NOSSO NOVO CAMPEÃO MUNDIAL DE JOKENPÔ! ' + '\033[0;0m')
#### ESCOLHAS 1  COM PEDRA
if escolha1=='pedra' and escolha2=='pedra':
    print('\033[36m' + 'TEMOS UM EMPATE SENHORAS E SENHORES! ' + '\033[0;0m')
if escolha1=='pedra' and escolha2=='papel':
    print('\033[36m' + 'PAPEL GANHA DE PEDRA!',nome2, 'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ' + '\033[0;0m')
if escolha1=='pedra' and escolha2=='tesoura':
    print('\033[36m' + 'PEDRA GANHA DE TESOURA!',nome1,'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ' + '\033[0;0m')
#### escolhas 1 com tesoura
if escolha1=='tesoura' and escolha2=='tesoura':
    print('\033[36m' + 'TEMOS UM EMPATE SENHORAS E SENHORES! ' + '\033[0;0m')
if escolha1=='tesoura' and escolha2=='papel':
    print('\033[36m' + 'TESOURA GANHA DE PAPEL',nome1,'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ' + '\033[0;0m')
if escolha1=='tesoura' and escolha2=='pedra':
    print('\033[36m' + 'PEDRA GANHA DE TESOURA!',nome2, 'É O NOSSO CAMPEÃO MUNDIAL DE JOKENPÔ! ' + '\033[0;0m')