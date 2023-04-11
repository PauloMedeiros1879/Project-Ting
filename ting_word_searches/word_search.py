def exists_word(word, instance):
    # Cria uma lista vazia para armazenar os resultados da busca
    search_info = []

    # Itera sobre cada arquivo no objeto "instance"
    for index in range(len(instance)):
        # Obtém o arquivo atual
        archive = instance.search(index)

        # Cria um dicionário para armazenar as informações do arquivo atual
        archive_data = {
            "palavra": word,
            "arquivo": archive["nome_do_arquivo"],
            "ocorrencias": [],
        }

        # Itera sobre cada linha do arquivo atual
        amount = 0
        for line in archive["linhas_do_arquivo"]:
            # Se a palavra for encontrada na linha, adiciona a
            # informação da linha na lista de ocorrências
            if word.lower() in line.lower():
                amount += 1
                archive_data["ocorrencias"].append({"linha": amount})

        # Se houver alguma ocorrência da palavra no arquivo atual,
        # adiciona as informações do arquivo à lista de resultados da busca
        if len(archive_data["ocorrencias"]) > 0:
            search_info.append(archive_data)

    # Retorna a lista de resultados da busca
    return search_info


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
