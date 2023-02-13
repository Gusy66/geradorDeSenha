import random
import string

def generate_password(length=8):
    # Gera uma lista de caracteres aleatórios, incluindo letras maiúsculas, letras minúsculas e números
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    
    # Escolhe aleatoriamente `length` caracteres da lista `chars`
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

# Teste o gerador de senha
password = generate_password()
print("Sua nova senha é: ", password)
