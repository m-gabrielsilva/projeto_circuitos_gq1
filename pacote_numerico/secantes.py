"""
Módulo do Método das Secantes
Membro 3 - Validador Numérico e Especialista em Métodos Numéricos
"""
import pandas as pd

def metodo_secantes(f, x0, x1, e1=1e-6, e2=1e-6, kmax=100):
    historico = []
    x_novo = x1

    for k in range(1, kmax + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        denominador = f_x1 - f_x0
        if abs(denominador) < 1e-12:
            raise ZeroDivisionError(f"Divisão por zero na iteração {k}: f(x1) e f(x0) são praticamente iguais.")

        x_novo = x1 - (f_x1 / denominador) * (x1 - x0)
        f_xnovo = f(x_novo)
        var_x = abs(x_novo - x1)

        historico.append({
            'Iteração': k, 
            'x0': x0, 
            'x1': x1, 
            'x_novo': x_novo, 
            'f(x_novo)': f_xnovo, 
            'erro_1': abs(f_xnovo),
            'erro2': var_x
        })

        if abs(f_xnovo) < e1:
            return pd.DataFrame(historico), x_novo, k

        if var_x < e2:
            return pd.DataFrame(historico), x_novo, k

        x0 = x1
        x1 = x_novo

    return pd.DataFrame(historico), x_novo, kmax