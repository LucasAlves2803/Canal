# Algoritmo de Euclides

def mdc_ite(a,b):
    r = a % b
    while (r != 0):
        a = b
        b = r
        r = a % b
    return b





print("Digite o valor de a:")
a = int(input())
print("Digite o valor de b:")
b = int(input())
print("o mdc({:d},{:d}) = {:d}".format(a,b,mdc_ite(a,b)))
