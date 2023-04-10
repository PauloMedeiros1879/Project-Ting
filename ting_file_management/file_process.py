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
    if not len(instance):
        sys.stdout.write('Não há elementos\n')
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        archive = f'Arquivo {path_file} removido com sucesso'
        print(archive, file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
