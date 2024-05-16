import math 
def convGrausRad(numero):
    rad = (numero/180) * math.pi
    return rad

print("-------- Funções Trigonométricas ----------")
angulo = float(input("Digite o valor em graus: "))
conv = convGrausRad(angulo)
print(f"Ângulo {angulo} em graus equivale a {conv:.2f} radianos")