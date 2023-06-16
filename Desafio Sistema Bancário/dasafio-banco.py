menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[C] Cadastrar Cliente
[I] Cadastrar Conta
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

clients = {
    "02132366055": { 
        "name": "Henrique Malikovski", 
        "date_of_birth": "27/01/1995",
        "address": {
            "road": "Barão do Trinfo", 
            "number": 2150, 
            "complement": "Apto 37", 
            "district": "Cruzeiro",
            "city": "Venâncio Aires",
            "state": "RS",
            "cep": 95800000
        },
    },
    "02132366000": { 
        "name": "Henrique Malikovski", 
        "date_of_birth": "27/01/1995",
        "address": {
            "road": "Barão do Trinfo", 
            "number": 2150, 
            "complement": "Apto 37", 
            "district": "Cruzeiro",
            "city": "Venâncio Aires",
            "state": "RS",
            "cep": 95800000
        },
    },
}

contas = {
    "0001": {
        1:{
            "cliente": "02132366055",
            "saldo": 1000,
            "extrato": ""
        },
    },
}

def validateCPF(pCPF):
    global clients
    for chave in clients:
        if chave == pCPF:
            return False
    
    return True

def add_new_client(pCPF, pName, pDate_of_birth, pAddress):
    global clients
    clients[pCPF] = dict(name=pName, date_of_birth = pDate_of_birth, address = pAddress)

def adicionaContaCorrente(pCPF, pSaldo):
    global contas
    conta = dict(cliente=pCPF, saldo=pSaldo, extrato="")
    


def addMensagem(valor, operacao):
    return "{} no valor de R$ {:.2f}".format(
        operacao.upper(), valor) + "\n"


while True:
    opcao = str(input(menu)).upper()
    if opcao == "Q":
        break

    if opcao == "C":
        cpf = str(input("Digite o CPF: (apenas números)"))
        if not validateCPF(cpf):
            raise Exception("Cliente já cadastrado no sistema! Por favor verifique!")    

        nome = str(input("Digite o nome completo do cliente: "))    
        date_of_birth = str(input("Digite a data de nascimento: "))

        address = {}
        address["road"] = str(input("Digite a Rua do Endereço: "))
        address["number"] = str(input("Digite Número do Endereço: "))
        address["complement"] = str(input("Digite o Complemento do Endereço: "))
        address["district"] = str(input("Digite o Bairro do Endereço: "))
        address["city"] = str(input("Digite a Cidade do Endereço: "))
        address["state"] = str(input("Digite o Estado do Endereço: "))
        address["cep"] = str(input("Digite o CEP do Endereço: "))
        add_new_client(cpf, nome, date_of_birth, address)
    elif opcao == "D":
        deposito = int(input("Digite o valor que deseja depositar: "))
        while deposito <= 0:
            deposito = int(
                input("\nERRO! \n O valor de deposito deve ser maior que 0(zero): "))

        saldo += deposito
        extrato += addMensagem(deposito, "Deposito")
        extrato += addMensagem(saldo, "##Saldo##")
        print(
            f"\n###DEPOSITO###\nSeu deposito de R$ {deposito:.2f} foi realizado com sucesso!")
    elif opcao == "S":
        if LIMITE_SAQUES == numero_saques:
            print(
                f"\nERRO! Você atingiu o limite de {LIMITE_SAQUES} saques diários.\nTente novamente amanhã.")
            continue

        saque = int(input("Digite o valor que deseja sacar: "))
        while saque <= 0:
            saque = int(
                input("\nERRO! \n O valor de saque deve ser maior que 0(zero): "))

        if saque > limite:
            print(
                f"\nERRO! Você não pode sacar mais do que R$ {limite:.2f} em um único saque.\nPor favor tente novamente.")
            continue

        if saque > saldo:
            print(
                f"\nERRO! Você não pode sacar mais do que possui em saldo.\nPor favor tente novamente.")
            continue

        saldo -= saque
        numero_saques += 1
        extrato += addMensagem(saque, "Saque")
        extrato += addMensagem(saldo, "##Saldo##")
        print(
            f"\n###SAQUE###\nSeu saque de R$ {saque:.2f} foi realizado com sucesso!")
    elif opcao == "E":
        print("\n"+extrato)
    else:
        print("ERRO! Opção não encontrada no sistema. Por favor tente novamente")
