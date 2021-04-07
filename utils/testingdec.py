from SymmetricDecryption import aesDecrypt
from SymmetricEncryption import aesEncrypt
from keygenerator import passgen, decPassgen

password_provided = input()


file = "testencrypted.txt"

with open(file, 'rb') as f:
    data = f.read()

salt = data[:16]
print(salt)
key = decPassgen(password_provided, 16, salt)
output_file = "testdecrypted.txt"

aesDecrypt(data, key, output_file)
