def newton_raphson_circuito(i0, eps1=1e-6, eps2=1e-6, kmax=100):

    def f(i):
        return -i**3 - 2*i + 10
        
    def df(i):
        return -3*i**2 - 2

    i_k = i0
    hist = []

    for k in range(1, kmax + 1):
        i_novo = i_k - f(i_k) / df(i_k)
        hist.append((k, i_novo, f(i_novo)))

        if abs(f(i_novo)) < eps1 or abs(i_novo - i_k) < eps2:
            return i_novo, hist

        i_k = i_novo

    return i_k, hist
