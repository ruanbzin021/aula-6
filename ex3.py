nome = input("Digite um nome: ").title()
tamanho = len(nome)

while len(nome) < 3:
    nome = input("Digite um nome valido: ").title()
print(f"Nome: {nome}")

idade = int(input("Digite sua idade: "))

while idade < 1 or idade > 149:
        idade = int(input("Digite sua idade entre[1 e 150]: "))
print(f"Idade: {idade}")

salario = float(input("Digite seu salário: "))

while salario < 1:
    salario = float(input("Digite um salário maior que R$0,00: "))

print(f"Salário: R${salario:,.2f}")

while True:
      
    sexo = input("Digite seu sexo (f) ou (m): ").lower()

    if sexo == "f":
          sexo_formatado = "feminino"
          print("Sexo: feminino")
          break
      
    elif sexo == "m":
          sexo_formatado = "masculino"
          print("Sexo: masculino")
          break        
    else:
          print("Digite (F) para feminino e (M) para masculino")   


while True:
    estado_civil = input("Informe seu estado civil: ").lower()

    if estado_civil == "solteiro" or estado_civil == "solteira":
        print(f"Estado civil: {estado_civil}")
        break
    
    elif estado_civil == "casado" or estado_civil == "casada":
        print(f"Estado civil: {estado_civil}")
        break

    elif estado_civil == "viuvo" or estado_civil == "viuva":
        print(f"Estado civil: {estado_civil}")
        break

    elif estado_civil == "divorciado" or estado_civil == "divorciada":
        print(f"Estado civil: {estado_civil}")
        break

    else:
        print("Digite apenas: solteiro, casado, viuvo ou divorciado")


print(f"Nome: {nome}\nIdade: {idade} anos\nSexo: {sexo_formatado}\nestado civil: {estado_civil}\nSalario: R${salario:,.2f}")