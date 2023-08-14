
def saque(saldo,valor,estrato): #Keyword exemplo: saldo = saldo           
    if valor > saldo:
        print("Valor para saque insuficiente!")
        estrato = ''
        saldo = 0.0
        return saldo, estrato
        
    elif valor > 500.0:
        print("O limite monetário para saque é de R$ 500,00") 
        estrato = ''
        saldo = 0.0
        return saldo, estrato
    else:
        
        print("Saque efetuado com Sucesso")
        estrato = f'\nsaque de {valor:.2f}'
        saldo -= valor
          
        return saldo,estrato #Vai retornar o saldo e o extrato

def deposito(saldo,estrato): #Position only
    print("--------------------------------------------------------------------------------------")
    valor = float(input("Valor para depósito: "))
    if valor < 0:
        print("O depósito não pode ser negativo!!")
        saldo = 0.0
        estrato = ''
        return [saldo,estrato]
    else:
        print(f"depósito de R${valor:.2f} efetuado")
        saldo += valor
        estrato = f'\ndepósito de R${valor:.2f}'
        
        return [saldo,estrato]
    
     #Retornar saldo e extrato

def extrato(saldo,/,**kwargs):  #Position only e Keyword Only
    print("--------------------------------------------------------------------------------------")
    print(f"Saldo de R${saldo:.2f}" + Estrato )

def cadastrar_usuario(matriz_usuario):
    cpf = int(input("Digite o seu CPF:"))
    usuario = filtrar_usuario(cpf,matriz_usuario)
    if usuario:
        print("Esse nome ja possui uma conta cadatrada")
        return
    
    nome = str(input("Digite o seu nome: "))
    dt_nascimento = str(input("Digite sua data de Nascimento: "))
    
    
    logradouro = input("Qual o seu endereço? ")
    numero = str(input("Seu número: "))
    bairro = str(input("Bairro:  "))
    cidade = str(input("Cidade"))
    estado = str(input("Estado: "))
    endereco = f'{logradouro} - {numero} - {bairro} - {cidade} - {estado}'
    
    matriz_usuario.append({'Nome':nome,'Data de Nascimento':dt_nascimento,'cpf':cpf,'Endereço':endereco})
    print("Usuário criado com sucesso!!!!!!!!!!")
                
    
def filtrar_usuario(cpf,matriz_usuario):
    usuarios_filtrados = [usuario for usuario in matriz_usuario if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def cadastrar_conta_bancaria(agencia,numero_conta,matriz_usuario):
    cpf = int(input("Digite o seu CPF:"))
    usuario = filtrar_usuario(cpf,matriz_usuario)
    if usuario:
        print("Conta criada com sucesso")

        return{'agencia':agencia,'numero_conta':numero_conta,'usuario':matriz_usuario}
    print("Usuário não encontrado!!")
    
   

def iniciar(menu):
    
    return input(menu)    

menu = '''
(c) - Cadastrar Usuário
(h) - Criar Conta Corrente
(d) - Depositar
(s) - Sacar
(e) - Estrato
(q) - Sair

'''

AGENCIA ='001'
matriz_usuario = []
matriz_corrente = []
Saldo = 0.0
Estrato = ''
numeros_saques = 0
limite_saques = 3

while True:
    print("--------------------------------------------------------------------------------------")
    
    opcao = iniciar(menu) 

    if opcao == 'c':
       matriz_usuario.append(cadastrar_usuario(matriz_usuario))
    elif opcao == 'h':
       matriz_corrente.append(cadastrar_conta_bancaria(AGENCIA,matriz_usuario)) 

    elif opcao == "d":
        lista = deposito(Saldo, Estrato)
        if lista[0] != 0 and lista[1] != '': 
            Saldo += lista[0]
            Estrato += lista[1]
        else:
            continue
        
        
    elif opcao == "s":
        print("--------------------------------------------------------------------------------------")
        if numeros_saques == limite_saques:
            print("Limite de saque diário excedido!!!!")
        else: 
            valor = float(input("Valor para saque: "))
            li = saque(saldo=Saldo,valor = valor,estrato= Estrato)
            if li[0] != 0.0 and Estrato != '':
                Saldo = li[0]
                Estrato += li[1]
                numeros_saques += 1
            else:
                numeros_saques += 1
                continue
    
    elif opcao == 'e':
        extrato(Saldo,estrato=Estrato)
        

    elif opcao == "q":
        print("--------------------------------------------------------------------------------------")
        print("Fim do programa!!!!!!!!!!!!!!!!")
        print("--------------------------------------------------------------------------------------")
        break
    else:
        print("Opção inválida, tente novamente:")

