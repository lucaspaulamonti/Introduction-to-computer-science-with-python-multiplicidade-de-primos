# Dado um número n, n>1, imprimir sua decomposição em fatores primos, indicando também a multiplicidade de cada fator. Ex. 8=2*2*2.
n=int(input('Digite um número inteiro maior que 1: '))
fator=2
multiplicidade=0
while(n>1):
    while(n%fator==0):
        multiplicidade=multiplicidade+1
        n=n/fator
    if(multiplicidade>0):
        print('Fator:',fator,",multiplicidade:",multiplicidade)
    fator=fator+1
    multiplicidade=0
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!