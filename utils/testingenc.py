from SymmetricDecryption import aesDecrypt
from SymmetricEncryption import aesEncrypt
from keygenerator import passgen
import os

password_provided = input()

key, salt = passgen(password_provided, 16)

file = "test.txt"

aesEncrypt(file, key, salt, "testencrypted.txt")
