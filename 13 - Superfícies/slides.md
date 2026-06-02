:::center
# Computação Visual
## 13 - Modelagem geométrica: Superfícies
:::
---
# Superfícies paramétricas
:::col width=60%
- Uma superfície paramétrica é dada por uma função de **dois** parâmetros
$$
\mathbf{x}(s,t): \mathbb{R}^2 \rightarrow \mathbb{R}^3, \quad (s,t) \in [a,b]\times[c,d]
$$
- Para cada par $(s,t)$ no domínio retangular, $\mathbf{x}(s,t)$ devolve um ponto no espaço
- Tudo o que vimos para curvas (pontos de controle, funções de mistura, Bézier, B-splines, NURBS, subdivisão) **estende-se** para superfícies
:::
:::col width=40%
- Comparação com curvas:
  - **Domínio**: $[a,b]$ (curva) → $[a,b]\times[c,d]$ (superfície)
  - **Parâmetros**: $t$ → $s,t$
  - **Controle**: polígono → grade de pontos
:::
---
# Um caso simples: interpolação bilinear
:::col width=55%
- O análogo da interpolação linear (segmento de reta) é a **interpolação bilinear** de quatro pontos
- Dada uma grade $2\times2$ de pontos $\mathbf{P}_{0,0}, \mathbf{P}_{1,0}, \mathbf{P}_{0,1}, \mathbf{P}_{1,1}$:
$$
\small
\mathbf{x}(s,t) = (1-s)(1-t)\,\mathbf{P}_{0,0} + s(1-t)\,\mathbf{P}_{1,0} \\
~\\
\quad +\; (1-s)\,t\,\mathbf{P}_{0,1} + s\,t\,\mathbf{P}_{1,1}
$$
:::
:::col width=45%
::img src=bilinear_surface.svg height=70%
- A ordem das interpolações não altera o resultado
:::
---
# Retalhos e produto tensorial
:::col
- A maneira padrão de construir superfícies é o **produto tensorial** de duas curvas paramétricas
- Combinam-se as funções de mistura de cada parâmetro:
$$
\small
\mathbf{x}(s,t) = \sum_{i=0}^{n}\sum_{j=0}^{m} \mathbf{P}_{i,j}\, N_i(s)\, M_j(t)
$$
:::
:::col
- A superfície fica definida sobre um **retângulo** no espaço de parâmetros, tipicamente $0 \le s < 1,\ 0 \le t < 1$
- A forma é especificada por uma **grade de controle** de pontos $\mathbf{P}_{i,j}$
  - $2\times2$ pontos → superfície bilinear
  - $3\times3$ → biquadrática
  - $4\times4$ → bicúbica, etc.
- Cada retângulo assim definido é chamado de **retalho** (_patch_)
:::
---
# Retalhos de Bézier
:::col width=60%
- Como nas curvas de Bézier, as funções de mistura são os **polinômios de Bernstein** $B_i^n(s)$ e $B_j^m(t)$, de graus $n$ e $m$
$$
\mathbf{x}(s,t) = \sum_{i=0}^{n}\sum_{j=0}^{m} \mathbf{P}_{i,j}\, B_i^n(s)\, B_j^m(t)
$$
- Frequentemente $n = m = 3$ (retalho **bicúbico**)
  - Necessários $4\times4 = 16$ pontos de controle $\mathbf{P}_{i,j}$
:::
:::col width=40%
::img src=bezier_surface.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F13+-+Superf%C3%ADcies%2Fbezier_surface.zip)
:::
---
# Avaliação como curvas de curvas
:::col width=60%
- Qualquer curva isoparamétrica ($s$ ou $t$ constante) é uma **curva de Bézier**
- Podemos avaliar $\mathbf{x}(s,t)$ em duas etapas:
  - Cada linha da grade ($4$ pontos) define uma curva de Bézier em $s$
  - Avaliando as $4$ linhas no mesmo $s$ obtemos $4$ pontos de controle **"virtuais"**
  - Esses pontos virtuais definem uma curva de Bézier em $t$
  - Avaliá-la em $t$ resulta no ponto $\mathbf{x}(s,t)$
:::
:::col width=40%
- Consequência prática: tudo o que sabemos sobre curvas (de Casteljau, reparametrização, subdivisão) aplica-se **direção a direção**
- A ordem ($s$ depois $t$ ou $t$ depois $s$) é indiferente
:::
---
# Propriedades dos retalhos de Bézier
:::col width=60%
- O retalho **interpola os quatro cantos** da grade de controle
  - Decorre da propriedade análoga das curvas de Bézier
- As **curvas de fronteira** são curvas de Bézier definidas pelas arestas da grade
- O **plano tangente** em um canto é definido pelas duas arestas da grade incidentes nesse canto
- O retalho está contido no **fecho convexo** da grade de controle
  - As funções de base são positivas e somam $1$ em toda parte
:::
:::col width=40%
::img src=bezier_surface.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F13+-+Superf%C3%ADcies%2Fbezier_surface.zip)
:::
---
# Retalhos de Bézier em forma matricial
- Para um retalho bicúbico, separando os parâmetros em vetores de potências:
$$\small
\mathbf{x}(s,t) = \mathbf{S}\,\mathbf{M}_B\,\mathbf{P}\,\mathbf{M}_B^{T}\,\mathbf{T}^{T}
$$onde
  - $\mathbf{S} = [s^3, s^2, s, 1]$ e $\mathbf{T} = [t^3, t^2, t, 1]$
  - $\mathbf{M}_B$ é a matriz de Bézier (a mesma das curvas)
  - $\mathbf{P}$ é a grade $4\times4$ de pontos de controle (aplicada coordenada a coordenada)
- Se os pontos de controle não mudam, pré-computa-se o produto das **três matrizes do meio** $\mathbf{M}_B\,\mathbf{P}\,\mathbf{M}_B^{T}$
  - Avaliar a superfície reduz-se a dois produtos vetor-matriz
---
# Malhas de retalhos de Bézier
:::col
- Superfícies complexas são modeladas como **malhas de retalhos** unidos ao longo das fronteiras
- Restrições para uma malha válida:
  - As arestas das grades de controle vizinhas precisam se **justapor perfeitamente**
  - As grades precisam ser **retangulares**
- É exatamente o mesmo problema das curvas longas: um único retalho de grau alto é caro e tem suporte global, então emendamos retalhos de grau baixo
:::
:::col 
::img src=valid_patches.svg
:::
---
# Continuidade em malhas de retalhos
:::col
- Como nas curvas, os pontos de controle precisam satisfazer **restrições** nas fronteiras
- Continuidade paramétrica ao longo de uma aresta:
  - $C^0$: os pontos de controle da aresta são os **mesmos** nos dois retalhos
  - $C^1$: os pontos vizinhos à aresta têm que ser **colineares e equidistantes**
  - $C^2$: restrições adicionais sobre pontos mais distantes da aresta
:::
:::col
- Continuidade **geométrica** ($G^1$): pontos vizinhos colineares, mas **não** necessariamente equidistantes — restrição mais frouxa
- Continuidade nos **vértices** da malha é mais delicada
  - Para $C^1$ em um vértice, todas as arestas incidentes precisam ser colineares — difícil de satisfazer em vértices de valência arbitrária
:::
---
# Desenhando retalhos — amostragem
:::col width=60%
- **Opção 1**: avaliar o retalho numa grade de pontos do domínio e **triangular**
  - $s$ e $t$ tomados em intervalos (regulares ou não), gerando uma grade de pontos
  - Cada célula da grade (4 pontos) gera **2 triângulos**
  - Não se usam quadriláteros: os 4 pontos não são necessariamente coplanares
  - Renderização eficiente com _triangle strips_
:::
:::col width=40%
- **Vantagem**: simples e diretamente suportado pela GPU / OpenGL
- **Desvantagem**: difícil controlar o nível de detalhe de forma **adaptativa** (regiões planas e curvas recebem a mesma densidade de triângulos)
:::
---
# Desenhando retalhos — subdivisão
:::col width=60%
- **Opção 2**: usar **subdivisão**, permitindo controle de erro durante a aproximação
- Análoga à subdivisão de curvas de Bézier (de Casteljau em $t=\tfrac12$), mas o refinamento é feito **alternadamente nos dois eixos**:
  1. Aplicar a subdivisão em cada **linha** da grade: $4\times4 \rightarrow 4\times7$
  2. Repetir em cada **coluna**: $4\times7 \rightarrow 7\times7$
:::
:::col width=40%
- Cada passo computa sucessivamente **pontos médios** dos vértices e os une (_midpoint subdivision_)
- Resultado: a grade $4\times4$ é substituída por **4 sub-grades** $4\times4$, cada uma descrevendo um quarto do retalho
:::
---
# Midpoint subdivision
:::row
- Subdividir um retalho de Bézier em $s=\tfrac12$ produz duas grades equivalentes ao longo de $s$; repetindo em $t=\tfrac12$ obtemos **quatro** sub-retalhos
- Os novos pontos de controle são apenas **médias de pontos vizinhos** — sem avaliar polinômios
- A grade de controle de cada sub-retalho aproxima a superfície melhor que a original (converge para a superfície)
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F13%20-%20Superf%C3%ADcies%2Fbezier_surface_subdiv.zip)
:::
:::row
::img src=subdiv1.png height=80%
::img src=subdiv2.png height=80%
::img src=subdiv3.png height=80%
::img src=subdiv4.png height=80%
:::
---
# Procedimento adaptativo
:::col width=60%
- Subdivide-se recursivamente apenas onde é necessário:
  - Se a grade de controle é **aproximadamente plana**, desenha-se
  - Senão, subdivide-se em **4 sub-grades** e aplica-se o procedimento recursivamente
- **Problema**: retalhos vizinhos podem ser subdivididos em níveis diferentes
:::
:::col width=40%
- Isso gera **rachaduras** (_cracks_): os polígonos de controle das bordas não se justapõem
- Solução: forçar a grade mais subdividida a se **alinhar** com a menos subdividida ao longo da aresta comum
:::
---
# Computando o vetor normal
- Para iluminação precisamos da **normal** em cada ponto da superfície
- As **derivadas parciais** $\dfrac{\partial \mathbf{x}}{\partial s}$ e $\dfrac{\partial \mathbf{x}}{\partial t}$ são tangentes à superfície e geram o plano tangente
- A normal é o **produto vetorial** normalizado:
$$
\mathbf{n}(s,t) = \frac{\dfrac{\partial \mathbf{x}}{\partial s} \times \dfrac{\partial \mathbf{x}}{\partial t}}{\left\| \dfrac{\partial \mathbf{x}}{\partial s} \times \dfrac{\partial \mathbf{x}}{\partial t} \right\|}
$$
- Na prática (malha triangulada), aproxima-se pela média das normais das faces incidentes em cada vértice
---
# Retalhos B-spline
:::col width=60%
- Os mesmos motivos das curvas (suporte local, modelagem sem restrições de continuidade) levam aos **retalhos B-spline**:
$$
\mathbf{x}(s,t) = \sum_{i}\sum_{j} \mathbf{P}_{i,j}\, B_i(s)\, B_j(t)
$$
- $B_i(s)$ e $B_j(t)$ são as funções de base B-spline em cada direção
- É preciso fornecer **dois vetores de nós**, um por direção
  - Permite retalhos B-spline uniformes e **não uniformes**
:::
:::col width=40%
::img src=nurbs_surface.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F13%20-%20Superf%C3%ADcies%2Fnurbs_surface.zip)
:::
---
# Forma matricial das B-splines bicúbicas
- Como para Bézier, um retalho B-spline bicúbico uniforme escreve-se
$$
\mathbf{x}(s,t) = \mathbf{S}\,\mathbf{M}\,\mathbf{P}\,\mathbf{M}^{T}\,\mathbf{T}^{T}
$$
onde $\mathbf{P}$ é a grade de pontos de controle e $\mathbf{M}$ é a matriz de coeficientes da B-spline cúbica uniforme:
$$
\mathbf{M} = \frac{1}{6}\begin{bmatrix}
-1 &  3 & -3 & 1 \\
 3 & -6 &  3 & 0 \\
-3 &  0 &  3 & 0 \\
 1 &  4 &  1 & 0
\end{bmatrix}
$$
- Trocar a matriz $\mathbf{M}_B$ por esta $\mathbf{M}$ basta para passar de retalhos Bézier para B-spline
---
# Avaliando retalhos B-spline uniformes
:::col width=60%
- Todas as funções de base são **translações** de uma mesma função
- Para avaliar em $(s,t)$:
  - Sejam $a = \lfloor s \rfloor$, $b = \lfloor t \rfloor$ (intervalo de nós)
  - Computar os parâmetros locais $u = s - a$, $v = t - b$
  - Usar as funções de base para o intervalo $[0,1)$ sobre os $4\times4$ pontos de controle vizinhos
:::
:::col width=40%
::img src=nurbs_surface.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F13+-+Superf%C3%ADcies%2Fnurbs_surface.zip)
:::
---
# Subdivisão de retalhos B-spline
:::col width=60%
- A grade de controle de uma B-spline bicúbica pode ser **refinada** em 4 sub-grades, permitindo desenho adaptativo (como em Bézier)
- A partir de uma grade $3\times3$ (suporte de um trecho bicúbico), o refinamento gera **25 pontos de controle**, divididos em 4 grupos de $3\times3$
- Cada novo ponto é uma **combinação ponderada fixa** dos pontos vizinhos da grade original
:::
:::col width=40%
- Esse refinamento **insere nós** em ambas as direções, dobrando a resolução da grade
- É a semente da ideia de **superfícies de subdivisão**: refinar a malha aplicando regras locais de média (veremos a seguir)
:::
---
# Propriedades dos retalhos B-spline
- O retalho está restrito ao **fecho convexo** da grade de controle
- Continuidade $C^2$ para B-splines **bicúbicas**
- Pode-se forçar **interpolação** duplicando nós (ou pontos) de controle
  - Problema: as derivadas parciais podem se anular e a normal ficar **indefinida**
  - Solução: usar um ponto próximo, estimar pela média das normais da grade, ou usar **B-splines interpoladoras**
- B-splines **não uniformes** dão mais controle à modelagem
- **Retalhos NURBS** generalizam tudo isso com pesos (coordenadas homogêneas), permitindo representar quádricas (esferas, cilindros) exatamente
---
# Superfícies de subdivisão
:::col width=60%
- Vimos para **curvas** uma alternativa elegante às splines: a **subdivisão** (Chaikin, Lane-Riesenfeld, 4-pontos)
  - Partindo de um polígono, aplica-se repetidamente uma **regra local de refinamento** que duplica e suaviza os vértices
  - A sequência converge para uma curva suave
- A mesma ideia se aplica a **superfícies**, e é hoje a representação dominante em animação e modelagem
:::
:::col width=40%
- Vantagens (as mesmas das curvas):
  - Implementação simples (apenas médias)
  - Estrutura **hierárquica** / multirresolução
  - Custo **linear** no número de pontos
  - **Topologia arbitrária** (não só grades retangulares!)
:::
---
# Adaptando a subdivisão de curvas (produto tensorial)
:::col width=60%
- A maneira mais direta de obter uma superfície de subdivisão é o **produto tensorial** do esquema de curva:
  1. Aplicar o passo de subdivisão de curva a cada **linha** da grade (direção $v$)
  2. **Transpor** a grade
  3. Aplicar o mesmo passo a cada linha (agora direção $u$)
  4. **Transpor** de volta
- **Um** passo de subdivisão de superfície = **dois** passes de subdivisão de curva
:::
:::col width=40%
- É exatamente o que fazem `lr_surface` e `four_point_surface` no demo: reutilizam, sem modificação, as rotinas `lr` e `four_point` das curvas
- Vale qualquer esquema de curva (Lane-Riesenfeld, 4-pontos, Chaikin…)
:::
---
# Lane-Riesenfeld tensorial
:::col width=60%
- Aplicando o esquema de **Lane-Riesenfeld** em ambas as direções, obtemos superfícies **B-spline uniformes** por subdivisão
- Cada passe (por linha) faz:
  1. **Refinamento**: duplicar os pontos (insere pontos médios)
  2. **Suavização**: $d-1$ rodadas de médias de pares adjacentes
- Grau $d=2$ → B-spline biquadrática; $d=3$ → bicúbica (a mesma do refinamento B-spline visto antes)
:::
:::col width=40%
::img src=lr_surface.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F13+-+Superf%C3%ADcies%2Fsubdivision_surfaces.zip)
:::
---
# Esquema dos 4-pontos tensorial
:::col width=60%
- Aplicando o esquema de **4-pontos (Dyn-Levin-Gregory)** em ambas as direções, obtemos uma superfície que **interpola** a grade de controle original
- Para cada par de pontos insere-se um ponto novo:
$$
\small
\mathbf{q} = -w\,\mathbf{p}_{-1} + (\tfrac12 + w)\,\mathbf{p}_{0} + (\tfrac12 + w)\,\mathbf{p}_{1} - w\,\mathbf{p}_{2}
$$
- Os pontos originais são **mantidos** (interpolação); $w \approx \tfrac{1}{16}$ controla a tensão
:::
:::col width=40%
::img src=4p_surface.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F13+-+Superf%C3%ADcies%2Fsubdivision_surfaces.zip)
:::
---
# Limite do produto tensorial
- O produto tensorial só funciona sobre grades **retangulares** com vértices de valência $4$
- Modelos reais têm topologia arbitrária: vértices com $3$, $5$ ou mais arestas, faces triangulares ou $n$-laterais, buracos…
- Precisamos de esquemas que operem sobre **malhas poligonais arbitrárias**, e não sobre grades $u\times v$
- A ideia central permanece: a cada passo, **refinar** a malha (mais faces) e **reposicionar** os vértices por **médias locais**
- Os esquemas clássicos generalizam exatamente as superfícies de produto tensorial que já conhecemos:
  - **Catmull-Clark** → generaliza a B-spline **bicúbica**
  - **Doo-Sabin** → generaliza a B-spline **biquadrática**
  - **Loop** → para malhas **triangulares**
---
# Subdivisão de Catmull-Clark
:::col width=60%
- Funciona em malhas de **quadriláteros** (e converte $n$-gonos em quadriláteros no primeiro passo). Cada passo cria três tipos de pontos:
  - **Ponto de face** $\mathbf{f}$: média dos vértices da face
  - **Ponto de aresta** $\mathbf{e}$: média dos 2 extremos da aresta e dos 2 pontos de face adjacentes
  - **Ponto de vértice** $\mathbf{v'}$: reposiciona o vértice original $\mathbf{v}$ de valência $n$:
$$
\small
\mathbf{v'} = \frac{\mathbf{F} + 2\mathbf{R} + (n-3)\,\mathbf{v}}{n}
$$
  onde $\mathbf{F}$ = média dos pontos de face vizinhos e $\mathbf{R}$ = média dos pontos médios das arestas vizinhas
:::
:::col width=40%
- Reconectam-se os novos pontos formando **quadriláteros**
- Em regiões regulares (valência $4$) o limite é **exatamente** uma B-spline bicúbica ($C^2$)
- Em **vértices extraordinários** (valência $\ne 4$) a continuidade cai para $C^1$, mas a superfície permanece suave
- É o esquema usado pela Pixar (_OpenSubdiv_)
:::
---
# Subdivisão de Loop
:::col width=60%
- Esquema **aproximador** para malhas **triangulares** (Charles Loop, 1987)
- Cada triângulo é dividido em **4**, criando um novo vértice por aresta:
  - **Vértice de aresta** (ímpar): $\tfrac38$ de cada extremo da aresta $+ \tfrac18$ de cada vértice oposto
  - **Vértice antigo** (par), de valência $n$, é suavizado:
$$
\small
\mathbf{v'} = (1 - n\beta)\,\mathbf{v} + \beta \sum_{i} \mathbf{v}_i,\quad
\beta = \frac{1}{n}\!\left(\frac58 - \Big(\tfrac38 + \tfrac14\cos\tfrac{2\pi}{n}\Big)^{2}\right)
$$
:::
:::col width=40%
- O limite tem continuidade $C^2$ nos vértices regulares (valência $6$) e $C^1$ nos extraordinários
- É o análogo triangular de Catmull-Clark
- Outros esquemas para triângulos: **$\sqrt{3}$-subdivision**, **butterfly** (interpolador)
:::
---
# Resumo
- **Superfícies paramétricas**: funções $\mathbf{x}(s,t): \mathbb{R}^2 \to \mathbb{R}^3$ sobre um domínio retangular
- **Produto tensorial**: combina as funções de mistura de curvas em duas direções → retalhos **Bézier**, **B-spline** e **NURBS**, controlados por uma grade
- Quase tudo das curvas se transfere **direção a direção**: de Casteljau, forma matricial, subdivisão, continuidade
- **Desenho**: amostragem + triangulação, ou subdivisão adaptativa (cuidado com rachaduras)
- **Superfícies de subdivisão**: refinamento iterativo por médias locais
  - Produto tensorial dos esquemas de curva (Lane-Riesenfeld, 4-pontos)
  - Generalização para topologia arbitrária: **Catmull-Clark**, **Doo-Sabin**, **Loop**
