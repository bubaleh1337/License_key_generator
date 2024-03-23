import secrets
import string

def generate_license_key(length):
    alphabet = string.ascii_letters + string.digits
    key_bytes = secrets.token_bytes(length)
    license_key = ''.join(alphabet[b % len(alphabet)] for b in key_bytes)
    return license_key

def save_license_keys(file_path, num_keys, key_length):
    with open(file_path, 'a') as file:
        for _ in range(num_keys):
            license_key = generate_license_key(key_length)
            file.write(license_key + '\n')

# Укажите путь к файлу, куда будут сохранены ключи
file_path = 'license_keys.txt'
# Укажите количество ключей для сохранения
num_keys = 1
# Укажите длину каждого ключа
key_length = 16

# Сохранение ключей в файл без перезаписи
save_license_keys(file_path, num_keys, key_length)
print(f"Сгенерированные ключи сохранены в файл {file_path}")
