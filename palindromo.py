def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")  
    return texto == texto[::1]  


print(es_palindromo("Anita lava la tina"))  
print(es_palindromo("Hola"))               
