#!/usr/bin/env python3
"""
TryHackMe - Anonymous Playground
Author: Operative
Script: decoder.py
Purpose: Reconstruct plaintext credentials from pair-sum modulo ciphertext.
"""

import sys

def solve_cipher(ciphertext: str) -> str:
    # Validate character stream is strictly even
    if len(ciphertext) % 2 != 0:
        raise ValueError(f"Ciphertext length must be even. Got {len(ciphertext)}.")
    
    # Extract lower 5 bits (alphabetical index 1-26)
    indices = [(ord(char) & 31) for char in ciphertext]
    
    output = []
    for i in range(0, len(indices), 2):
        pair_sum = (indices[i] + indices[i + 1]) % 26
        # Account for edge case where modulo results in 0 (representing 'z' / 26)
        if pair_sum == 0:
            pair_sum = 26
        output.append(chr(pair_sum + 96)) # 96 is base for lowercase ('a' is 97)
    
    return "".join(output)

def main():
    raw_blob = "hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN"
    user_part, pass_part = raw_blob.split("::")
    
    username = solve_cipher(user_part)
    password = solve_cipher(pass_part)
    
    print("=" * 60)
    print(f"[*] Raw Token:       {raw_blob}")
    print(f"[+] Solved Username: {username}")
    print(f"[+] Solved Password: {password}")
    print(f"[+] SSH Command:     ssh {username}@10.49.159.175")
    print("=" * 60)

if __name__ == "__main__":
    main()
