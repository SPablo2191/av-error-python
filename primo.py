def es_primo n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1,-1):
        if n % i == 0:
            return False
    return True

# Ejemplo de uso
num = 17
print(f"{num} es primo: {es_primo(num)}")  # True
