# encryption_project


## Instructions

1. Download 
2. Extract in a folder
3. Open with visual studio code

Commands:

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    py manage.py runserver

# Admin login
1. http://127.0.0.1:8000/admin
2. username = admin / password= password

## Description
    The whole project was built having in mind that I can extend the abilities
    of django framework by adding my own logic(in this case is the encryption.py).
    


# Applications
1. Text encryption
2. File content encryption
3. Login registration
    1.Text encryption:
        Takes an input text and using the encryption.py and specifically a similar
        to ceasar's cipher algorithm encrypts the text. Also decrypts the encrypted text .
    
    2.File content encryption:
        Takes input a file (e.g .txt ) and encrypts its content , given back the encrypted file , also can decrypt a file which is encrypted by the same app.
    
    3.Login registration:
        Simple app login-registration-logout with custom forms 

    Django Ratelimit:
        also this project makes use of django Ratelimit to limit 