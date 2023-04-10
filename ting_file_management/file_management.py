import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith('txt'):
        return sys.stderr.write('Formato inválido\n')

    try:
        with open(path_file, mode="r") as file:
            data = file.read().split('\n')
            return data

    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
