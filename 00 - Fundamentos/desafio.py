usuarios = []
contas = []

def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [c] Cadastrar Conta
    [u] Cadastrar Usuario
    
    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_conta = 1

    while True:

        opcao = input(menu)

        # ---------------------- DEPÓSITO ----------------------
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        # ---------------------- SAQUE ----------------------
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        # ---------------------- EXTRATO ----------------------
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        # ---------------------- SAIR ----------------------
        elif opcao == "q":
            print("Sistema encerrado.")
            break

        elif opcao == "c":
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "u":
            cadastrar_usuario(usuarios)

        # ---------------------- OPÇÃO INVÁLIDA ----------------------
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    # Verifica se usuário já existe
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
        })
    print("Usuário cadastrado com sucesso.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso.")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("Usuário não encontrado. Fluxo de criação de conta encerrado.")


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


if __name__ == "__main__":
    main()