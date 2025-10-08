# ----------------------------------------------
# sdes-implementation/src/Encryptions.py
#
# SDES implementation in Python
#
# Applied Cryptography Class
# <diogopinto> 2025+
# ----------------------------------------------

from CryptoOperations import CryptoOperations

class Encrypting:

    # PT: Encriptação do plaintext
    def encrypt_text(plaintext, keys):
         # PT: Verificação de que o plaintext está em binário
        for char in plaintext:
            if char != '0' and char != '1':

                print("[SDES] Only binary input is accepted!")
                exit(-1)

        # PT: Verifica se é uma string convencional 
        if type(plaintext) is str:

            # PT: Passar de string convencional para string bytes
            plaintext = plaintext.encode()

        # PT: Verifica o comprimento do input
        if len(plaintext) != 8:
            print("[SDES] The length of the plaintext has to be 10 bits!")
            exit(-1)

        ###############
        # 1ª Iteração #
        ###############

        ip_result = CryptoOperations.permutate(plaintext, CryptoOperations.ip)

        # PT: Separar os resultados em left e right para a próxima operação
        # PT: Este resultado do IP da esquerda vai ser usado mais tarde para fazer XOR com o P4
        ip_result_left = ip_result[:4]
        ip_result_right = ip_result[4:8]

        # PT: Calculamos o E/P com o que vem da direita do IP
        ep_result = CryptoOperations.permutate(ip_result_right, CryptoOperations.ep)

        # PT: Damos XOR com a SKey1
        xor_ep_skey1_result = format(int(ep_result, 2) ^ int(keys[0], 2), "08b")

        # PT: Separar os resultados em left e right para a próxima operação
        xor_ep_skey1_result_left = xor_ep_skey1_result[:4]
        xor_ep_skey1_result_right = xor_ep_skey1_result[4:8]

        # PT: Caixas S
        s0_result = CryptoOperations.s_boxes(xor_ep_skey1_result_left, CryptoOperations.s0)
        s1_result = CryptoOperations.s_boxes(xor_ep_skey1_result_right, CryptoOperations.s1)
        s_result = s0_result + s1_result

        # PT: Calculo do P4
        p4_result = CryptoOperations.permutate(s_result, CryptoOperations.p4)

        # PT: XOR com o resultado à esquerda do IP
        xor_p4_ip_result_left = format(int(p4_result, 2) ^ int(ip_result_left, 2), "04b")

        # PT: Agora damos o SWAP para finalizar a primeira iteração
        swapped_left = ip_result_right
        swapped_right = xor_p4_ip_result_left 


        ###############
        # 2ª Iteração #
        ###############

        # PT: Calculamos o E/P com o que vem da direita do swap
        ep_result_2 = CryptoOperations.permutate(swapped_right, CryptoOperations.ep)

        # PT: Damos XOR com a SKey2
        xor_ep_skey2_result = format(int(ep_result_2, 2) ^ int(keys[1], 2), "08b")

        # PT: Separar os resultados em left e right para a próxima operação
        xor_ep_skey2_result_left = xor_ep_skey2_result[:4]
        xor_ep_skey2_result_right = xor_ep_skey2_result[4:8]

        # PT: Caixas S
        s0_result_2 = CryptoOperations.s_boxes(xor_ep_skey2_result_left, CryptoOperations.s0)
        s1_result_2 = CryptoOperations.s_boxes(xor_ep_skey2_result_right, CryptoOperations.s1)
        s_result_2 = s0_result_2 + s1_result_2

        # PT: Calculo do P4
        p4_result_2 = CryptoOperations.permutate(s_result_2, CryptoOperations.p4)

        # PT: XOR com o resultado à esquerda do IP
        xor_p4_sw_result_left = format(int(p4_result_2, 2) ^ int(swapped_left, 2), "04b")

        # TODO: Fazer uma função para o algoritmo principal, para não estar a repetir código
        # ainda não o fiz porque o final das iteraçoes é sempre diferente.... e por preguiça também

        # PT: Concatenar o resultado do XOR com o valor do swap right
        xor_concat_sw_right = xor_p4_sw_result_left + swapped_right

        # PT: Permutação IP⁻¹ / Permutação final
        return CryptoOperations.permutate(xor_concat_sw_right, CryptoOperations.ip_negative)