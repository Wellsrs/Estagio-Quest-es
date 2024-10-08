# Solicita ao usuário para inserir uma string
string_usuario = input("Digite uma string: ")

# Converte a string para minúsculas para facilitar a verificação
string_lower = string_usuario.lower()

# Conta a ocorrência da letra 'a'
quantidade_a = string_lower.count('a')

# Verifica se a letra 'a' existe na string
if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vez(es) na string.")
else:
    print("A letra 'a' não está presente na string.")
