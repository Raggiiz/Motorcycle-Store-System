import Utilities as util

CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"


def register_client(id, clients):
    """
    Registra o nome, cidade e idade do cliente

    :param id: O id será o numero verificador do cliente
    :param clients: Dicionário que armazena os dados do cliente
    :return: Envia pro dicionário os dados inseridos
    """
    name = input("Por favor, digite o nome do cliente: ")
    city = input("Por favor, digite a cidade do cliente: ")
    age = util.get_int_value_with_range("Digite a idade do cliente", 18, 120)
    clients[id] = {
        CONST_FIELD_NAME: name,
        CONST_FIELD_CITY: city,
        CONST_FIELD_AGE: age
    }


def database_clear(clients):
    """
    Apaga o banco de dados dos clientes

    :param clients: Dicionário que armazena os dados do cliente
    :return: mensagem com sucesso ou cancelamento da operação
    """
    op = util.get_yes_no_value("Tem certeza que deseja zerar o banco de dados")
    if op == 's':
        clients.clear()
        return True, "Dados zerados com sucesso"
    else:
        return False, "Operação cancelada pelo usuário"


def client_query(clients):
    """
    Lista os dados contidos no banco

    :param clients: Dicionário que armazena os dados do cliente
    :return: retorna os dados do cliente escolhido
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        print("Nome do cliente:", clients[id][CONST_FIELD_NAME])
        print("Cidade do cliente:", clients[id][CONST_FIELD_CITY])
        print("Idade do cliente:", clients[id][CONST_FIELD_AGE])
        input("")
    else:
        print("Cliente não localizado")
        input("")


def client_del(clients):
    """
    Apaga o um clente do banco

    :param clients: Dicionário que armazena os dados do cliente
    :return: mensagem com sucesso ou cancelamento da operação
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        op = util.get_yes_no_value("Deseja mesmo excluir este cliente")
        if op == 's':
            del clients[id]
            return True, "Cliente excluído com sucesso"
        else:
            return False, "Operação cancelada pelo usuário"


def client_edit(clients):
    """
    Edita os dados de um cliente

    :param clients: Dicionário que armazena os dados do cliente
    :return: mensagem com sucesso ou fracasso da operação
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        register_client(id, clients)
        return True, "Cliente alterado com sucesso"
    else:
        op = util.get_yes_no_value("Cliente não encontrado. Deseja cadastrar?")
        if op == 's':
            register_client(id, clients)
            return True, "Cliente cadastrado com sucesso"
        else:
            return False, "Cliente não localizado."


def client_add(clients):
    """
    Adiciona um cliente

    :param clients: Dicionário que armazena os dados do cliente
    :return: mensagem com sucesso ou fracasso da operação
    """
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        op = util.get_yes_no_value("Cliente existente. Quer alterar os dados?")
        if op == 's':
            register_client(id, clients)
            return True, "Cliente alterado com sucesso"
        else:
            return False, "Cadastro não realizado. Cliente já existente"
    else:
        register_client(id, clients)
        return True, "Cliente cadastrado com sucesso"


def load_file(filename):
    """
    Carrega o arquivo do banco

    :param filename: Nome do arquivo do banco de dados
    :return: None
    """
    clients = util.file_read_bin(filename)
    return clients


def save_file(filename, clients):
    """
    Salve um arquivo do banco

    :param filename: Nome do arquivo do banco de dados
    :param clients: Dicionário que armazena os dados do cliente
    :return: None
    """
    util.file_write_bin(filename, clients)


def menu():
    """
    Menu com as opções do sistema

    :return: Retorna a opção escolhida pelo cliente
    """
    print("*** Sistema de Cadastro de Clientes ***")
    print("1. Cadastrar cliente")
    print("2. Alterar dados de cliente")
    print("3. Excluir cliente")
    print("4. Pesquisar cliente")
    print("5. Zerar banco de dados")
    print("6. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções", 1, 6)


def main(clients):
    """
    Ponto de entrada do módulo

    :return: None
    """
    filename = "dbclients"
    clients = load_file(filename)
    while True:
        op = menu()
        if op == 1:
            resp, msg = client_add(clients)
            print(msg)
            input("")

        elif op == 2:
            resp, msg = client_edit(clients)
            print(msg)
            input("")

        elif op == 3:
            resp, msg = client_del(clients)
            print(msg)
            input("")

        elif op == 4:
            client_query(clients)

        elif op == 5:
            resp, msg = database_clear(clients)
            print(msg)
            if resp:
                r = util.get_yes_no_value("Deseja criar um primeiro cliente")
                if r == 's':
                    client_add(clients)

        elif op == 6:
            save_file(filename, clients)
            break

if __name__ == '__main__':
    database = {}
    main(database)
