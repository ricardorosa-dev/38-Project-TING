import sys


def txt_importer(path_file):
    extension = path_file.split('.')[1]
    if extension != "txt":
        print('Formato inválido', file=sys.stderr)
        return None
    try:
        with open(path_file) as file:
            return_file = [line.strip('\n') for line in file]
        return return_file
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)


if __name__ == "__main__":
    txt_importer('statics/arquivo_teste.txt')
