print("1 - Cadastrar Empresa")
print("2 - Cadastrar Usuário")
print("3 - Registrar Compra de um Usuário")
print("4 - Mostrar Saldo de um Usuário")
print("5 - Resgatar Saldo de um Usuário")
print("6 - Excluir Empresa")
print("0 - Sair")

empresas={"ALB": "10","MM": "8","CZB": "5"}
usuario={}
i="sim"

while i == "sim":
    Resp=int(input("Qual serviço desejas realizar?"))
    if Resp==1:
        id=str(input("Id da empresa:"))
        porc=int(input("Qual a porcentagem de cashback oferecida:"))
        empresas[id]=porc
    elif Resp==2:
        idpes=str(input("Id do usuario:"))
        saldo=0
        usuario[idpes]=saldo
    elif Resp==3:
        id3=str(input("Id do usuario:"))
        if id3 in usuario:
            valor_compra=int(input("Valor da compra:"))
            idemp=str(input("Id da empresa:"))
            p=(usuario[id3])
            u=empresas[idemp]
            u=int(u)
            novo=(valor_compra*u)/100
            novo=p+novo
            usuario[id3]=novo   
        else:
            print("Usuario desconhecido")  
    elif Resp==4:
        idsaldo=str(input("Id do usuario:"))
        if idsaldo in usuario:
            print(usuario[idsaldo])
        else:
            print("Usuario desconhecido")
    elif Resp==5:
         nomesla=str(input("Id do usuario:"))
         if nomesla in usuario:
            print(usuario[nomesla])  
            n=(usuario[nomesla])
            tirar=float(input("Qual valor deseja retirar?"))
            m=n-tirar
            usuario[nomesla]=m
         else:
             print("Usuario desconhecido")
    elif Resp==6:
        remover_emp=str(input("Qual empresa desejas remover?"))
        if remover_emp in empresas:
            sim_nao=str(input("Desejas mesmo excluira empresa?"))
            if sim_nao=="sim":
                empresas.pop(remover_emp)
            else:
                print("Certo, empresa não excluida.")
        else:
            print("Empresa não cadastrada")
    elif Resp==0:
        print("Volte sempre")
        break

    i=str(input("Desejas mais alguma coisa? sim/não"))

