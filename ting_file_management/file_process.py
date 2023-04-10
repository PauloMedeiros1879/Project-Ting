import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    archive = txt_importer(path_file)  # Dados do arquivo
    data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(archive),
            "linhas_do_arquivo": (archive),
        }

    instance.enqueue(data)
    sys.stdout.write(str(data))
    return data


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
