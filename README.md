# 🧩 S-DES Implementation in Python

A small, from-scratch implementation of the **Simplified Data Encryption Standard (S-DES)** for learning and résumé demonstration.  
Developed for my Applied Cryptography class — clear, readable code that shows the internal steps of a symmetric cipher.

---

## Project structure

~~~text
sdes-implementation/
│
├── sdes.py              # Main CLI program (entry point)
├── Keygen.py            # Subkey generation (Keygen class)
├── CryptoOperations.py  # Permutations, S-boxes, helpers
├── Encryption.py        # Encryption flow (Encrypting class)
└── Decryption.py        # Decryption flow (Decrypting class)
~~~

---

## Module responsibilities

- **Keygen.py** — Generates subkeys from a 10-bit key.  
- **CryptoOperations.py** — Implements permutations, S-boxes, and low-level helpers.  
- **Encryption.py** — Implements the S-DES encryption routine.  
- **Decryption.py** — Implements the reverse routine using subkeys in reverse order.  
- **sdes.py** — Simple CLI to run Encrypt / Decrypt / Generate keys.

---

## How it works

S-DES (Simplified Data Encryption Standard) is a reduced version of the DES cipher, designed for teaching purposes. 
It operates on **8-bit plaintext blocks** and uses a **10-bit key** to produce an **8-bit ciphertext**.

### 🔑 1. Key generation
The 10-bit user key is transformed into two 8-bit **subkeys** (`SK1`, `SK2`):

1. **P10 permutation** — reorders the bits of the key according to a fixed pattern.  
2. **Left shift (LS-1)** — both halves of the permuted key are rotated left by one position.  
3. **P8 permutation** — compresses and reorders the 10-bit value into 8 bits → this is **SK1**.  
4. **Left shift (LS-2)** — both halves are rotated left by two positions.  
5. **P8 permutation again** — produces **SK2**.  

These two subkeys are used in the two rounds of encryption.

---

### 🔒 2. Encryption process

Given an 8-bit plaintext block and the two subkeys:

1. **Initial Permutation (IP)** — reorders the plaintext bits into a new 8-bit sequence.  
2. **Split** into left (L) and right (R) 4-bit halves.  
3. **Round 1:**
   - Expand and permute R using **EP**, producing 8 bits.
   - XOR the result with **SK1**.
   - Split into two 4-bit halves → pass each half through the **S-boxes (S0 and S1)**.
   - Concatenate and permute the 4-bit result using **P4**.
   - XOR the P4 output with L.
   - Swap the two halves → output of round 1 becomes input for round 2.
4. **Round 2:**
   - Repeat the same process, but this time use **SK2** instead of SK1.
   - Skip the swap at the end of this round.
5. **Inverse Initial Permutation (IP⁻¹)** — final permutation to produce the ciphertext.

Result → **8-bit ciphertext**.

---

### 🔓 3. Decryption process

Decryption is **identical to encryption**, except the subkeys are applied in reverse order:

1. Apply **SK2** during the first round.  
2. Apply **SK1** during the second round.  
3. The rest of the operations (permutations, XOR, S-boxes, etc.) remain the same.

This symmetry is a property of the Feistel structure — it makes encryption and decryption processes mirror each other.

---

## Usage

Run the CLI:

~~~bash
python3 sdes.py
~~~
