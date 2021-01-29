def mmc(a,b):
    mc = (a*b)/ mdc(a,b) // Fórmula que calcula o mmc a partir do mdc 
    return mc


def mdc(a,b): // Algoritmo que calcula o mdc
    r = a % b
    while(r != 0):
        a = b
        b = r
        r = a % b
    return b


def mmc_n(): // Função que calcula o mmc de uma lista de número
    for i in range(1,len(lista)):
        lista[i] = mmc(lista[i-1],lista[i])
    return lista[i]




lista = [567,34,565,98]

print("O mmc = {}".format(mmc_n()))
