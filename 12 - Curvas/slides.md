:::center
# Computação Visual
## 12 - Modelagem geométrica: Curvas
:::
---
# Modelagem geométrica
- É a disciplina que estuda como construir modelos geométricos para diversos propósitos
    - Tipicamente, curvas e superfícies
- Há vários paradigmas para modelagem geométrica:
  - Curvas e superfícies paramétricas 
  - Curvas e superfícies implícitas
  - Modelos lineares por parte (polígonos, malhas)
  - Enumeração
    - Nuvens de pontos / surflets
    - Pixels e voxels
---
# Curvas paramétricas
- Comumente, a curva é definida por uma lista de pontos e um conjunto de _funções de mistura_ (_blending functions_):
$$ 
\mathbf{C}(t) = \sum_{i=0}^{n} \mathbf{P}_i N_i(t), \quad t \in [a,b], $$
onde $\mathbf{P}_i$ são os _pontos de controle_ e $N_i(t)$ as _funções de mistura_.
- Para desenhar, aproxima-se a curva por amostragem
  - Divide-se o intervalo $[a,b]$ em $m$ subintervalos de comprimento $\Delta t = (b-a)/m$
  - Calcula-se $m+1$ pontos $\mathbf{C}(t_j), j=0,\ldots,n$ 
  - Conecta-se os pontos consecutivos
---
# Suavidade e continuidade
::: col width=60%
- Normalmente, estamos interessados em curvas _suaves_
- A maneira mais simples de garantir suavidade é através da continuidade _algébrica_ das funções de mistura
  - Continuidade $C^i$ significa que as $i$ primeiras derivadas em relação ao parâmetro $t$ são contínuas
    - $C^0$ - contínua (sem quebras)
    - $C^1$ - derivada primeira contínua (tangentes)
    - $C^2$ - derivada segunda contínua (curvatura)
    - etc
:::
::: col width=40%
::img src=continuity.svg height=80%
:::
---
# Interpolação vs Aproximação
:::col 
- É natural querermos modelar uma curva suave que passa por um conjunto de pontos dados
- Se a curva desejada é polinomial, chamamos tal
curva de interpolação polinomial _lagrangeana_
- Entretanto, o resultado nem sempre é o esperado (oscilações)
- É mais comum querermos curvas que “passem perto” dos pontos dados, isto é, _aproximações_
:::
:::col
:: img src=lagrange_curve.png
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Flagrange_curve.py)
:::
---
# Curvas de Bézier
- São as mais utilizadas na computação gráfica
- Desenvolvidas independentemente por Pierre Bézier e Paul de Casteljau nos anos 60
- As funções de mistura das curvas de Bézier são os polinômios de Bernstein:
$$ 
\mathbf{C}(t) = \sum_{i=0}^{n} \mathbf{P}_i B_i^n(t),\\
~\\
\textrm{onde } B_i^n(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad t \in [0,1]

$$

---
# Polinômios de Bernstein
::img src=bernstein.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbernstein_polynomials.zip)
---
# Propriedades das curvas de Bézier
::: col width=60%
- O grau da curva (do polinômio) é dado pelo número de pontos do polígono de controle menos 1
- A curva passa por $\mathbf{P}_0$ quando $t=0$ e por $\mathbf{P}_{n-1}$ quando $t=1$.
- A curva está contida no fecho convexo dos pontos de controle
    - Os polinômios de Bernstein somam 1 para qualquer $t$
:::
::: col width=40%
:: image src=bezier_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbezier_curve.py)
:::
---
# Propriedades das curvas de Bézier (II)
::: col width=60%
- Uma reta não intersecta a curva em mais pontos do que intersecta o polígono de controle
- A direção tangente no ponto inicial é dada por $\mathbf{P}_1 - \mathbf{P}_0$ e no ponto final por $\mathbf{P}_{n-1} - \mathbf{P}_{n-2}$.
    - Para cúbicas, as derivadas são $3(\mathbf{P}_{1}-\mathbf{P}_{0})$ e $3(\mathbf{P}_{2}-\mathbf{P}_{3})$
- Transformar os pontos de controle (transf. afim) e desenhar a curva é equivalente a desenhar a curva transformada
- Continuidade $C^\infty$
:::
::: col width=40%
:: image src=bezier_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbezier_curve.py)
:::
---
# Forma matricial
- Podemos escrever a equação para uma curva
de Bézier cúbica na forma $C(t) = B(t) \mathbf{M}_b \mathbf{P}$, 
onde 
  - $B(t) = [t^3, t^2, t, 1]$  
  - $\mathbf{P} = [P_0, P_1, P_2, P_3]^T$
  - $\mathbf{M}_b = \begin{bmatrix}    -1 & 3 & -3 & 1\\     3 & -6 & 3 & 0\\     -3 & 3 & 0 & 0\\     1 & 0 & 0 & 0  \end{bmatrix}$

---
# O algoritmo de de Casteljau
::: col width=60%
- Para graus altos, os polinômios de Bernstein podem introduzir erros numéricos consideráveis.
- O método de de Casteljau calcula pontos na curva usando interpolação linear repetida
$$
\mathbf{b}_{i}^{k}(t) = (1-t)\mathbf{b}_{i}^{k-1}(t) + t \mathbf{b}_{i+1}^{k-1}(t) 
$$
para $k=1..n$ e $i=0..n-k$, sendo $\mathbf{b}_{i}^{0}=\mathbf{P}_i$
:::
::: col width=40%
:: image src=casteljau-curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fde_casteljau_algorithm.zip)
:::
---
# Reparametrização de curvas de Bézier
:::col
- O algoritmo de de Casteljau oferece um meio de reparametrizar
 a curva
- Ao avaliar a curva no parâmetro $t$, dois polígonos de controle equivalentes são calculados:

  $\mathbf{b}_0^0, \mathbf{b}_0^1 \cdots \mathbf{b}_0^n$ e 

  $\mathbf{b}_0^n, \mathbf{b}_1^{n-1} \cdots \mathbf{b}_n^0$ 
:::
:::col
:: img src=reparametrization.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fde_casteljau_algorithm.zip)
:::
---
# Desenho adaptativo
- Ao invés de amostrar uniformemente, podemos usar recursão para desenhar a curva
  - Se o polígono de controle é suficientemente plano,
    - desenhamos o polígono
  - senão
    - Usamos de Casteljau para avaliar a curva em $t=0.5$, gerando dois polígonos de controle equivalentes, mas cobrindo um trecho menor da curva
    - Chamamos a função recursivamente para ambos os polígonos

[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fde_casteljau_algorithm.zip)
---
# Curvas longas
- Curvas Bézier com $k$ pontos de controle são de grau $k – 1$
- Curvas de grau alto são difíceis de desenhar
  - Complexas
  - Sujeitas a erros de precisão
- Normalmente, queremos que pontos de controle
tenham efeito local
  - Em curvas Bézier, todos os pontos de controle têm efeito global
- **Solução**:
    - Emendar curvas polinomiais de grau baixo
    - Relaxar condições de continuidade
---
# Emendando curvas Bézier
:::col
- Continuidade $C^0$: Último ponto da primeira = primeiro ponto da segunda
- Continuidade $C^1$: $C^0$ e último segmento da curva $i$ com mesma direção e comprimento que primeiro segmento da curva $i+1$ 
- Continuidade $C^2$: $C^1$ e restrições adicionais entre o ante-penúltimo ponto da curva $i$ e o terceiro ponto da curva $i+1$
- Etc.
:::
:::col
::img src=cubic_bezier_splines.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcubic_bezier_splines.zip)
:::
---
# Splines
- A base de Bézier não é própria para a modelagem de curvas longas
  - Bézier única: suporte não local
  - Trechos emendados: restrições não são naturais
- Base alternativa: _B-Splines_
  - Nome vem de um instrumento usado por desenhistas
  - Modelagem por polígonos de controle sem restrições adicionais
  - Suporte local
  - Alteração de um vértice afeta curva apenas na vizinhança
  - Existem muitos tipos de Splines, mas vamos nos concentrar em _B-splines uniformes_
    - Uma B-spline uniforme de grau $d$ tem continuidade $C^{d-1}$
---
# Base B-Spline
:::col
- Funções de base são não nulas apenas em um intervalo no espaço do parâmetro
  - Como é impossível obter isso com apenas 1 polinomial, cada função de base é composta da emenda de funções polinomiais
  - Por exemplo, uma função de base de uma B-spline quadrática tem 3 trechos (não nulos) emendados com continuidade $C^1$
:::
:::col
::img src=quadratic_bspline.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcox_de_boor.zip)
:::
---
# Funções de base de uma B-Spline
:::col
- Todas as funções de base têm a mesma forma, mas são deslocadas entre si em intervalos no espaço de parâmetros 
  - Num determinado intervalo, apenas um pequeno número de funções de base são não-nulas
- Numa B-spline quadrática, cada intervalo é influenciado por 3 funções de base
:::
:::col
::img src=quadratic_bspline_overlap.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcox_de_boor.zip)
:::
---
# Nós de uma B-Spline
:::col
- O conjunto de nós define os limites dos trechos de cada função de base
- Os nós são dados por $t_0, t_1, ..., t_{n+d+1}$
  - $n$ é o número de funções
  - $d$ é o grau
- Onde $n$ é o número de pontos de controle e $d$ é o grau da curva
- Para B-splines uniformes, os nós são dados por $t_i = i$
:::
:::col
::img src=local_bspline.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcox_de_boor.zip)
:::
---
# Recorrência Cox-de Boor
$$
B^d_i(t) = \frac{t-t_i}{t_{i+d}-t_i}B^{d-1}_i(t) + \frac{t_{i+d+1}-t}{t_{i+d+1}-t_{i+1}}B^{d-1}_{i+1}(t) \\
~\\
 \textrm{sendo que } B^0_i(t) = \begin{cases} 1 & \text{se } t_i \le t < t_{i+1} \\ 0 & \text{senão} \end{cases} $$
onde $t_i$ é o nó correspondente ao ponto de controle $P_i$ e $d$ é o grau da curva.
---
# Avaliando as funções de base
:::col
- É preciso cuidado com denominadores iguais a zero
  - Isso ocorre quando os nós são repetidos
    - Usado para impor restrições de continuidade
  - A convenção nesses casos é considerar o termo como zero
- Cuidado também com o último intervalo!
- A recorrência de Cox-de Boor pode ser avaliada iterativamente
:::
:::col
::img src=bspline_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbspline_curve.zip)
:::
---
# Usando nós para interpolar pontos de controle
:::col
- É possível forçar a interpolação dos pontos de controle à custa de repetir os nós
  - Por exemplo, para interpolar os pontos $P_0$ e $P_3$ de uma B-spline cúbica com 4 pontos de controle, repetimos os nós nos extremos, $[0,0,0,0,1,1,1,1]$
  - Neste caso, temos uma Bézier cúbica como resultado!
- Alternativamente, pode-se simplesmente repetir os pontos de controle
:::
:::col
::img src=bspline_interpolating.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbspline_curve.zip)
:::
---
# Curvas fechadas
:::col
- Para obter uma curva fechada, basta repetir os nós iniciais no final ou os nós finais no início
  - Por exemplo, para uma B-spline cúbica com 4 pontos de controle, podemos usar $[P_0, P_1, P_2, P_3, P_0, P_1]$
:::
:::col
::img src=bspline_closed.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbspline_curve.zip)
:::
---
# NURBS
:::col
- É impossível representar círculos e quádricas em geral com B-splines
- A solução é usar NURBS (Non-Uniform Rational B-Splines)
  - Usa-se o espaço projetivo, onde a coordenada $w$ serve para "esticar" a curva
  - Coordenadas são multiplicadas por $w$ antes de aplicar o Cox-de Boor
  - O ponto $\mathbf{P}_i$ vira $\mathbf{P}_i = (w_i x_i, w_i y_i, w_i)$
  - Após calcular o ponto na NURBS, divide-se por $w$ para voltar ao espaço euclidiano
:::
:::

