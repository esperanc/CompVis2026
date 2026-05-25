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
- Normalmente, queremos que pontos de controle tenham efeito local
  - Em curvas Bézier, todos os pontos de controle têm efeito global
- **Solução**:
    - Emendar curvas polinomiais de grau baixo
    - Relaxar condições de continuidade
---
# Curvas de Hermite Cúbicas
:::col
- Uma curva de Hermite cúbica é definida por **duas condições de contorno em cada extremo** do segmento:
  - As posições $\mathbf{P}_0$ e $\mathbf{P}_1$ (pontos de interpolação)
  - As tangentes $\mathbf{T}_0$ e $\mathbf{T}_1$ (vetores de velocidade)
- A curva é o único polinômio cúbico que satisfaz simultaneamente essas quatro condições
:::
:::col
- Motivação: queremos controlar **onde** a curva passa e **como** ela chega e sai de cada ponto
- Aplicações típicas:
  - Animação (trajetórias com velocidade prescrita)
  - Fontes tipográficas (TrueType usa variante quadrática)
  - Conexão suave entre segmentos
:::
---
# Funções de base de Hermite
- Impondo $\mathbf{C}(0)=\mathbf{P}_0$, $\mathbf{C}(1)=\mathbf{P}_1$, $\mathbf{C}'(0)=\mathbf{T}_0$, $\mathbf{C}'(1)=\mathbf{T}_1$, obtemos as quatro **funções de base de Hermite**:
$$
\mathbf{C}(t) = h_{00}(t)\,\mathbf{P}_0 + h_{10}(t)\,\mathbf{T}_0 + h_{01}(t)\,\mathbf{P}_1 + h_{11}(t)\,\mathbf{T}_1\\
~\\
\begin{array}{ll}
h_{00}(t) =  2t^3 - 3t^2 + 1 &
h_{10}(t) =   t^3 - 2t^2 + t \\
h_{01}(t) = -2t^3 + 3t^2     &
h_{11}(t) =   t^3 -  t^2
\end{array}
$$
- $h_{00}$ e $h_{01}$ são as funções de posição : valem 1 em um extremo e 0 no outro
- $h_{10}$ e $h_{11}$ são as funções de tangente: valem 0 em ambos os extremos, mas têm derivada 1 em um deles e 0 no outro
---
# Funções de base de Hermite (gráfico)
::img src=hermite_polynomials.png height=70%
- Note que $h_{00}(t) + h_{01}(t) = 1$ para todo $t$ (partição da unidade para as posições)
- As quatro funções têm suporte global em $[0,1]$, mas com papéis claramente separados
---
# Forma matricial
- A curva de Hermite pode ser escrita compactamente como $\mathbf{C}(t) = \mathbf{B}(t)\,\mathbf{M}_H\,\mathbf{G}_H$, onde
  - $\mathbf{B}(t) = [t^3,\; t^2,\; t,\; 1]$
  - $\mathbf{G}_H = [\mathbf{P}_0,\; \mathbf{P}_1,\; \mathbf{T}_0,\; \mathbf{T}_1]^T$ é o vetor de geometria
  - $\mathbf{M}_H$ é a **matriz de Hermite**:

$$
\mathbf{M}_H =
\begin{bmatrix}
 2 & -2 &  1 &  1 \\
-3 &  3 & -2 & -1 \\
 0 &  0 &  1 &  0 \\
 1 &  0 &  0 &  0
\end{bmatrix}
$$

- A matriz $\mathbf{M}_H$ é invertível: dado qualquer polinômio cúbico, é possível encontrar os parâmetros de Hermite equivalentes
- A mesma estrutura se aplica a dimensões maiores: basta aplicar a fórmula coordenada a coordenada
---
# Relação com Bézier
- As curvas de Bézier cúbicas e as de Hermite são **representações diferentes do mesmo espaço** de polinômios cúbicos
- A conversão entre as duas é dada por uma simples mudança de base:
$\mathbf{G}_B = \mathbf{M}_B^{-1}\mathbf{M}_H\,\mathbf{G}_H$
- Em termos explícitos, os pontos de Bézier equivalentes são:
$$
\mathbf{Q}_0 = \mathbf{P}_0, \quad
\mathbf{Q}_1 = \mathbf{P}_0 + \tfrac{1}{3}\mathbf{T}_0, \quad
\mathbf{Q}_2 = \mathbf{P}_1 - \tfrac{1}{3}\mathbf{T}_1, \quad
\mathbf{Q}_3 = \mathbf{P}_1
$$
- Interpretação geométrica:
  - Os pontos de controle internos de Bézier ficam a $\tfrac{1}{3}$ da tangente a partir de cada extremo
  - Escalar a tangente $\mathbf{T}_0$ por um fator $\alpha$ equivale a mover $\mathbf{Q}_1$ ao longo dessa direção
---
# Emendando segmentos de Hermite
:::col width=60%
- Para construir uma curva longa, emendamos segmentos sucessivos $[\mathbf{P}_i, \mathbf{P}_{i+1}]$
- Continuidade nas junções:
  - $C^0$: basta fazer $\mathbf{P}_{i+1}$ do segmento $i$ igual a $\mathbf{P}_0$ do segmento $i+1$ (automático se os pontos são compartilhados)
  - $C^1$: impor $\mathbf{T}_1^{(i)} = \mathbf{T}_0^{(i+1)}$ — a tangente de saída do segmento $i$ deve ser igual à tangente de entrada do segmento $i+1$
:::
:::col width=40%
::img src=hermite_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fhermite_curve.zip)
:::
---
# Emendando curvas Bézier
:::col width=60%
- Suavidade requer condições geométricas nas fronteiras entre curvas, ex.:
  - Continuidade $C^0$: Último ponto da primeira = primeiro ponto da segunda
  - Continuidade $C^1$: $C^0$ e último segmento da curva $i$ com mesma direção e comprimento que primeiro segmento da curva $i+1$ 
  - Continuidade $C^2$: $C^1$ e restrições adicionais entre o ante-penúltimo ponto da curva $i$ e o terceiro ponto da curva $i+1$
- Na prática, se usa cúbicas com continuidade $C^1$
:::
:::col width=40%
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
:::col width=60%
- É preciso cuidado com denominadores iguais a zero
  - Isso ocorre quando os nós são repetidos
    - Usado para impor restrições de continuidade
  - A convenção nesses casos é considerar o termo como zero
- Cuidado também com o último intervalo!
- A recorrência de Cox-de Boor pode ser avaliada iterativamente
:::
:::col width=40%
::img src=bspline_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbspline_curve.zip)
:::
---
# Interpolação de pontos de controle
:::col width=60%
- É possível forçar a interpolação dos pontos de controle à custa de repetir os nós
  - Por exemplo, para interpolar os pontos $P_0$ e $P_3$ de uma B-spline cúbica com 4 pontos de controle, repetimos os nós nos extremos, $[0,0,0,0,1,1,1,1]$
  - Neste caso, temos uma Bézier cúbica como resultado!
- Alternativamente, pode-se simplesmente repetir os pontos de controle
:::
:::col width=40%
::img src=bspline_interpolating.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbspline_curve.zip)
:::
---
# Curvas fechadas
:::col width=60%
- Para obter uma curva fechada, basta repetir os nós iniciais no final ou os nós finais no início
  - Por exemplo, para uma B-spline cúbica com 4 pontos de controle, podemos usar $[P_0, P_1, P_2, P_3, P_0, P_1]$
:::
:::col width=40%
::img src=bspline_closed.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fbspline_curve.zip)
:::
---
# NURBS
:::col width=60%
- É impossível representar círculos e quádricas em geral com B-splines
- A solução é usar NURBS (Non-Uniform Rational B-Splines)
  - Usa-se o espaço projetivo, onde a coordenada $w$ serve para "esticar" a curva
  - Coordenadas são multiplicadas por $w$ antes de aplicar o Cox-de Boor
  - O ponto $\mathbf{P}_i$ vira $\mathbf{P}_i = (w_i x_i, w_i y_i, w_i)$
  - Após calcular o ponto na NURBS, divide-se por $w$ para voltar ao espaço euclidiano
:::
:::col width=40%
::img src=nurbs_curve.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fnurbs_curve.zip)
:::
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
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcatmull_rom_curve.py)
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
- **Nós extremos** (sem $\mathbf{P}_{-1}$ ou $\mathbf{P}_{n+1}$): a solução mais simples é repetir o primeiro e o último ponto como pontos fantasmas
- Para curvas fechadas, repete-se os nós iniciais no final ou os nós finais no início
---
# Parâmetro de tensão
:::col width=60%
- A fórmula original de Catmull-Rom usa o fator $\tfrac{1}{2}$ na tangente:
$$
\mathbf{T}_i = \frac{\mathbf{P}_{i+1} - \mathbf{P}_{i-1}}{2}
$$
- Generalizando, introduz-se o **parâmetro de tensão** $\tau \in [0,1]$:
$$
\mathbf{T}_i = (1-\tau)\,\frac{\mathbf{P}_{i+1} - \mathbf{P}_{i-1}}{2}
$$
- $\tau = 0$: Catmull-Rom original (tensão nula, curva mais solta)
- $\tau = 1$: tangentes nulas em todos os pontos — curva degenera em segmentos de reta ($C^0$)
- A matriz de base parametrizada por $\tau$ é:
$$
\mathbf{M}_{CR}(\tau) = \frac{1-\tau}{2}
\begin{bmatrix}
-1 &  3 & -3 &  1 \\
 2 & -5 &  4 & -1 \\
-1 &  0 &  1 &  0 \\
 0 &  2 &  0 &  0
\end{bmatrix}
+ \tau
\begin{bmatrix}
0 & 0 & 0 & 0 \\
0 & 1 &-2 & 1 \\
0 &-1 & 2 &-1 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$
- $\tau$ pode ser definido **por ponto**, permitindo diferentes tensões locais
:::
:::col width=40%
::img src=catmull_rom_tension.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcatmull_rom_curve.zip)
:::
---
# Variante centripetal e comparações
:::col width=60%
- A variante **uniforme** pode gerar torções e auto-interseções quando os pontos estão muito irregularmente espaçados
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
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F12+-+Curvas%2Fcatmull_rom_curve.zip)
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
