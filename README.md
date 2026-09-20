# Projeto 1°GQ - Métodos Numéricos

Solução numérica para o Problema 1: **Circuito elétrico com dispositivo não linear**, onde a corrente $i$ é determinada através da equação $f(i) = -i^3 - 2i + 10 = 0$.

A arquitetura do projeto isola as implementações numéricas (Métodos da Bisseção, Newton-Raphson e Secantes) dentro de um pacote Python instalável chamado `pacote_numerico`, deixando a análise de dados e gráficos restritas ao Jupyter Notebook.

## Estrutura do Projeto

```
projeto_circuitos_gq1/
├── pacote_numerico/       # Pacote com os métodos numéricos
│   ├── bissecao.py
│   ├── newton_raphson.py
│   └── secantes.py
├── notebooks/
│   └── pratica.ipynb      # Análise comparativa e gráficos
├── pyproject.toml         # Configuração do pacote instalável
└── README.md
```

## Como Instalar e Executar

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/m-gabrielsilva/projeto_circuitos_gq1.git
   cd projeto_circuitos_gq1
   ```

2. **Instalar o pacote (recomendado usar um ambiente virtual):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # no Windows: venv\Scripts\activate
   pip install .
   ```

3. **Rodar o notebook:**
   ```bash
   jupyter notebook notebooks/pratica.ipynb
   ```
   Com o pacote instalado, os métodos podem ser importados diretamente:
   ```python
   from pacote_numerico.bissecao import metodo_bissecao
   from pacote_numerico.newton_raphson import newton_raphson
   from pacote_numerico.secantes import metodo_secantes
   ```

## Métodos Implementados

- **Bisseção** (`pacote_numerico/bissecao.py`): busca a raiz por bisseção de intervalo, com intervalo inicial [1, 2].
- **Newton-Raphson** (`pacote_numerico/newton_raphson.py`): usa a derivada de f(i) para convergência mais rápida, partindo de i₀ = 1.5.
- **Secantes** (`pacote_numerico/secantes.py`): aproxima a derivada por diferenças finitas entre dois pontos, sem precisar calculá-la analiticamente.

Todos os métodos usam tolerância de 1e-6 e limite de 100 iterações como critérios de parada.
