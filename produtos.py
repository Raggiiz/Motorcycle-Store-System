"""
Sistema de vendas de motos
"""

import Utilities as util

CONST_FIELD_MODEL = "modelo"
CONST_FIELD_BRAND = "marca"
CONST_FIELD_YEAR = "ano"
CONST_FIELD_PRECO = "preco"
CONST_FIELD_DESCRICAO = "descricao"
CONST_FIELD_ESTOQUE = "estoque"


def register_moto(chassi, motos):
    """
    Registra motos no sistema

    :param chassi: Armazena o número do chassi da moto
    :param motos: Dicionário que armazena os dados da moto
    :return: Envia pro dicionário os dados inseridos
    """
    modelo = input("Modelo da moto: ")
    marca = input("Marca da moto: ")
    preco = input("Preço da moto: ")
    ano = util.get_int_value_with_range("Qual o ano da moto? ", 1990, 2021)
    descricao = input("Descrição da moto: ")
    estoque = int(input("Estoque da moto: "))
    motos[chassi] = {
        CONST_FIELD_MODEL: modelo,
        CONST_FIELD_BRAND: marca,
        CONST_FIELD_YEAR: ano,
        CONST_FIELD_PRECO: preco,
        CONST_FIELD_DESCRICAO: descricao,
        CONST_FIELD_ESTOQUE: estoque
    }


def moto_edit(motos):
    """
    Edita os dados da moto

    :param motos: Dicionário que armazena os dados da moto
    :return: Retorna menssagem com sucesso ou não localização no banco
    """
    chassi = input("Por favor, digite o chassi da moto: ")
    if chassi in motos:
        register_moto(chassi, motos)
        return True, "Moto alterada com sucesso"
    else:
        op = util.get_yes_no_value("Moto não encontrada. Deseja cadastra-la?")
        if op == 's':
            register_moto(chassi, motos)
            return True, "Moto cadastrada com sucesso"
        else:
            return False, "Moto não localizada."


def moto_add(motos):
    """
    Adiciona uma moto

    :param motos: Dicionário que armazena os dados da moto
    :return: mensagem com sucesso ou fracasso da operação
    """
    chassi = input("Por favor, digite o chassi da moto: ")
    if chassi in motos:
        op = util.get_yes_no_value("Moto já existe. Deseja alterar os dados")
        if op == 's':
            register_moto(chassi, motos)
            return True, "Moto alterada com sucesso"
        else:
            return False, "Cadastro não realizado. Moto já existente"
    else:
        register_moto(chassi, motos)
        return True, "Moto cadastrada com sucesso"


def moto_query(motos):
    """
    Lista os dados de uma moto

    :param motos: Dicionário que armazena os dados da moto
    :return: retorna os dados da moto escolhida
    """
    chassi = input("Por favor, digite o chassi da moto: ")
    if chassi in motos:
        print("Modelo da moto: ", motos[chassi][CONST_FIELD_MODEL])
        print("Marca da moto: ", motos[chassi][CONST_FIELD_BRAND])
        print("Ano da moto: ", motos[chassi][CONST_FIELD_YEAR])
        print("Preço da moto: ", motos[chassi][CONST_FIELD_PRECO])
        print("Descrição da moto: ", motos[chassi][CONST_FIELD_DESCRICAO])
        print("Estoque da moto: ", motos[chassi][CONST_FIELD_ESTOQUE])
        input("")
    else:
        print("Moto não localizada")
        input("")


def moto_list(motos):
    """
    Lista motos

    :param motos: Dicionário que armazena os dados da moto
    :return: retorna as motos
    """
    print(motos)


def moto_del(motos):
    """
    Deleta uma moto do banco

    :param motos: Dicionário que armazena os dados da moto
    :return: mensagem com sucesso ou cancelamento da operação
    """
    chassi = input("Por favor, digite o chassi da moto: ")
    if chassi in motos:
        tirar = int(input("Quantas motos deseja remover? "))
        op = util.get_yes_no_value("Tem certeza que deseja excluir essa moto")
        if op == 's':
            modelo = motos[chassi][CONST_FIELD_MODEL]
            marca = motos[chassi][CONST_FIELD_BRAND]
            preco = motos[chassi][CONST_FIELD_PRECO]
            ano = motos[chassi][CONST_FIELD_YEAR]
            descricao = motos[chassi][CONST_FIELD_DESCRICAO]
            estoque = motos[chassi][CONST_FIELD_ESTOQUE] - tirar
            motos[chassi] = {
                CONST_FIELD_MODEL: modelo,
                CONST_FIELD_BRAND: marca,
                CONST_FIELD_YEAR: ano,
                CONST_FIELD_PRECO: preco,
                CONST_FIELD_DESCRICAO: descricao,
                CONST_FIELD_ESTOQUE: estoque
            }
        else:
            print("Operação cancelada")


def load_file(filename):
    """
    Carrega o arquivo do banco

    :param filename: Nome do arquivo do banco de dados
    :return: None
    """
    motos = util.file_read_bin(filename)
    return motos


def save_file(filename, motos):
    """
    Salve um arquivo do banco

    :param filename: Nome do arquivo do banco de dados
    :param motos: Dicionário que armazena os dados da moto
    :return: None
    """
    util.file_write_bin(filename, motos)


def menu():
    """
    Menu com as opções do sistema

    :return: Retorna a opção escolhida pelo cliente
    """
    print("*** Sistema de Cadastro de Motos ***")
    print("1. Cadastrar moto")
    print("2. Pesquisar moto")
    print("3. Listar motos")
    print("4. Alterar dados das motos")
    print("5. Excluir moto")
    print("6. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções", 1, 6)


def main(motos):
    """
    Ponto de entrada do módulo

    :return: None
    """
    filename = "dbmotos"
    motos = load_file(filename)
    while True:
        op = menu()
        if op == 1:
            moto_add(motos)
        elif op == 2:
            moto_query(motos)
        elif op == 3:
            moto_list(motos)
        elif op == 4:
            moto_edit(motos)
        elif op == 5:
            moto_del(motos)
        elif op == 6:
            save_file(filename, motos)
            break


if __name__ == '__main__':
    products = {}
    main(products)
