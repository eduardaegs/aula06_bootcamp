def media_notas():
    lista_notas = []
    for i in range(4):
        notas = float(input(f"Digite a nota {i + 1}: "))
        lista_notas.append(notas)
    media = sum(lista_notas) / len(lista_notas)
    print(f"A média é: {media:.2f}")


media_notas()
