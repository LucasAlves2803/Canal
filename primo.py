# Algoritmo para verificar se um número é primo


print("Digite um número a ser verificado:")
p = int(input())
cont = 0
for i in range(1,p+1):
    if p % i == 0:
        cont = cont + 1
if cont == 2:
    print ("{:d} é primo".format(p))
else:
    print ("{:d} não é primo".format(p))
