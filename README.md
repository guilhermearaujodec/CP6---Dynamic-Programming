# 🎒 Problema da Mochila 0/1 — Relatório Técnico

## 👥 Integrantes do Grupo
| Nome Completo | RM |
|----------------|----|
| Guilherme Araujo de Carvalho | 558926 |
| Augusto Douglas Nogueira de Mendonça | 558371 |
| Gabriel Vasquez Queiroz da Silva | 557056 |
| Gustavo Oliveira Ribeiro | 559163 |


---

## 🧭 Introdução e Contextualização do Problema

O **Problema da Mochila 0/1** é um dos clássicos desafios de **otimização combinatória**. Ele busca determinar o conjunto ótimo de itens que deve ser incluído em uma mochila com capacidade limitada, de modo a **maximizar o valor total transportado**, respeitando a **restrição de peso**.

Em termos gerais, o problema é definido assim:

* Temos uma **mochila** com capacidade máxima `W`.
* Temos uma lista de **n itens**, cada um com:

  * **peso** `pᵢ`
  * **valor** `vᵢ`
* Para cada item, podemos escolher:

  * `1` → incluir o item completamente
  * `0` → não incluir o item
* **Não é permitido** incluir frações de itens nem itens repetidos.

### 🎯 Objetivo

Maximizar a soma dos valores dos itens incluídos, garantindo que o peso total não exceda `W`.

### 📊 Conjunto de Dados de Exemplo

| Item | Peso (pᵢ) | Valor (vᵢ) |
| ---- | --------- | ---------- |
| A    | 2         | 10         |
| B    | 3         | 12         |
| C    | 4         | 20         |
| D    | 1         | 3          |

**Capacidade Máxima da Mochila (W):** 6 kg

### 💡 Solução Ótima Manual

| Itens Selecionados | Peso Total | Valor Total | Viável? | Observação         |
| ------------------ | ---------- | ----------- | ------- | ------------------ |
| B + D              | 4          | 15          | ✅       | Viável             |
| A + B + D          | 6          | 25          | ✅       | Boa, mas não ótima |
| A + C              | 6          | **30**      | ✅       | 🏆 Solução ótima   |
| B + C              | 7          | 32          | ❌       | Excede o peso      |

---

## 🧩 O Problema da Mochila

### Contextualização

O problema é um exemplo clássico de **decisão binária** em otimização: incluir ou não cada item. Ele é amplamente utilizado em áreas como:

* Planejamento de recursos
* Logística
* Seleção de investimentos
* Engenharia e economia

### Natureza do Problema

Esse é um **Problema de Otimização NP-Completo**, o que significa que:

* Não há solução exata eficiente para todos os casos em tempo polinomial.
* Exige **estratégias inteligentes** como **Programação Dinâmica** ou **Heurísticas** para encontrar boas soluções.

---

## 🧮 Definição de Programação Dinâmica (PD)

A **Programação Dinâmica** é uma técnica de otimização baseada na **divisão de um problema complexo em subproblemas menores**, resolvendo cada um uma única vez e armazenando os resultados intermediários.

### 🧠 Pilares Fundamentais

#### 1. Subestrutura Ótima

A solução ótima de um problema depende das soluções ótimas de seus subproblemas.
Exemplo: o melhor valor para uma mochila de capacidade `W` pode ser construído a partir das soluções ótimas das mochilas de capacidades menores (`W - pᵢ`).

#### 2. Subproblemas Sobrepostos

Durante a execução recursiva, os mesmos subproblemas são recalculados várias vezes.
A **memoização** e o **método bottom-up** evitam esse retrabalho armazenando os resultados já computados.

---

## 🔍 Análise Detalhada das Abordagens

### 🧭 Função 1: Estratégia Gulosa (Iterativa)

#### Conceito

A estratégia gulosa escolhe os itens com base na **melhor razão valor/peso**, tentando preencher a mochila da maneira mais vantajosa no momento.

#### Análise Crítica

Embora seja rápida e intuitiva, **não garante a solução ótima** no caso 0/1, pois um item mais leve e valioso pode combinar melhor com outro, superando o resultado localmente ótimo.

#### Demonstração

Usando os dados do problema:

* Razão (v/p): A=5.0, B=4.0, C=5.0, D=3.0
  A escolha gulosa pegaria **A (2kg)** e **C (4kg)** → resultado ótimo neste caso.
  Porém, em outros cenários, pode falhar.

#### Complexidade

* **Tempo:** O(n log n) (ordenamento)
* **Espaço:** O(1)

---

### 🔁 Função 2: Recursiva Pura (Sem Memoização)

#### Conceito

Explora todas as combinações possíveis de itens, decidindo recursivamente se cada item é incluído ou não.

#### Análise de Desempenho

A árvore de recursão se ramifica para cada item em duas possibilidades (`incluir` ou `excluir`), resultando em **2ⁿ chamadas recursivas**.

Exemplo:
Para 4 itens → 2⁴ = 16 combinações possíveis.

#### Complexidade

* **Tempo:** O(2ⁿ)
* **Melhor caso (Ω):** O(1)
* **Espaço:** O(n)

---

### 🧠 Função 3: Recursiva com Memoização (Top Down)

#### Conceito

A memoização armazena os resultados dos subproblemas já resolvidos (usando um dicionário ou matriz), evitando recomputações desnecessárias.

#### Ligação com PD

A memoização é considerada **Programação Dinâmica Top-Down**, pois resolve o problema de forma recursiva e armazena soluções parciais.

#### Melhoria na Eficiência

Elimina o reprocessamento dos subproblemas, reduzindo a complexidade de **exponencial** para **polinomial**.

#### Complexidade

* **Tempo:** O(n * W)
* **Melhor caso (Ω):** O(W)
* **Espaço:** O(n * W)

---

### 🧱 Função 4: Programação Dinâmica (Bottom Up)

#### Conceito

Constrói uma **tabela (matriz dp)** de forma iterativa, onde cada célula `dp[i][w]` representa o valor máximo obtido com os `i` primeiros itens e capacidade `w`.

#### Fluxo do Algoritmo

1. Inicializa-se uma matriz de zeros com dimensões `(n+1) x (W+1)`.
2. Para cada item, atualiza-se o valor ótimo para cada capacidade possível.
3. O resultado final está em `dp[n][W]`.

#### Vantagem sobre Memoização

Evita chamadas recursivas e é geralmente **mais rápida e estável** na prática.

#### Complexidade

* **Tempo:** O(n * W)
* **Espaço:** O(n * W)

---

## 📋 Conclusão

### 🔢 Tabela Comparativa de Complexidades

| Método                    | Tipo de Abordagem      | Tempo (O)  | Espaço (O) | Observações                   |
| ------------------------- | ---------------------- | ---------- | ---------- | ----------------------------- |
| Estratégia Gulosa         | Iterativa / Heurística | O(n log n) | O(1)       | Rápida, mas não garante ótimo |
| Recursiva Pura            | Recursiva              | O(2ⁿ)      | O(n)       | Muito lenta                   |
| Recursiva com Memoização  | Top Down (PD)          | O(n·W)     | O(n·W)     | Boa eficiência                |
| Programação Dinâmica (PD) | Bottom Up              | O(n·W)     | O(n·W)     | Melhor desempenho geral       |

---

### 🧩 Escolha Ótima

A abordagem de **Programação Dinâmica (Bottom-Up)** é a mais eficiente e robusta para resolver o **Problema da Mochila 0/1**, equilibrando clareza, desempenho e estabilidade.

---

### 💭 Reflexão

O Problema da Mochila exemplifica a força da **Programação Dinâmica** para lidar com problemas complexos onde:

* Há **subestrutura ótima**; e
* Existem **subproblemas sobrepostos**.

Essas técnicas são amplamente aplicáveis em contextos reais, desde logística e finanças até bioinformática e aprendizado de máquina.
