# ----------------------------------------------
# sdes-implementation/src/sdes.py
#
# SDES implementation in Python
#
# Applied Cryptography Class
# <diogopinto> 2025+
# ----------------------------------------------

# Bloco de entrada: 8 bits
# Chave: 10 bits
# Input de entrada: Binário

from Keygen import Keygen
from Encryption import Encrypting
from Decryption import Decrypting


# PT: Interação com o utilizador
def main():
    while True:
        print("\n===============\n" +
              "1.) Encrypt\n" +
              "2.) Decrypt\n" +
              "3.) Generate keys\n" +
              "4.) Exit\n" +
              "===============\n")
        user_choice = input("Select an option > ")

        match user_choice:
            case '1':
                plaintext = str(input("Input your 8 bit text > "))
                key = str(input("Input your 10 bit key > "))

                print("\nYour cipher is: " + Encrypting.encrypt_text(plaintext, Keygen.gen_subkeys(key)).decode())


            case '2':
                cipher = str(input("Input your 8 bit cipher > "))
                key = str(input("Input your 10 bit key > "))

                print("\nYour plaintext is: " + Decrypting.decrypt_text(cipher, Keygen.gen_subkeys(key)).decode())

            case '3':
                key = str(input("Input your 10 bit key > "))
                keys = Keygen.gen_subkeys(key)

                print(f"\nYour keys are {keys[0].decode()} and {keys[1].decode()}")

            case '4': 
                exit(0)

            case _:
                print("[SDES] Invalid choice!\n")
                continue


if __name__=="__main__":
    main()