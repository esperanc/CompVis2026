---
# Splines de Catmull-Rom
:::col width=60%
- Motivação: queremos uma curva suave que **interpole** os pontos de controle
  - B-splines aproximam, mas não interpolam
- As splines de Catmull-Rom são splines cúbicas interpolantes desenvolvidas por Edwin Catmull e Raphael Rom (1974)
- São um caso especial das **splines de Hermite cúbicas** com tangentes estimadas automaticamente a partir dos vizinhos:
$$
\mathbf{T}_i = \frac{\mathbf{P}_{i+1} - \mathbf{P}_{i-1}}{2}
$$
- Suporte local: cada segmento depende de apenas 4 pontos consecutivos
- Continuidade $C^1$
:::
:::col width=40%
::img src=catmull_rom.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcatmull_rom.py)
:::
---
# Forma matricial das Splines de Catmull-Rom
- O trecho entre $\mathbf{P}_i$ e $\mathbf{P}_{i+1}$, dados os vizinhos $\mathbf{P}_{i-1}$ e $\mathbf{P}_{i+2}$, é:
$$
\mathbf{C}(t) = \mathbf{B}(t)\, \mathbf{M}_{CR}\, [\mathbf{P}_{i-1},\; \mathbf{P}_i,\; \mathbf{P}_{i+1},\; \mathbf{P}_{i+2}]^T, \quad t \in [0,1]
$$
onde $\mathbf{B}(t) = [t^3, t^2, t, 1]$ e
$$
\mathbf{M}_{CR} = \frac{1}{2}
\begin{bmatrix}
-1 &  3 & -3 &  1 \\
 2 & -5 &  4 & -1 \\
-1 &  0 &  1 &  0 \\
 0 &  2 &  0 &  0
\end{bmatrix}
$$
- $t=0$ corresponde a $\mathbf{P}_i$ e $t=1$ a $\mathbf{P}_{i+1}$
- **Nos extremos** (sem $\mathbf{P}_{-1}$ ou $\mathbf{P}_{n+1}$): a solução mais simples é repetir o primeiro e o último ponto como pontos fantasmas
---
# Variante centripetal e comparações
:::col width=60%
- A variante **uniforme** (apresentada acima) pode gerar torções e auto-interseções quando os pontos estão muito irregularmente espaçados
- A variante **centripetal** usa como comprimento de cada intervalo $\Delta t_i = \|\mathbf{P}_{i+1} - \mathbf{P}_i\|^{1/2}$
  - Evita torções e auto-interseções
  - Resultado visual geralmente mais natural
- A variante **cordal** usa $\Delta t_i = \|\mathbf{P}_{i+1} - \mathbf{P}_i\|$
  - Mais fácil de calcular, mas pode produzir arcos indesejados
- Comparação com B-splines:
  - Catmull-Rom **interpola** os pontos (B-spline apenas aproxima)
  - Catmull-Rom tem $C^1$ (B-spline cúbica tem $C^2$)
  - Catmull-Rom é mais simples de usar para trajetórias e animação
:::
:::col width=40%
::img src=catmull_rom.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcatmull_rom.py)
:::
---
# Curvas de Subdivisão
- Ideia: dado um polígono inicial, aplica-se repetidamente uma **regra de refinamento** local que duplica os vértices e suaviza as posições
- A sequência de polígonos converge para uma curva suave
- Vantagens sobre a formulação explícita de splines:
  - Implementação extremamente simples (apenas operações de média)
  - Estrutura hierárquica natural (multirresolução)
  - Fácil de generalizar para **superfícies** (malhas de subdivisão como Catmull-Clark e Loop)
  - Custo computacional cresce linearmente com o número de pontos
- O tipo de curva limite depende da **regra de subdivisão** escolhida
---
# Algoritmo de Chaikin
:::col width=60%
- Proposto por George Chaikin (1974) como **corte de cantos** (_corner cutting_)
- A cada iteração, cada aresta $(\mathbf{P}_i, \mathbf{P}_{i+1})$ gera dois novos pontos a $\tfrac{1}{4}$ e $\tfrac{3}{4}$ da aresta:
$$
\mathbf{Q}_i = \tfrac{3}{4}\mathbf{P}_i + \tfrac{1}{4}\mathbf{P}_{i+1}, \qquad
\mathbf{R}_i = \tfrac{1}{4}\mathbf{P}_i + \tfrac{3}{4}\mathbf{P}_{i+1}
$$
- Os vértices originais são descartados
- Aplicado repetidamente, o polígono converge para uma **B-spline quadrática uniforme**
  - Continuidade $C^1$
  - A curva está dentro do fecho convexo do polígono de controle
- Funciona igualmente para polígonos abertos e fechados
:::
:::col width=40%
::img src=chaikin.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fchaikin_subdivision.py)
:::
---
# Generalização: Lane-Riesenfeld
:::col width=60%
- Lane e Riesenfeld (1980) generalizaram o algoritmo de Chaikin para produzir B-splines de **grau $d$ arbitrário**
- Cada iteração tem dois passos:
  1. **Refinamento**: inserir o ponto médio entre cada par consecutivo (dobra o número de pontos)
  $$\mathbf{P}^{\text{novo}}_{2i} = \mathbf{P}_i, \quad \mathbf{P}^{\text{novo}}_{2i+1} = \tfrac{1}{2}(\mathbf{P}_i + \mathbf{P}_{i+1})$$
  2. **Suavização**: aplicar $d-1$ rodadas consecutivas de médias de pares adjacentes:
  $$\mathbf{P}_i \leftarrow \tfrac{1}{2}(\mathbf{P}_i + \mathbf{P}_{i+1})$$

| Grau $d$ | Curva limite | Continuidade |
|---|---|---|
| 2 | Quadrática (= Chaikin) | $C^1$ |
| 3 | Cúbica | $C^2$ |
| 4 | Quártica | $C^3$ |
:::
:::col width=40%
::img src=lane_riesenfeld.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fchaikin_subdivision.py)
:::
---
# Curvas Implícitas
- Uma curva implícita é o **conjunto de zeros** de uma função escalar $f: \mathbb{R}^2 \to \mathbb{R}$:
$$
\mathcal{C} = \{\, (x,y) \in \mathbb{R}^2 \mid f(x,y) = 0 \,\}
$$
- Exemplos clássicos:
  - Círculo: $f(x,y) = x^2 + y^2 - r^2$
  - Elipse: $f(x,y) = x^2/a^2 + y^2/b^2 - 1$
  - Folha de Descartes: $f(x,y) = x^3 + y^3 - 3axy$
- **Vantagens** sobre curvas paramétricas:
  - Representação natural de topologias complexas (ilhas, buracos, auto-interseções)
  - Teste de pertencimento trivial: $f(x,y) < 0$ (interior), $f(x,y) > 0$ (exterior)
  - Operações booleanas via $\min/\max$: união $\min(f,g)=0$, interseção $\max(f,g)=0$
- **Desafio**: renderização requer algoritmos específicos (não há parametrização explícita)
---
# Renderização: Quadrados Marchantes
:::col width=60%
- O algoritmo de _Marching Squares_ extrai a isocurva $f=0$ de uma grade regular:
  1. Avaliar $f$ em todos os vértices da grade
  2. Para cada célula quadrada, identificar quais arestas são cruzadas pela isocurva — detectado por **mudança de sinal** de $f$ nos extremos da aresta
  3. Estimar o ponto de cruzamento por **interpolação linear**:
  $$t = \frac{f(A)}{f(A)-f(B)}, \quad \mathbf{X} = \mathbf{A} + t(\mathbf{B}-\mathbf{A})$$
  4. Conectar os pontos de cruzamento dentro de cada célula
- Há $2^4 = 16$ configurações de sinal por célula (reduzidas a 4 por simetria)
- Ambiguidades nas configurações de "sela" podem gerar inconsistências topológicas
:::
:::col width=40%
::img src=marching_squares.png height=80%
:::
---
# Funções de Base Radial (RBF)
:::col width=60%
- Uma Função de Base Radial (RBF) define $f$ como combinação de funções de distância:
$$
f(\mathbf{x}) = \sum_{i=1}^{n} \lambda_i\; \varphi(\|\mathbf{x} - \mathbf{c}_i\|)
$$
onde $\mathbf{c}_i$ são os **centros**, $\lambda_i$ os pesos e $\varphi: \mathbb{R}_{\ge 0}\to\mathbb{R}$ a função radial
- Funções $\varphi$ comuns:

| Nome | $\varphi(r)$ |
|---|---|
| Biharmonica | $r$ |
| Placa fina | $r^2 \ln r$ |
| Multiquádrica | $\sqrt{r^2+\varepsilon^2}$ |
| Gaussiana | $e^{-\varepsilon^2 r^2}$ |

- A função $f$ é globalmente suave e pode representar curvas de topologia arbitrária
:::
:::col width=40%
::img src=rbf_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Frbf_implicit.zip)
:::
---
# Construção de Curvas Implícitas via RBF
:::col width=60%
- Para construir uma curva que passe por pontos dados $\{\mathbf{q}_j\}$:
  1. **Pontos sobre a curva**: impor $f(\mathbf{q}_j) = 0$
  2. **Pontos fora da curva**: deslocar $\mathbf{q}_j$ ao longo da normal estimada $\hat{\mathbf{n}}_j$ por um offset $\varepsilon$:
$$f(\mathbf{q}_j + \varepsilon\hat{\mathbf{n}}_j) = +1, \quad f(\mathbf{q}_j - \varepsilon\hat{\mathbf{n}}_j) = -1$$
  3. **Resolver o sistema linear** $\mathbf{\Phi}\,\boldsymbol{\lambda} = \mathbf{d}$, onde $\Phi_{ij} = \varphi(\|\mathbf{c}_i - \mathbf{c}_j\|)$
  4. **Renderizar** avaliando $f$ em uma grade e extraindo a isocurva $f=0$ via _marching squares_
- A normal estimada no ponto $\mathbf{q}_i$ pode ser obtida como a perpendicular ao segmento $\mathbf{q}_{i-1}\mathbf{q}_{i+1}$
- A regularização $\mathbf{\Phi} + \mu \mathbf{I}$ melhora a estabilidade numérica
:::
:::col width=40%
::img src=rbf_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Frbf_implicit.zip)
:::
