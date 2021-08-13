import sys
from queue import Queue


def process(path_file, instance):
    """Criar uma instância da fila,
    Armazenar as linhas do arquivo na fila,
    Retornar nome do arquivo, qtd de linhas e as linhas."""

    if len(instance) != 0:
        return None
    instance.enqueue(path_file)

    file_lines = []
    with open(path_file) as file:
        for line in file:
            file_lines.append(line.strip('\n'))

    file_report = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }
    print(file_report, file=sys.stdout)


def remove(instance):
    """Remove o primeiro arquivo processado"""
    if len(instance) > 0:
        removed = instance.dequeue()
        print(f'Arquivo {removed} removido com sucesso', file=sys.stdout)
    else:
        print('Não há elementos', file=sys.stdout)


def file_metadata(instance, position):
    """Exibe a informação do arquivo no index 'position'"""
    try:
        path_file = instance.get(position)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
        return None

    file_lines = []
    with open(path_file) as file:
        for line in file:
            file_lines.append(line.strip('\n'))

    file_report = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }
    print(file_report, file=sys.stdout)


if __name__ == "__main__":
    my_instance = Queue()
    process('statics/arquivo_teste.txt', my_instance)
    process('statics/arquivo_teste2.txt', my_instance)
    print(len(my_instance))
    my_instance.print_lines()
