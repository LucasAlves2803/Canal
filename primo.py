# Algoritmo para verificar se um n�mero � primo


print("Digite um n�mero a ser verificado:")
p = int(input())
cont = 0
for i in range(1,p+1):
    if p % i == 0:
        cont = cont + 1
if cont == 2:
    print ("{:d} � primo".format(p))
else:
    print ("{:d} n�o � primo".format(p))
