try:

    while True:
        nota = int(input("Digite um valor entre [0 e 10]"))
        if nota < 0 or nota > 10:
            print("Error!!!!!!!!!")
        else:
            print(f"Vc digitou: {nota}")
        break
except:
    print("Digite apenas numeros!!!!")
