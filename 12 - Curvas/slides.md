:::center
# Computação Visual
## 12 - Modelagem geométrica: Curvas
:::
---
# Modelagem geométrica
- É a disciplina que estuda como construir modelos geométricos para diversos propósitos
- Entre os modelos mais comuns estão curvas e superfícies
- Há vários paradigmas para modelagem geométrica:
  - Curvas e superfícies paramétricas 
  - Curvas e superfícies implícitas
  - Modelos lineares por parte (polígonos, malhas)
  - Enumeração
    - Nuvens de pontos / surflets
    - Pixels e voxels
---
# Curvas
- O modelo mais comum são as curvas paramétricas
- Comumente, a curva é definida por uma lista de pontos e um conjunto de _funções de mistura_ (_blending functions_):
$$ 
\mathbf{C}(t) = \sum_{i=0}^{n} \mathbf{P}_i N_i(t), \quad t \in [a,b], $$
onde $\mathbf{P}_i$ são os _pontos de controle_ e $N_i(t)$ as _funções de mistura_.
---
# Curvas de Bézier
- São as mais utilizadas na computação gráfica
- Elas foram desenvolvidas por Pierre Bézier na década de 1960 e Paul de Casteljau na mesma época
- As funções de mistura das curvas de Bézier são os polinômios de Bernstein:
$$ 
B_i^n(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad t \in [0,1], 
$$
- A curva é definida por 
$$ 
\mathbf{C}(t) = \sum_{i=0}^{n} \mathbf{P}_i B_i^n(t), \quad t \in [0,1], $$
---
# Polinômios de Bernstein
::img src=bernstein.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbernstein_polynomials.zip)
---
# Propriedades das curvas de Bézier
- A curva passa por $\mathbf{P}_0$ quando $t=0$ e por $\mathbf{P}_{n-1}$ quando $t=1$.
- A curva está contida no fecho convexo dos pontos de controle
- A direção tangente no ponto inicial é dada por $\mathbf{P}_1 - \mathbf{P}_0$ e no ponto final por $\mathbf{P}_{n-1} - \mathbf{P}_{n-2}$.
