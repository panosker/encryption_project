from random import choice
nums = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['<','>','@','!','$','-','%',',','?','+']

def encrypt(text):
    shift = choice(range(1,10))
    
    encrypted_text = ""
    for char in text:
        if isinstance(char, str):
            if char.isalpha():
                if char.isupper():
                    encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                encrypted_text += encrypted_char
            else:
                if char == " ":
                    encrypted_text += "/"
                elif char == "/":
                    encrypted_text += " "
                elif char in nums :
                    ind = nums.index(char)
                    encrypted_text += symbols[ind]
                elif char in symbols:
                    ind=symbols.index(char)
                    encrypted_text += nums[ind]
                else:
                    encrypted_text += char
        else:
            encrypted_text += str(char)    
    encrypted_text+= str(shift)
    return encrypted_text + encrypted_text + encrypted_text


def decrypt(encrypted_text):
    decrypted_text = ""
    shift=int(encrypted_text[-1])
    endpoint = int(len(encrypted_text)/3-1)
    for char in encrypted_text[:endpoint]:
        if isinstance(char, str):
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                decrypted_text += decrypted_char
            else:
                if char == " ":
                    decrypted_text += "/"
                elif char == "/":
                    decrypted_text += " "
                elif char in nums :
                    ind = nums.index(char)
                    decrypted_text += symbols[ind]
                elif char in symbols:
                    ind=symbols.index(char)
                    decrypted_text += nums[ind]
                else:
                    decrypted_text += char    
        else:
            decrypted_text += char
    return decrypted_text

