#original trilha python basico
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue # pula a execução

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue 

#     print(numero, end=" ")