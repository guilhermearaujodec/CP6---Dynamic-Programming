# =========================================================
# Problema da Mochila 0/1 — Checkpoint FIAP
# =========================================================

# ---------------------------------------------------------
# Integrantes do Grupo:

# Nome: Augusto Mendonça                        RM: 558371
# Nome: Gabriel Vasquez Queiroz da Silva        RM: 557056    
# Nome: Guilherme Araujo de Carvalho            RM: 558926
# Nome: Gustavo Oliveira                        RM: 559163
# ---------------------------------------------------------

# Quatro abordagens: Gulosa, Recursiva, Memoizada, e Programação Dinâmica
# Dados de exemplo:
# pesos = [2, 3, 4, 1]
# valores = [10, 12, 20, 3]
# capacidade_max = 6
# Solução ótima: valor 30 (itens A + C)

# ----------------------------
# Função 1 — Estratégia Gulosa
# ----------------------------
def knapsack(pesos, valores, W):
    """Resolve o problema da mochila 0/1 usando uma estratégia gulosa.

    A estratégia escolhe itens com maior razão valor/peso até atingir o limite da mochila.
    Obs: Essa abordagem não garante a solução ótima em todos os casos.

    Parâmetros:
        pesos (list[int]): Lista dos pesos dos itens.
        valores (list[int]): Lista dos valores dos itens.
        W (int): Capacidade máxima da mochila.

    Retorno:
        int: Valor total obtido pela estratégia gulosa.

    Complexidade:
        - Tempo: O(n log n)  (devido à ordenação)
        - Melhor caso (Ω): Ω(n)
        - Caso médio (Θ): Θ(n log n)
    """
    itens = sorted(zip(pesos, valores), key=lambda x: x[1]/x[0], reverse=True)
    peso_atual, valor_total = 0, 0

    for peso, valor in itens:
        if peso_atual + peso <= W:
            peso_atual += peso
            valor_total += valor

    return valor_total

# ------------------------------------
# Função 2 — Abordagem Recursiva Pura
# ------------------------------------
def knapsackRec(pesos, valores, W, n=None):
    """Resolve o problema da mochila 0/1 usando recursão pura (sem memoização).

    Parâmetros:
        pesos (list[int]): Lista dos pesos dos itens.
        valores (list[int]): Lista dos valores dos itens.
        W (int): Capacidade máxima da mochila.
        n (int, opcional): Índice atual do item sendo avaliado.

    Retorno:
        int: Valor máximo obtido sem exceder o peso da mochila.

    Complexidade:
        - Tempo: O(2^n)
        - Melhor caso (Ω): Ω(1)
        - Caso médio (Θ): Θ(2^n)
    """
    if n is None:
        n = len(pesos)

    if n == 0 or W == 0:
        return 0

    if pesos[n-1] > W:
        return knapsackRec(pesos, valores, W, n-1)

    incluir = valores[n-1] + knapsackRec(pesos, valores, W - pesos[n-1], n-1)
    excluir = knapsackRec(pesos, valores, W, n-1)

    return max(incluir, excluir)

# ------------------------------------------
# Função 3 — Recursiva com Memoização (Top-Down)
# ------------------------------------------
def knapsackMemo(pesos, valores, W):
    """Resolve o problema da mochila 0/1 usando recursão com memoização.

    Parâmetros:
        pesos (list[int]): Lista dos pesos dos itens.
        valores (list[int]): Lista dos valores dos itens.
        W (int): Capacidade máxima da mochila.

    Retorno:
        int: Valor máximo obtido sem exceder o peso da mochila.

    Complexidade:
        - Tempo: O(n * W)
        - Melhor caso (Ω): Ω(n)
        - Caso médio (Θ): Θ(n * W)
    """
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def solve(i, w):
        if i == 0 or w == 0:
            return 0

        if pesos[i-1] > w:
            return solve(i-1, w)

        incluir = valores[i-1] + solve(i-1, w - pesos[i-1])
        excluir = solve(i-1, w)

        return max(incluir, excluir)

    return solve(len(pesos), W)

# ------------------------------------------------
# Função 4 — Programação Dinâmica (Bottom-Up)
# ------------------------------------------------
def knapsackPD(pesos, valores, W):
    """Resolve o problema da mochila 0/1 usando Programação Dinâmica (Bottom-Up).

    Parâmetros:
        pesos (list[int]): Lista dos pesos dos itens.
        valores (list[int]): Lista dos valores dos itens.
        W (int): Capacidade máxima da mochila.

    Retorno:
        int: Valor máximo possível sem exceder a capacidade da mochila.

    Complexidade:
        - Tempo: O(n * W)
        - Melhor caso (Ω): Ω(n)
        - Caso médio (Θ): Θ(n * W)
    """
    n = len(pesos)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(valores[i - 1] + dp[i - 1][w - pesos[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# -----------------------------
# Testes das quatro abordagens
# -----------------------------
if __name__ == "__main__":
    pesos = [2, 3, 4, 1]
    valores = [10, 12, 20, 3]
    capacidade_max = 6

    print("\n===== Testes do Problema da Mochila =====")
    print(f"Capacidade Máxima: {capacidade_max} kg")
    print(f"Pesos: {pesos}")
    print(f"Valores: {valores}\n")

    print(f"Estratégia Gulosa → Valor total: {knapsack(pesos, valores, capacidade_max)}")
    print(f"Recursiva Simples → Valor total: {knapsackRec(pesos, valores, capacidade_max)}")
    print(f"Com Memoização → Valor total: {knapsackMemo(pesos, valores, capacidade_max)}")
    print(f"Programação Dinâmica → Valor total: {knapsackPD(pesos, valores, capacidade_max)}")