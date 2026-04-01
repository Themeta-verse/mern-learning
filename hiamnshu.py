print("Name: Himanshu Tiwari\nRoll no.: 54\nBranch: CSE\n")
# Publicly shared values
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a primitive root (g): "))
# Alice input
a = int(input("Enter Alice's private key: "))
A = (g ** a) % p
# Bob input
b = int(input("Enter Bob's private key: "))
B = (g ** b) % p
# Shared secret calculation
shared_secret_alice = (B ** a) % p
shared_secret_bob = (A ** b) % p
print("\n--- Results ---")
print("Alice's public key:", A)
print("Bob's public key:", B)
print("Shared secret (Alice):", shared_secret_alice)
print("Shared secret (Bob):", shared_secret_bob)