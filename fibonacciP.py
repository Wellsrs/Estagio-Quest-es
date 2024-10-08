def fibonacci(n):
    """Gera a sequência de Fibonacci até o número n."""
    fib_sequence = [0, 1]  # Começa com os dois primeiros números da sequência
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Soma dos dois últimos
        if next_fib > n:
            break  # Para se o próximo número for maior que n
        fib_sequence.append(next_fib)  # Adiciona o próximo número à sequência
    return fib_sequence

# Solicita ao usuário um número
try:
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    
    # Gera a sequência de Fibonacci até o número informado
    sequencia = fibonacci(numero)
    
    # Verifica se o número está na sequência
    if numero in sequencia:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
