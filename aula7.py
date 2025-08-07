frutas = []

for i in range(3):
    x = input(f"Digite o nome da {i+1}ª fruta: ")
    while len(x) < 4:
        x = input("Digite uma fruta valida!: ")
    frutas.append(x)

print(f"Lista de frutas: {frutas}")
