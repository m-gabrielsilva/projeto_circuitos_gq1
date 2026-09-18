# Projeto 1°GQ - Métodos Numéricos

Solução numérica para o Problema 1: **Circuito elétrico com dispositivo não linear**, onde a corrente $i$ é determinada através da equação $f(i) = -i^3 - 2i + 10 = 0$.

A arquitetura do projeto isola as implementações numéricas (Métodos da Bisseção, Newton-Raphson e Secantes) dentro de um pacote Python instalável chamado `pacote_numerico`, deixando a análise de dados e gráficos restritas ao Jupyter Notebook.

## Como Instalar e Executar

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/m-gabrielsilva/projeto_circuitos_gq1.git](https://github.com/m-gabrielsilva/projeto_circuitos_gq1.git)
   cd projeto_circuitos_gq1