a= int(input())
b= int(input())
## 1 - Faça uma função de multiplicação de
##     dois números inteiros usando apenas soma
def mult(a,b):
    c=[]
    i=0
    while i<b:
        c.append(a)
        i=i+1

    print(sum(c))

## 2 - Faça uma função de exponenciação de
##     dois números inteiros usando a função acima.
def exponen():
    mult(a,b)  

## 3 - Faça uma função de divisão inteira de
##     dois números inteiros usando só subtração.
def DivisaoInt(a,b):
    x=a
    i=0
    while x>=b:
        x=x-b
        i=i+1
    print(i)
## 4 - Faça uma função de resto de uma divisão inteira de
##     dois números inteiros usando só subtração.
def restoInt(a,b):
    x = a
    while x >=b:
        x = x - b
    print(x)

## 5 - Um botânico dedicou-se, durante anos de estudos, a conseguir
##     criar uma função exponencial que medisse o crescimento dos
##     pinheiros no decorrer do tempo. Sua conclusão foi que, ao
##     plantar-se essa árvore, seu crescimento em centímetros, no
##     decorrer dos anos, é dado por C(t) = 5 x 2^(t – 1).  Faça um
##     programa que leia t (número de anos) e mostre qual o tamanho
##     esperado de um pinheiro em centímetros.  Use apenas as funções
##     criadas anteriormente.
def Botanico():
    t=int(input("Anos: "))
    a=5
    b=2**(t-1)
    mult(a,b)
## 6 - Faça um programa que leia um número de segundos e mostre o
##     equivalente em horas, minutos e segundos. Ex.: 7321 ->
##     02h02m01s. Use apenas as funções anteriormente.
def hora():
    s=int(input())
    a=s
    b=3600
    print("horas:")
    DivisaoInt(a,b)
    print("minutos:")
    s%=3600
    a=s
    b=60
    DivisaoInt(a,b)
    print("segundos:")
    a=s
    b=60
    restoInt(a,b)
    print
hora()