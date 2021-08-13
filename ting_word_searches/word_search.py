# from ting_file_management import file_process
from ting_file_management.queue import Queue
from ting_file_management.file_process import process


def exists_word(word, instance):
    """Retorna as ocorrências de 'word'
    em cada arquivo processado, por linhas"""
    result_list = []
    result_list.append({
        "palavra": word,
        "arquivo": instance.search(0),
        "ocorrencias": []
    })

    for num in range(len(instance)):
        with open(instance.search(0)) as file:
            for index, line in enumerate(file):
                if word in line:
                    result_list[num]['ocorrencias'].append({
                        "linha": index + 1
                        })

    if not result_list[0]['ocorrencias']:
        return []
    else:
        return result_list


def search_by_word(word, instance):
    """Igual à função anterior, porém com o conteúdo?"""
    lower_word = word.lower()
    result_list = []
    result_list.append({
        "palavra": lower_word,
        "arquivo": instance.search(0),
        "ocorrencias": []
    })

    for num in range(len(instance)):
        with open(instance.search(0)) as file:
            for index, line in enumerate(file):
                if lower_word in line.lower().strip('\n'):
                    result_list[num]['ocorrencias'].append({
                        "linha": index + 1, "conteudo": line
                        })

    if not result_list[0]['ocorrencias']:
        return []
    else:
        print(result_list)
        return result_list


if __name__ == "__main__":
    project = Queue()
    process("statics/nome_pedro.txt", project)
    search_by_word("Pedro", project)
