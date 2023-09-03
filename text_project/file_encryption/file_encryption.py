from django.conf import settings
from django.core.files.base import ContentFile
from encr_decr_app.encryption import encrypt, decrypt
import os

def file_encrypt(file):
    encrypted_data = encrypt(file.read().decode())
    encrypted_file = ContentFile(encrypted_data.encode())

    # Set the name and content type of the encrypted file
    file_name = file.name
    encrypted_file.name = 'encrypted' + file_name 
    encrypted_file.content_type = 'text/plain'

    # Save the encrypted file inside the 'encrypted_files' folder
    file_path = os.path.join(settings.ENCRYPTED_FILES_PATH, encrypted_file.name)
    with open(file_path, 'wb') as destination:
        for chunk in encrypted_file.chunks():
            destination.write(chunk)

    return file_path

def file_decrypt(file):
    decrypted_data = decrypt(file.read().decode())
    decrypted_file = ContentFile(decrypted_data.encode())

    # Set the name and content type of the decrypted file
    file_name = file.name
    decrypted_file.name = 'decrypted_file' + file_name
    decrypted_file.content_type = 'text/plain'

    # Save the decrypted file inside the 'encrypted_files' folder
    file_path = os.path.join(settings.ENCRYPTED_FILES_PATH, decrypted_file.name)
    with open(file_path, 'wb') as destination:
        for chunk in decrypted_file.chunks():
            destination.write(chunk)

    return file_path