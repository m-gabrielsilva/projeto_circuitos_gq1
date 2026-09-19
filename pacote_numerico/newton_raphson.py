def newton_raphson(f, df, x0, eps1=1e-6, eps2=1e-6, kmax=100):

    x = x0
    hist = []

    for k in range(1, kmax + 1):
        derivada = df(x)
        if derivada == 0:
            raise ZeroDivisionError(f"Derivada nula na iteração {k} para x = {x}")

        x_novo = x - f(x) / derivada
        hist.append((k, x_novo, f(x_novo), abs(x_novo - x)))

        if abs(f(x_novo)) < eps1 or abs(x_novo - x) < eps2:
            return x_novo, hist

        x = x_novo

    return x, hist
