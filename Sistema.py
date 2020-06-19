"""
Ponto de entrada do sistema
"""

import cadastro as c
import produtos as p
import Utilities as util

from datetime import date

CONST_FIELD_COMPRADOR = "comprador"
CONST_FIELD_PRODUTO = "produto"
CONST_FIELD_DATA = "data"


def cart_motos(motos, clients, vendas):
    """
    Carrinho onde você pode comprar um produto

    :param vendas: Dicionário onde armazena os dados das vendas
    :param clients: Dicionário que armazena os dados do cliente
    :param motos: Dicionário que armazena os dados da moto
    :return: mensagem com sucesso ou fracasso da operação
    """
    id = input("Por favor, digite o seu cpf: ")
    if id in clients:
        chassi = input("Digite o chassi da moto que deseja comprar: ")
        if chassi in motos:
            print("Preço da moto: ", motos[chassi][p.CONST_FIELD_PRECO])
            print("Modelo da moto: ", motos[chassi][p.CONST_FIELD_MODEL])
            print("Marca da moto: ", motos[chassi][p.CONST_FIELD_BRAND])
            print("Quant. em estoque: ", motos[chassi][p.CONST_FIELD_ESTOQUE])
            op = util.get_yes_no_value("Tem certeza que quer comprar a moto? ")
            if op == 's':
                print("Novo estoque: ", int(
                    motos[chassi][p.CONST_FIELD_ESTOQUE])-1)
                delete_estoque(motos, chassi)
                vendaid = int(input("Seu id de venda é: "))
                comprador = clients[id][c.CONST_FIELD_NAME]
                modelo = motos[chassi][p.CONST_FIELD_MODEL]
                data_atual = date.today()
                vendas[vendaid] = {
                    CONST_FIELD_COMPRADOR: comprador,
                    CONST_FIELD_PRODUTO: modelo,
                    CONST_FIELD_DATA: data_atual
                }
                print("Moto comprada com sucesso")
            else:
                return False, "Operação cancelada pelo usuário"
        else:
            return False, "Moto não encontrada"
    else:
        c.register_client(id, clients)
        return True, "Cliente cadastrado com sucesso"


def show_register(vendas):
    """
    Mostra todos os registros de vendas

    :param vendas: Dicionário onde armazena os dados das vendas
    :return: mensagem com as vendas
    """
    print("Suas vendas são: ", vendas)


def show_register_by_id(vendas):
    """
    Mostra um registros de vendas na pesquisada

    :param vendas: Dicionário onde armazena os dados das vendas
    :return: mensagem com a venda escolhida
    """
    pesquisa_venda = int(input("Digite um numero do registro de venda: "))
    if pesquisa_venda in vendas:
        print("Registro escolhido: ", vendas[pesquisa_venda])
    else:
        print("Registro não encontrado")


def delete_estoque(motos, chassi):
    """
    Deleta uma moto do banco

    :param chassi: Armazena o número do chassi da moto
    :param motos: Dicionário que armazena os dados da moto
    :return: mensagem com sucesso ou cancelamento da operação
    """
    retirar_do_estoque = 1
    modelo = motos[chassi][p.CONST_FIELD_MODEL]
    marca = motos[chassi][p.CONST_FIELD_BRAND]
    preco = motos[chassi][p.CONST_FIELD_PRECO]
    ano = motos[chassi][p.CONST_FIELD_YEAR]
    descricao = motos[chassi][p.CONST_FIELD_DESCRICAO]
    estoque = motos[chassi][p.CONST_FIELD_ESTOQUE] - retirar_do_estoque
    motos[chassi] = {
        p.CONST_FIELD_MODEL: modelo,
        p.CONST_FIELD_BRAND: marca,
        p.CONST_FIELD_YEAR: ano,
        p.CONST_FIELD_PRECO: preco,
        p.CONST_FIELD_DESCRICAO: descricao,
        p.CONST_FIELD_ESTOQUE: estoque
    }


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
    print("*** Sistema de Cadastro de Produtos ***")
    print("1. Fazer um pedido")
    print("2. Relatório de pedidos")
    print("3. Relatório de pedidos por cliente")
    print("4. Sair")
    print("***************************************\n")
    return util.get_int_value_with_range("Digite uma das opções", 1, 6)


def main():
    """
    Ponto de entrada do módulo

    :return: None
    """
    filename = "vendas"
    vendas = load_file(filename)
    clients = load_file("dbclients")
    motos = load_file("dbmotos")

    while True:
        op = menu()
        if op == 1:
            cart_motos(motos, clients, vendas)
        elif op == 2:
            show_register(vendas)
        elif op == 3:
            show_register_by_id(vendas)
        elif op == 4:
            save_file("dbmotos", motos)
            save_file("dbclients", clients)
            save_file(filename, vendas)
            break


if __name__ == '__main__':
    main()
