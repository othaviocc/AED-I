#PROJETO 2 SEM USAR IF PRA CARAMBA
print('10 - Caderno pautado R$ 10,00')
print('20 - Caneta azul R$ 3,00')
print('21 - Caneta vermelha R$ 3,00')
print('30 - Borracha R$ 2,00')
print('45 - Lápis macio R$ 1,00')
print("==============================")

print('Seja Bem-Vindo')
cliente=str(input("Digite seu nome:"))

produto=["Caderno pautado","Caneta azul","Caneta vermelha","Borracha","Lapis macio"]
codigo=[10,20,21,30,45]
valor=[10,3,3,2,1]

cod=[]
quant=[]
val=[]

c=1
while c!=0:
    c=int(input("Qual o codigo do produto escolhido?"))
    if c != 0:
        quantidade=int(input("Qual a quantidade você deseja?"))
        if c in codigo:
            cont=0
            while codigo[cont]!=c:
                cont+=1
            cod.append(produto[cont])
            quant.append(quantidade)
            val.append(valor[cont])
        print((quant[(len(quant)-1)]),"x", (cod[(len(cod)-1)]))
        resposta=str(input("Deseja mais alguma coisa? sim/não:"))
        if resposta=="não":
            c=0

#PRINT IMPORTANTE
print("==============================")
print("Cliente: ",cliente)
cont=0
preco=[]
while cont < len(cod):
    men=val[cont]*quant[cont]
    preco.append(men)
    cont+=1
cont=0
s=len(cod)
p=len(quant)
while cont<len(cod):
    print("R$",preco[cont],"-->", (quant[(len(quant)-p)]) ,"x", (cod[(len(cod)-s)]) )
    cont+=1
    s=s-1
print("==============================")
cont=0
pagar=0
while cont <len(val):
    pagar+preco[cont]
    cont+=1
print("R$",sum(preco), "valor total")
print("Obrigado pela preferência")




