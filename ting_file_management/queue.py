from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):  # Construtor
        """Aqui irá sua implementação"""
        self.list = list()

    def __len__(self):  # Retorna o tamanho da lista
        """Aqui irá sua implementação"""
        return len(self.list)

    def enqueue(self, value):  # Adiciona dados
        """Aqui irá sua implementação"""
        return self.list.append(value)

    def dequeue(self):  # Remove dados
        """Aqui irá sua implementação"""
        return self.list.pop(0)

    def search(self, index):  # Busca dados
        """Aqui irá sua implementação"""
        if 0 > index or index >= len(self.list):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.list[index]
