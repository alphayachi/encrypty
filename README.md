# encrypty

Steps to run this in your pc:
1. Clone the repository to your pc.
2. Open the terminal and navigate to the project directory.
3. Create a virtual environment using the command - 'py -m venv venv'.
4. Activate the virtual environment by using the command - 'cd venv/Scripts/' then type the command - 'activate'.
5. Navigate back to the base directory using the command - 'cd ../..'.
6. Install the dependencies using the commang - 'pip install -r requirements.txt'.
7. Run the app.py file using the command - 'app.py'

Using the application:
The application has a checkbox which says 'Help me out here'. Click on it to make the instructions visible. They explain how to use the application step by step.


DISCLAIMER: USE IT WISELY. DON'T TRY TO ENCRYPT FILES WHICH DON'T BELONG TO YOU. BY USING THIS APPLICATION YOU ARE TAKING FULL RESPONSIBILITY FOR THE CONSEQUENCES OF ITS USAGE.

The application currently has three Encryptions to choose from: 
1. Fernet (symmetric encryption), uses PBKDF2HMAC as key derivation function. Fernet is built on AES-CBC (128-bit key) and PKCS7 for padding. It is the most secure in the list but also the most slowest.
2. AES-CBC - AES is both fast, and cryptographically strong. Although Fernet is stronger than vanilla AES-CBC, AES-CBC provides a reasonable security with a faster performance for encrypting and decrypting. You can use this encryption instead of Fernet for faster encryption.
3. ChaCha20Poly1305, Authenticated encryption with associated data (AEAD). It provides strong integrity for the data, has an associated text with it. The associated text including the whitespaces must be the same while decrypting. This cipher uses a 32 byte key.
4. AES-GCM - AES with GCM mode is secure and fast and requires an associated data for maintaining the integrity of the data. This is recommended over AES-CBC.
5. Triple DES - This mode is not recommended beacuse even though it is secure, it is very slow and AES-GCM would be a better choice over it, in respect of both performance and security.

*All these ciphers use custom passwords which undergo key generator functions for the convenience of the user.

![Encrypy image](https://user-images.githubusercontent.com/62387039/114082452-611cea00-98cb-11eb-9432-a8d19e828464.png)

![encrypty image](https://user-images.githubusercontent.com/62387039/119491586-b7f75980-bd7b-11eb-9ee4-d6d5c1e5397e.png)

![Encrypy image encrypted](https://user-images.githubusercontent.com/62387039/114082351-4185c180-98cb-11eb-8046-336bac1af908.png)



