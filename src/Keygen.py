# ----------------------------------------------
# sdes-implementation/src/Keygen.py
#
# SDES implementation in Python
#
# Applied Cryptography Class
# <diogopinto> 2025+
# ----------------------------------------------

from CryptoOperations import CryptoOperations

class Keygen:

    # PT: Primeiro precisamos de gerar as sub-chaves através da chave principal
    def gen_subkeys(key):

        # PT: Verificação de que o input está em binário
        for bit in key:
            if bit != '0' and bit != '1':

                print("[SDES] Only binary input is accepted!")
                exit(-1)

        # PT: Verifica se é uma string convencional 
        if type(key) is str:

            # PT: Passar de string convencional para string bytes
            key = key.encode()

        # PT: Verifica o comprimento do input
        if len(key) != 10:
            print("[SDES] The length of the key has to be 10 bits!")
            exit(-1)

        p10_result = CryptoOperations.permutate(key, CryptoOperations.p10)

        # PT: Separar os resultados em left e right para a próxima operação
        p10_result_left = p10_result[:5]
        p10_result_right = p10_result[5:10]

        # PT: Calcular o LS-1
        ls1_result_left = CryptoOperations.permutate(p10_result_left, CryptoOperations.ls1)
        ls1_result_right = CryptoOperations.permutate(p10_result_right, CryptoOperations.ls1)

        # PT: Obter o p8 e guardar este valor como a primeira chave
        p8_result = CryptoOperations.permutate((ls1_result_left + ls1_result_right), CryptoOperations.p8)
        skey1 = p8_result

        # PT: Calcular o LS-2
        ls2_result_left = CryptoOperations.permutate(ls1_result_left, CryptoOperations.ls2)
        ls2_result_right = CryptoOperations.permutate(ls1_result_right, CryptoOperations.ls2)

        # PT: Calcular o p8 e guardar o resultado como a segunda chave
        p8_result = CryptoOperations.permutate((ls2_result_left + ls2_result_right), CryptoOperations.p8)
        skey2 = p8_result

        return [skey1, skey2]    