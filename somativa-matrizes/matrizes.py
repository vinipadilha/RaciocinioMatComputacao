# Integrante - 1: Vinicius da Rosa Padilha
# Integrante - 2: Murilo Regnier Stange

matrizA = [
    [3, 4, -2],
    [8, 0, 2],
    [1, 1, -2]
]
matrizB = [
    [4, 2],
    [4, 2],
    [-4, -2]
]

matrizC = [
    [0, 2, 0],
    [-3, -4, 2],
    [7, 2, -1]
]

matriz1 = [
    [],
    [],
    []
]

matriz2 = [
    [],
    [],
    []
]


matriz3 = [
    [],
    [],
    []
]


for i in range(3):
    for j in range(3):
        valor = matrizA[i][j] + matrizC[i][j]
        matriz1[i].append(valor)

print("========= A + C ===========")
for i in range(3):
    print(matriz1[i])



for i in range(3):
    for j in range(2):
        valor = matrizB[i][j] - matrizB[i][j]
        matriz2[i].append(valor)

print("========= B - B ===========")
for i in range(3):
    print(matriz2[i])



for i in range(3):
    for j in range(3):
        valor = (matrizA[i][j] * 3) - (matrizC[i][j] * 2)
        matriz3[i].append(valor)


print("========= 3A - 2C  ===========")
for i in range(3):
    print(matriz3[i])




