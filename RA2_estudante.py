# Integrante - 1: Vitor Vieira Machado
# Integrante - 2: Vinicius da Rosa Padilha
# Integrante - 3: 

import numpy as np
import matplotlib.pyplot as plt

# =========== INÍCIO da área onde as funções deverão estar desenvolvidas para ENTREGA

# Função para resolver inequação de 1º grau (ax + b > c)
def resolver_inequacao_1_grau(a, b, c):
    #desenvolva o cálculo necessário
    x = (c - b) / a
    return x

# Função para resolver inequação de 2º grau (ax^2 + bx + c > d)
def resolver_inequacao_2_grau(a, b, c, d):
    #desenvolva o cálculo necessário considerando as 3 situações do delta
    #considere somente raízes reais
    #quando não houver raíz, retorne lista vazia
    #OBS: considere para delta= b**2 - 4*a*(c - d)
    delta =  b**2 - 4*a*(c - d)
    
    if delta < 0:
        return []
    elif delta == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        return [x1, x2]

# Função polinomial de 1º grau
def polinomio_1_grau(a, b, x):
    #desenvolva o cálculo necessário
    conta = a * x + b
    return conta

# Função polinomial de 2º grau
def polinomio_2_grau(a, b, c, x):
    #desenvolva o cálculo necessário
    conta = a * x**2 + b * x + c
    return conta

# Função exponencial
def funcao_exponencial(a, b, x):
    #use a função disponível em Numpy
    conta = a * np.exp(b * x)
    return conta

# Função logarítmica
def funcao_logaritmica(a, b, x):
    #use a função disponível em Numpy
    conta = a * np.log(b * x)
    return conta

# Funções trigonométricas
def funcao_seno(x):
    #use a função trigonométrica disponível em Numpy
    conta = np.sin(x)
    return conta

def funcao_cosseno(x):
    #use a função trigonométrica disponível em Numpy
    conta = np.cos(x)
    return conta
    
def funcao_tangente(x):
    #use a função trigonométrica disponível em Numpy
    conta = np.tan(x)
    return conta

def funcao_cotangente(x):
    #use a função trigonométrica que vc desenvolveu
    tangente = np.tan(x)
    cotangente = 1 / tangente
    return cotangente

def funcao_cossecante(x):
    #use a função trigonométrica que vc desenvolveu    
    sen = np.sin(x)
    cossecante = 1 / sen
    return cossecante

def funcao_secante(x):
    #use a função trigonométrica que vc desenvolveu
    cos = math.cos(x)
    secante = 1 / cos
    return secante

# =========== FIM da área onde as funções deverão estar desenvolvidas para ENTREGA

# Desse ponto em diante, é PROIBIDA a alteração de qualquer linha de código
def imprime_menu():
    print ("\n" * 50) 
    print('******************* MENU *********************')
    print('* 1: Inequação de 1ºgrau (ax+b>c)            *')
    print('* 2: Inequação de 2º grau (ax^2 + bx + c > d)*')
    print('* 3: Função polinomial de 1º grau            *')
    print('* 4: Função polinomial de 2º grau            *')
    print('* 5: Função exponencial                      *')
    print('* 6: Função logarítmica                      *')
    print('* 7: Função seno                             *')
    print('* 8: Função cotangente                       *')
    print('* 9: Função secante                          *')
    print('* 0: Encerrar                                *')
    print('**********************************************')

# Testando as funções
if __name__ == "__main__":
    x_values = np.linspace(-10, 10, 400)
    while True: #repete o programa até 0 ser digitado
        # mostra o menu de opções
        imprime_menu()
        # lê uma opção do usuário
        while True:
            op = int(input('\nDigite uma opção válida do menu:'))
            if 0<=op<=9:
                break
        # verifica qual opção foi digitada e realiza a devida ação
        if op==0: # encerrar o programa
            print('\nEncerrando o programa...')
            break        
        
        elif op==1: # Inequação de 1ºgrau (ax+b>c)
            a1, b1, c1 = 2, 3, 5
            sol_ineq_1 = resolver_inequacao_1_grau(a1, b1, c1)
            print(f"Solução da inequação {a1}x + {b1} > {c1}: x > {sol_ineq_1}")
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50) 

        elif op==2: # Inequação de 2º grau (ax^2 + bx + c > d)
            a2, b2, c2, d2 = 1, -4, 4, 0
            sol_ineq_2 = resolver_inequacao_2_grau(a2, b2, c2, d2)
            print(f"Soluções da inequação {a2}x^2 + {b2}x + {c2} > {d2}: x > {sol_ineq_2}")
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50)     
                    
        elif op==3: # Função polinomial de 1º grau
            y_polinomio_1 = polinomio_1_grau(2, 3, x_values)
            plt.plot(x_values, y_polinomio_1, label='2x + 3')
            plt.title('Função Polinomial de 1º Grau')
            plt.show()
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50) 
            
        elif op==4: # Função polinomial de 2º grau
            y_polinomio_2 = polinomio_2_grau(1, -4, 4, x_values)
            plt.plot(x_values, y_polinomio_2, label='x^2 - 4x + 4')
            plt.title('Função Polinomial de 2º Grau')
            plt.show()
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50) 
            
        elif op==5: # Função exponencial
            y_exponencial = funcao_exponencial(2, 1, x_values)
            plt.plot(x_values, y_exponencial, label='2e^x')
            plt.title('Função Exponencial')  
            plt.show()          
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50) 
            
        elif op==6: # Função logarítmica
            y_logaritmica = funcao_logaritmica(2, 1, x_values[x_values > 0])  # Valores positivos para logaritmo
            plt.plot(x_values[x_values > 0], y_logaritmica, label='2ln(x)')
            plt.title('Função Logarítmica')
            plt.show()
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50) 
            
        elif op==7: # Função seno
            y_seno = funcao_seno(x_values)
            plt.plot(x_values, y_seno, label='sen(x)')
            plt.title('Função Seno')    
            plt.show()        
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50) 
            
        elif op==8: # Função cotangente
            y_cotangente = funcao_cotangente(x_values)
            plt.plot(x_values, y_cotangente, label='cotang(x)')
            plt.title('Função Cotangente')    
            plt.show()              
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50) 
            
        elif op==9: # Função cossecante  
            y_cossecante = funcao_cossecante(x_values)             
            plt.plot(x_values, y_cossecante, label='cossec(x)')
            plt.title('Função Cossecante')    
            plt.show()              
            w = input('Pressione <enter> para continuar...')
            print ("\n" * 50)                                         
