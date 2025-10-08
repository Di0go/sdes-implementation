# ----------------------------------------------
# sdes-implementation/src/CryptoOperations.py
#
# SDES implementation in Python
#
# Applied Cryptography Class
# <diogopinto> 2025+
# ----------------------------------------------

# PT: Classe de helpers para os cálculos como permutações, expansões, compressões, ....
class CryptoOperations:

    # TODO: Mudar o nome desta classe
    # TODO: Criar uma função para calcular o XOR entre byte strings (já que o python apenas permite calcular com ints .-.)
    # Vamos ter que passar as byte strings para ints, calcular o XOR e converter de volta para binário e depois de novo para bytestring

    # PT: Vamos usar 4 listas dentro de uma lista (matrizes) para representar as S Boxes, 
    # onde o index da lista principal vai representar as linhas e o index das nested lists vai representar as colunas
    s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    # PT: Listas de permutações, compressões e expansões do algoritmo
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    ip_negative = [4, 1, 3, 5, 7, 2, 8, 6]
    p4 = [2, 4, 3, 1]

    # PT: Listas de permutações, compressões e expansões da geração de chaves
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]
    ls1 = [2, 3, 4, 5, 1]
    ls2 = [3, 4, 5, 1, 2]

    # PT: Helper para calcular permutações, retorna uma byte string permutada pela plist
    # É também compatível para expansões e compressões :)
    def permutate(input, plist):
        permutated_input = ''

        # PT: Verifica se é uma string do tipo byte e dá .decode() caso seja
        if type(input) is bytes:
            input = input.decode()

        # PT: Algoritmo para a permutação
        for item in plist:
            permutated_input += input[item - 1]

        # PT: Depois de calculado dámos encode para string do tipo bytes de novo
        return permutated_input.encode()
    
    # PT: Helper para calcular as Substitution Boxes
    def s_boxes(input, box):

         # PT: Verifica se é uma string do tipo byte e dá .decode() caso seja
        if type(input) is bytes:
            input = input.decode()

        # PT: Linha = 1 ° e 4° bits e Coluna = 2° e 3° bits | Ambos convertidos para decimal
        line = int(input[0] + input[-1], 2)
        column = int(input[1] + input[-2], 2)

        # PT: Vamos buscar o valor à matriz
        box_number = box[line][column]

        # PT: Voltamos a converter o valor para binário com duas casas (00, 01, 10, 11)
        return format(box_number, "02b").encode()