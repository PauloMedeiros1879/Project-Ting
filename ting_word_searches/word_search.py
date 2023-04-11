def exists_word(word, instance):
    """Aqui irá sua implementação"""
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
    # Cria uma lista vazia para armazenar os resultados da busca
    search_info = []

    # Itera sobre cada arquivo no objeto "instance"
    for index in range(len(instance)):
        # Obtém o arquivo atual
        file = instance.search(index)

        # Cria um dicionário para armazenar as informações do arquivo atual
        file_info = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        # Inicializa o contador de linhas
        amount = 0

        # Itera sobre cada linha do arquivo atual
        for line in file["linhas_do_arquivo"]:
            # Se a palavra for encontrada na linha, adiciona a informação da linha na lista de ocorrências
            if word.lower() in line.lower():
                amount += 1
                file_info["ocorrencias"].append(
                    {
                        "linha": amount,
                        "conteudo": line,
                    }
                )

        # Se houver alguma ocorrência da palavra no arquivo atual, adiciona as informações do arquivo à lista de resultados da busca
        if len(file_info["ocorrencias"]) > 0:
            search_info.append(file_info)

    # Retorna a lista de resultados da busca
    return search_info
