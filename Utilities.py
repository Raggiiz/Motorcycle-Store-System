"""
Módulo de funções úteis
"""
import pickle

def get_int_value_with_range(message: str, min_value: int, max_value: int) -> int:
    """
    Valida dados inteiros em um determinado range

    :param message: A mensagem a ser exibida
    :param min_value: Valor inteiro mínimo
    :param max_value: Valor inteiro máximo
    :return: Retorna a opção escolhida dentro do range
    """
    while True:
        try:
            op = int(input(message + ": "))  # recebe o número da opção escolhida
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= op <= max_value:
            print("Opção inválida: escolha um número de", min_value, "a", max_value)
        else:
            return op


def get_yes_no_value(message: str) -> str:
    """
    Valida opções de sim e não

    :param message: A mensagem a ser exibida
    :return: Retorna a opção escolhida s/n
    """
    while True:
        op = input(message + " (s/n): ")
        if op == 's' or op == 'n':
            return op
        else:
            print("Opção inválida: escolha s (sim) ou n (não)")

def file_read_bin(filename: str) -> dict:
    """
    
    """
    content = {}
    try:
        file = open(filename, "rb")
        content = pickle.load(file)
        file.close()
    except IOError:
        pass
    return content


def file_write_bin(filename: str, content: dict):
    """
    
    """
    file = open(filename, "wb")
    pickle.dump(content, file)
    file.close()