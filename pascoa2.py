,from datetime import datetime, timedelta

lista_pascoa = []
pascoa_ano = []
histograma= []


def cria_datas():
    for i in range(22,32):
        lista_pascoa.append([i,3])
    for i in range(1,26):
        lista_pascoa.append([i,4])


def inicia():
    for i in range(len(lista_pascoa)):
        histograma.append([0,[]])

#ordenação por seleção
def ordenacao():
    for i in range(len(lista_pascoa)):
        aux = i
        for j in range(i+1,len(lista_pascoa)):
            if (lista_pascoa[aux][0] > lista_pascoa[j][0]):
                aux = j
            elif (lista_pascoa[aux][0] == lista_pascoa[j][0]):
               if (lista_pascoa[aux][1] > lista_pascoa[j][1]):
                    aux = j
        aux1 = lista_pascoa[aux] 
        lista_pascoa[aux]= lista_pascoa[i]
        lista_pascoa[i] = aux1


def faixa(ano):
    x = int()
    y = int()
    if ( 1599 <=  ano  <= 1699):
        x = 22
        y = 2
    elif (1700 <= ano <= 1799):
        x = 23
        y = 3
    elif (1800 <= ano <= 1899):
        x = 23
        y = 4
    elif (1900 <= ano <= 2099):
        x = 24
        y = 5
    elif(2100 <= ano <= 2199):
        x = 24
        y = 6
    elif(2200 <= ano <= 2299):
        x = 25
        y = 0
    return x,y
        
    

def algoritmo_de_Gauss(i): 
        X,Y = faixa(i)
        a = i % 19
        b = i % 4
        c = i % 7
        d = (19 * a + X) % 30
        e = (2 * b + 4 * c + 6 * d + Y) % 7
        if ((d  + e) > 9):
            dia = d + e - 9
            mes = 4
        else:
            dia = d + e + 22
            mes = 3

        if (dia == 26 and mes == 4):
            dia = 19

        if (dia == 25 and d == 28 and a > 10):
            dia = 18
        pascoa_ano.append([dia,mes,i])
        if (i > 2020):
            print "A pascoa em {:d} sera em {:d}/{:d}".format(i,dia,mes)
        else:
            print "A pascoa em {:d} foi em {:d}/{:d}".format(i,dia,mes)
def calcula_frequencia():

    for i in range(len(pascoa_ano)):
        busca_binaria(i,0,35/2,35)

def busca_binaria(i,inicio,meio,fim): # Busca binária recursiva
    if (pascoa_ano[i][0:2] > lista_pascoa[meio]):
        busca_binaria(i,meio,(meio+fim)/2,fim)
    elif (pascoa_ano[i][0:2] < lista_pascoa[meio]):
        busca_binaria(i,inicio,(meio+inicio)/2,meio)
    else:
        histograma[meio][0] = histograma[meio][0] + 1
        histograma[meio][1].append(pascoa_ano[i][2])

def calendario():
    for i in range(len(lista_pascoa)):
        print "Pascoa em {:d}/{:d} acontece nos anos de ".format(lista_pascoa[i][0],lista_pascoa[i][1])
        if histograma[i][1] == []:
            print "Não aconteceu"
        else:
            print histograma[i][1]
        print ""

def grafico():
    print "========== Frequência da Páscoa entre os anos de 1897 ate 2100 ============="
    print "  Dia",   "1 2 3 4 5 6 7 8 9 10 11  " , "Ano"
    for i in range(len(lista_pascoa)):
        print "{:3d}/{:d}".format(lista_pascoa[i][0],lista_pascoa[i][1]),
        for j in range(13):
            if (j < len(histograma[i][1])):
                print "{}".format("*"),
            else:
                print " ",
        for j in histograma[i][1]:
            print "{:}".format(j),
        print ""


#cria_datas()
#inicia()
#ordenacao()
while True:
    print "Digite o ano"
    i=int(input())
    if (i == 0):
        break
    algoritmo_de_Gauss(i)
    print""
    
#calcula_frequencia()
#calendario()
#grafico()

        

