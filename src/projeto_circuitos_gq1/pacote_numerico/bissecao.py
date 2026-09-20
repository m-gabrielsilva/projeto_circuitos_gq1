import pandas as pd

def metodo_bissecao(f, a, b, tol, max_iter):
    historico = []
  
    if f(a) * f(b) >= 0:
        raise ValueError("O intervalo inicial é inválido. f(a) e f(b) devem ter sinais opostos.")
    
    k = 0
  
    while (b - a) >= tol and k < (max_iter + 1):

        x = (a + b) / 2.0 
        erro = abs(b-a) / 2
        historico.append({'Iteração': k+1, 'x_novo': x, 'Erro': erro})

        if f(x) == 0:
            a = x
            b = x
            break 
            
        if f(a) * f(x) < 0:
            b = x  
        else:
            a = x
            
        k += 1
        
    raiz_aprox = (a + b) / 2.0
    
    return pd.DataFrame(historico), raiz_aprox, k


# =====================================================================
# ÁREA DE TESTES LOCAIS (Segura para exportação)
# =====================================================================
if __name__ == "__main__":
    # 1. Definimos a equação do Problema 1
    f_circuito = lambda i: -i**3 - 2*i + 10
    
    # 2. Executamos o método liberando a precisão
    print("--- Teste de Validação: Método da Bisseção ---")
    raiz, iteracoes = metodo_bissecao(f_circuito, 1, 2, 0.0001, 100)
    print(f"\nAproximação parada na iteração {iteracoes}: {raiz}")
