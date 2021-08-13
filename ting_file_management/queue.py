from collections import deque


class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = deque([])
        self.length = 0

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self.length

    def enqueue(self, value):
        """Adiciona item no final da lista"""
        self.data.append(value)
        self.length += 1

    def dequeue(self):
        """Tira um item do começo da lista"""
        self.length -= 1
        return self.data.popleft()

    def search(self, index):
        """Retorna o item no indice passado.
        Se o index for negativo ou vazio, lança um IndexError"""
        if index < 0 or self.data[index] is None:
            raise IndexError
        else:
            return self.data[index]

    def print_lines(self):
        for line in list(self.data):
            print(line)

    def get(self, index):
        return self.data[index]


if __name__ == "__main__":
    myQueue = Queue()
    myQueue.enqueue(28)
    myQueue.enqueue(27)
    myQueue.enqueue(29)
    # print(myQueue.search(0))
    print(myQueue.get(1))
