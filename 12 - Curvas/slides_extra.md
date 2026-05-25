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
