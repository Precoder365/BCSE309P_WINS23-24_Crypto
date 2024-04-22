import hmac
import hashlib

def generate_hmac(key, message):
    hash_function = hashlib.sha256
    hmac_obj = hmac.new(key.encode(), message.encode(), hash_function)
    hmac_digest = hmac_obj.digest()
    return hmac_digest

def verify_hmac(key, message, hmac_digest):
    hash_function = hashlib.sha256
    hmac_obj = hmac.new(key.encode(), message.encode(), hash_function)
    computed_hmac_digest = hmac_obj.digest()
    return hmac.compare_digest(hmac_digest, computed_hmac_digest)

key = "secretkey"
message = input("Enter the message: ")
hmac_digest = generate_hmac(key, message)
print("Generated HMAC digest:", hmac_digest.hex())

is_valid = verify_hmac(key, message, hmac_digest)
print("Is valid HMAC?", is_valid)
