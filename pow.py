import hashlib


def find_nonce(message, difficulty):
    nonce = 0
    prefix = "0" * difficulty
    while True:
        data = message + str(nonce)
        hash_result = hashlib.sha256(data.encode()).hexdigest()
        if hash_result[:difficulty] == prefix:
            return nonce
        nonce += 1


message = "1d9a93388c25ace105f30f48c732"
difficulty = 2
nonce = find_nonce(message, difficulty)
print("Nonce encontrado:", nonce)
