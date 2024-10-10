# Questão 5
def inverter_string(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string_original = input("Digite a string que deseja inverter: ")

resultado = inverter_string(string_original)

print(f"String invertida: {resultado}")
