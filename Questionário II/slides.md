### Na formulação de curvas paramétricas $\mathbf{C}(t) = \sum_{i=0}^{n} \mathbf{P}_i N_i(t)$, qual é o papel das funções $N_i(t)$?

- A. Definem as posições absolutas dos pontos de controle no espaço euclidiano.

- B. São as funções de mistura (blending functions) que ponderam a contribuição de cada ponto de controle.

- C. Determinam o número de subdivisões necessárias para desenhar a curva.

- D. Calculam a curvatura da curva em cada ponto de controle.
---
### O que significa dizer que uma curva possui continuidade $C^2$?

- A. A curva é composta por exatamente dois segmentos polinomiais.

- B. A curva, sua derivada primeira (tangente) e sua derivada segunda (curvatura) são todas contínuas.

- C. A curva passa por todos os pontos de controle e tem dois pontos de inflexão.

- D. A curva possui grau 2 (quadrática) em todo o seu domínio.
---
### Qual a diferença fundamental entre interpolação e aproximação no contexto de curvas paramétricas?

- A. Interpolação usa polinômios de grau baixo, enquanto aproximação usa grau alto.

- B. Interpolação gera curvas que passam por todos os pontos dados, enquanto aproximação gera curvas que passam "perto" dos pontos.

- C. Aproximação é sempre mais precisa que interpolação.

- D. Interpolação é usada apenas em 2D e aproximação em 3D.
---
### As funções de mistura das curvas de Bézier são os polinômios de Bernstein. Qual é a fórmula correta do polinômio $B_i^n(t)$?

- A. $B_i^n(t) = \binom{n}{i} t^n (1-t)^i$

- B. $B_i^n(t) = \binom{n}{i} t^i (1-t)^{n-i}$

- C. $B_i^n(t) = \frac{n!}{i!} t^i (1-t)^n$

- D. $B_i^n(t) = \frac{t^i}{(1+t)^n}$
---
### Quantos pontos de controle são necessários para definir uma curva de Bézier de grau 3 (cúbica)?

- A. 3 pontos.

- B. 4 pontos.

- C. 5 pontos.

- D. 6 pontos.
---
### Qual das seguintes NÃO é uma propriedade das curvas de Bézier?

- A. A curva está contida no fecho convexo dos pontos de controle.

- B. A curva interpola todos os pontos de controle.

- C. A curva passa pelo primeiro e pelo último ponto de controle.

- D. A tangente no ponto inicial é dada pela direção $\mathbf{P}_1 - \mathbf{P}_0$.
---
### O algoritmo de de Casteljau calcula pontos em uma curva de Bézier. Qual é sua principal vantagem sobre a avaliação direta dos polinômios de Bernstein?

- A. É mais rápido por usar multiplicação de matrizes em GPU.

- B. Permite desenhar curvas de grau infinito sem custo adicional.

- C. Evita erros numéricos consideráveis para graus altos, usando apenas interpolação linear repetida.

- D. Produz automaticamente uma triangulação da curva para renderização.
---
### No contexto de curvas de Bézier longas, por que se prefere emendar segmentos de grau baixo em vez de usar uma única curva de grau alto?

- A. Curvas de grau alto não podem ser transformadas por matrizes afins.

- B. Curvas de grau alto são mais sujeitas a erros de precisão e todos os pontos de controle têm efeito global.

- C. Curvas de grau alto são sempre descontínuas nas junções.

- D. Curvas de grau baixo não precisam de funções de mistura.
---
### Em uma spline de Hermite cúbica, quais são as condições de contorno que definem cada segmento?

- A. Apenas as posições dos dois extremos do segmento.

- B. As posições dos dois extremos e as tangentes (vetores de velocidade) nos dois extremos.

- C. As posições de quatro pontos de controle equidistantes.

- D. A posição de um extremo e a curvatura no outro.
---
### Como se obtém continuidade $C^1$ na junção entre dois segmentos de Hermite consecutivos?

- A. Os dois segmentos devem ter a mesma curvatura no ponto de junção.

- B. A tangente de saída do primeiro segmento deve ser igual à tangente de entrada do segundo segmento.

- C. Os segmentos devem compartilhar os mesmos quatro pontos de controle.

- D. A derivada segunda deve ser contínua no ponto de junção.
---
### Na relação entre curvas de Bézier cúbicas e de Hermite, como se obtêm os pontos de controle internos de Bézier ($\mathbf{Q}_1$ e $\mathbf{Q}_2$) a partir dos parâmetros de Hermite?

- A. $\mathbf{Q}_1 = \mathbf{P}_0 + \tfrac{1}{3}\mathbf{T}_0$ e $\mathbf{Q}_2 = \mathbf{P}_1 - \tfrac{1}{3}\mathbf{T}_1$

- B. $\mathbf{Q}_1 = \mathbf{P}_0 + \mathbf{T}_0$ e $\mathbf{Q}_2 = \mathbf{P}_1 - \mathbf{T}_1$

- C. $\mathbf{Q}_1 = \tfrac{1}{2}(\mathbf{P}_0 + \mathbf{P}_1)$ e $\mathbf{Q}_2 = \tfrac{1}{2}(\mathbf{T}_0 + \mathbf{T}_1)$

- D. $\mathbf{Q}_1 = \mathbf{T}_0$ e $\mathbf{Q}_2 = \mathbf{T}_1$
---
### Qual é a principal vantagem das B-Splines em relação às curvas de Bézier para modelar curvas longas?

- A. As B-Splines sempre passam por todos os pontos de controle.

- B. As B-Splines possuem suporte local: alterar um vértice afeta a curva apenas na vizinhança.

- C. As B-Splines não precisam de pontos de controle.

- D. As B-Splines podem representar apenas retas e círculos.
---
### Na recorrência de Cox-de Boor para B-Splines, qual é o caso base $B^0_i(t)$?

- A. $B^0_i(t) = t^i$ para todo $t$.

- B. $B^0_i(t) = 1$ se $t_i \le t < t_{i+1}$, e $0$ caso contrário.

- C. $B^0_i(t) = \frac{1}{n}$ para todo $i$.

- D. $B^0_i(t) = (1-t)^i$ para $t \in [0,1]$.
---
### Uma B-spline uniforme de grau $d$ possui qual nível de continuidade?

- A. $C^0$ (apenas contínua).

- B. $C^{d-1}$.

- C. $C^d$.

- D. $C^{d+1}$.
---
### O que são NURBS e por que são necessárias?

- A. São B-Splines com pesos uniformes, usadas apenas para retas.

- B. São Non-Uniform Rational B-Splines, necessárias porque é impossível representar círculos e quádricas com B-splines convencionais.

- C. São curvas de Bézier de grau infinito, usadas para animação.

- D. São polinômios de Lagrange não uniformes para interpolação de dados.
---
### Nas splines de Catmull-Rom, como são estimadas as tangentes em cada ponto de controle $\mathbf{P}_i$?

- A. $\mathbf{T}_i = \mathbf{P}_{i+1} - \mathbf{P}_i$

- B. $\mathbf{T}_i = \frac{\mathbf{P}_{i+1} - \mathbf{P}_{i-1}}{2}$

- C. $\mathbf{T}_i = \frac{\mathbf{P}_{i+1} + \mathbf{P}_{i-1}}{2}$

- D. $\mathbf{T}_i = \mathbf{P}_i \times \mathbf{P}_{i+1}$
---
### O que acontece com uma spline de Catmull-Rom quando o parâmetro de tensão $\tau$ é igual a $1$?

- A. A curva se torna uma B-spline cúbica.

- B. As tangentes se anulam em todos os pontos e a curva degenera em segmentos de reta ($C^0$).

- C. A curva passa a interpolar os pontos com continuidade $C^2$.

- D. A curva se torna um círculo perfeito.
---
### No algoritmo de Chaikin (1974), como são gerados os novos pontos a cada iteração?

- A. Cada ponto de controle é substituído pela média de todos os outros pontos.

- B. Cada aresta gera dois novos pontos a $\tfrac{1}{4}$ e $\tfrac{3}{4}$ da aresta, e os vértices originais são descartados.

- C. Cada ponto é duplicado e deslocado aleatoriamente.

- D. Pontos médios são inseridos entre pares, mas os vértices originais são mantidos.
---
### Para que tipo de curva o algoritmo de Chaikin converge?

- A. Curva de Bézier cúbica.

- B. B-spline quadrática uniforme.

- C. Spline de Catmull-Rom.

- D. Polinômio de Lagrange de grau $n$.
---
### No algoritmo de Lane-Riesenfeld, quais são os dois passos de cada iteração?

- A. Translação e rotação de cada ponto de controle.

- B. Refinamento (inserir pontos médios) seguido de $d-1$ rodadas de suavização (médias de pares adjacentes).

- C. Avaliação dos polinômios de Bernstein e posterior reparametrização.

- D. Projeção dos pontos no plano e posterior elevação para 3D.
---
### Qual a vantagem da variante centrípeta da spline de Catmull-Rom sobre a variante uniforme?

- A. A variante centrípeta é mais rápida computacionalmente.

- B. A variante centrípeta evita torções e auto-interseções quando os pontos estão muito irregularmente espaçados.

- C. A variante centrípeta sempre produz curvas fechadas.

- D. A variante centrípeta não requer pontos de controle.
---
### O que é uma superfície paramétrica e como ela se relaciona com as curvas paramétricas?

- A. É uma função de três parâmetros que retorna um ponto 2D.

- B. É uma função de dois parâmetros $(s,t)$ que retorna um ponto no espaço 3D, estendendo o conceito de curvas paramétricas (um parâmetro).

- C. É idêntica a uma curva, mas desenhada com linhas mais grossas.

- D. É uma curva paramétrica avaliada apenas em pontos inteiros.
---
### Na interpolação bilinear de uma superfície, quantos pontos de controle são necessários?

- A. 2 pontos (como uma reta).

- B. 3 pontos (como um triângulo).

- C. 4 pontos numa grade $2\times2$.

- D. 9 pontos numa grade $3\times3$.
---
### O que é um "retalho" (patch) no contexto de superfícies paramétricas?

- A. Uma textura aplicada sobre um modelo 3D.

- B. Uma superfície definida sobre um retângulo no espaço de parâmetros, controlada por uma grade de pontos.

- C. Uma aresta da malha de triângulos.

- D. Um erro de continuidade entre duas superfícies vizinhas.
---
### Quantos pontos de controle são necessários para definir um retalho de Bézier bicúbico?

- A. 4 pontos ($2\times2$).

- B. 9 pontos ($3\times3$).

- C. 16 pontos ($4\times4$).

- D. 25 pontos ($5\times5$).
---
### Qual a principal propriedade que permite avaliar um retalho de Bézier como "curvas de curvas"?

- A. Qualquer curva isoparamétrica ($s$ ou $t$ constante) é uma curva de Bézier.

- B. A superfície é sempre plana ao longo de uma das direções.

- C. O produto tensorial elimina a necessidade de pontos de controle.

- D. A superfície é avaliada apenas nos cantos da grade.
---
### Como é obtido o vetor normal em um ponto de uma superfície paramétrica?

- A. Pela média aritmética das posições dos pontos de controle vizinhos.

- B. Pelo produto vetorial normalizado das derivadas parciais $\frac{\partial \mathbf{x}}{\partial s}$ e $\frac{\partial \mathbf{x}}{\partial t}$.

- C. Pela derivada segunda da superfície em relação ao parâmetro $t$.

- D. Pela projeção do vetor "up" do mundo no plano tangente.
---
### Para garantir continuidade $C^1$ entre dois retalhos de Bézier vizinhos ao longo de uma aresta, quais condições devem ser satisfeitas?

- A. Apenas que os retalhos compartilhem a mesma aresta de pontos de controle.

- B. Os pontos de controle da aresta compartilhada devem coincidir ($C^0$) e os pontos vizinhos à aresta devem ser colineares e equidistantes.

- C. Os dois retalhos devem ter o mesmo número de pontos de controle.

- D. As normais nos cantos devem ser paralelas.
---
### O que é a continuidade geométrica $G^1$ e como difere de $C^1$?

- A. $G^1$ exige apenas que pontos vizinhos à aresta sejam colineares, mas não necessariamente equidistantes; $C^1$ exige equidistância.

- B. $G^1$ e $C^1$ são a mesma coisa, apenas com nomes diferentes.

- C. $G^1$ significa que a curvatura é contínua; $C^1$ não.

- D. $G^1$ requer que a superfície seja planar na junção.
---
### Na subdivisão de um retalho de Bézier (midpoint subdivision), como é feita a divisão em quatro sub-retalhos?

- A. O retalho é cortado por dois planos arbitrários.

- B. Aplica-se a subdivisão em cada linha da grade ($4\times4 \rightarrow 4\times7$) e depois em cada coluna ($4\times7 \rightarrow 7\times7$), obtendo 4 sub-grades $4\times4$.

- C. Os pontos de controle são descartados e novos pontos são gerados aleatoriamente.

- D. Cada triângulo da malha é subdividido em 4 triângulos menores.
---
### Qual é a principal vantagem da subdivisão adaptativa de superfícies sobre a amostragem uniforme?

- A. A subdivisão adaptativa é mais simples de implementar.

- B. A subdivisão adaptativa permite controlar o nível de detalhe, refinando mais onde a superfície é curva e menos onde é plana.

- C. A subdivisão adaptativa não precisa de pontos de controle.

- D. A subdivisão adaptativa sempre produz menos triângulos que a amostragem uniforme.
---
### Qual é a forma matricial de um retalho B-spline bicúbico uniforme?

- A. $\mathbf{x}(s,t) = \mathbf{S}\,\mathbf{M}\,\mathbf{P}\,\mathbf{M}^{T}\,\mathbf{T}^{T}$, onde $\mathbf{M}$ é a matriz de coeficientes da B-spline cúbica uniforme.

- B. $\mathbf{x}(s,t) = \mathbf{P} + \mathbf{S} + \mathbf{T}$, uma simples soma de matrizes.

- C. $\mathbf{x}(s,t) = \mathbf{S}^{-1}\,\mathbf{P}\,\mathbf{T}^{-1}$, envolvendo inversas.

- D. $\mathbf{x}(s,t) = \det(\mathbf{P}) \cdot s \cdot t$.
---
### Para obter superfícies de subdivisão por produto tensorial, qual é o procedimento aplicado?

- A. Aplica-se o esquema de subdivisão de curva a cada linha da grade, transpõe-se, aplica-se novamente e transpõe-se de volta.

- B. Duplica-se a grade inteira e aplica-se uma rotação de 90°.

- C. Remove-se cada segundo ponto de controle e recalculam-se as normais.

- D. Cada ponto é projetado no eixo $z$ e reamostrado.
---
### Qual esquema de subdivisão de curva, quando aplicado por produto tensorial, produz superfícies B-spline uniformes?

- A. O algoritmo de de Casteljau.

- B. O algoritmo de Lane-Riesenfeld.

- C. A interpolação de Lagrange.

- D. A reparametrização de Bézier.
---
### No esquema dos 4-pontos tensorial, o que acontece com os pontos da grade original após cada iteração?

- A. São descartados e substituídos por novos pontos.

- B. São mantidos (interpolados) e novos pontos são inseridos entre eles.

- C. São deslocados para o centroide da grade.

- D. São duplicados e espelhados ao longo do eixo principal.
---
### No contexto de modelos geométricos, o que é B-Rep (Boundary Representation)?

- A. Uma representação onde o interior do objeto é decomposto em tetraedros.

- B. Uma representação onde o objeto é descrito pela(s) superfície(s) que o delimita(m).

- C. Uma função implícita que define o interior como $f(x,y,z) \le 0$.

- D. Uma grade regular de voxels preenchida com valores de densidade.
---
### Qual é a fórmula de Euler-Poincaré para superfícies fechadas e o que ela relaciona?

- A. $V + E + F = 2G$, soma de vértices, arestas e faces igual ao dobro do genus.

- B. $V - E + F = 2 - 2G$, relaciona vértices ($V$), arestas ($E$), faces ($F$) e genus ($G$) de uma superfície fechada.

- C. $V \times E = F + G$, o produto de vértices e arestas é igual à soma de faces e genus.

- D. $V = E - F + 2G$, o número de vértices é determinado pelas arestas e faces.
---
### Para uma esfera (genus $G=0$), qual é o valor de $V - E + F$ segundo a fórmula de Euler-Poincaré?

- A. $0$.

- B. $1$.

- C. $2$.

- D. $4$.
---
### O algoritmo Marching Cubes converte uma função implícita em malha triangular. Quantos casos distintos existem (reduzidos por simetria)?

- A. 8 casos.

- B. 15 casos.

- C. 32 casos.

- D. 256 casos.
---
### Qual é a principal vantagem do Marching Tetrahedra sobre o Marching Cubes?

- A. Produz menos triângulos no total.

- B. Poligoniza cada tetraedro de forma exata e sem ambiguidade.

- C. Funciona apenas com malhas quadrangulares.

- D. Não precisa amostrar a função implícita.
---
### Qual é a representação mais simples de uma malha poligonal?

- A. A estrutura half-edge (DCEL).

- B. Uma árvore BSP com planos de corte.

- C. Uma tabela de vértices (posições) e uma tabela de faces (tuplas de índices de vértices).

- D. Uma lista de arestas com ponteiros para faces adjacentes.
---
### Na estrutura half-edge (DCEL), cada aresta é representada por duas half-edges gêmeas. Quais informações cada half-edge armazena?

- A. Apenas a posição 3D dos dois extremos da aresta.

- B. Referências para o vértice de origem, a gêmea (twin), a próxima (next), a anterior (prev) e a face à sua esquerda.

- C. A normal da face e a cor do vértice.

- D. O comprimento da aresta e o ângulo com a face vizinha.
---
### Na estrutura half-edge, como se percorre o "leque" (fan) de faces ao redor de um vértice?

- A. Usando `next` repetidamente.

- B. Usando `twin.next` repetidamente a partir de uma half-edge com origem no vértice.

- C. Percorrendo todas as faces da malha e verificando quais contêm o vértice.

- D. Usando `prev.twin` alternado com `next.twin`.
---
### Os Operadores de Euler garantem que as operações de edição em malhas B-Rep preservem qual propriedade fundamental?

- A. Que a malha tenha apenas faces triangulares.

- B. Que a malha permaneça topologicamente válida, satisfazendo a fórmula de Euler-Poincaré.

- C. Que todas as normais apontem para o interior do objeto.

- D. Que o número de vértices nunca diminua.
---
### Na subdivisão de Catmull-Clark, quais são os dois tipos de novos pontos criados?

- A. Pontos de vértice e pontos de normal.

- B. Pontos de face (centroide da face) e pontos de aresta (média dos extremos e faces adjacentes).

- C. Pontos médios de arestas e pontos aleatórios no interior das faces.

- D. Pontos de textura e pontos de iluminação.
---
### Qual é a fórmula para reposicionar um vértice antigo de valência $n$ na subdivisão de Catmull-Clark?

- A. $\mathbf{v'} = \frac{\mathbf{v}}{n}$

- B. $\mathbf{v'} = \frac{\mathbf{F} + 2\mathbf{R} + (n-3)\,\mathbf{v}}{n}$, onde $\mathbf{F}$ é a média dos pontos de face vizinhos e $\mathbf{R}$ a média dos pontos médios das arestas.

- C. $\mathbf{v'} = \frac{\mathbf{v} + \mathbf{F}}{2}$

- D. $\mathbf{v'} = n \cdot \mathbf{v} - \mathbf{F}$
---
### A subdivisão de Catmull-Clark converge para qual tipo de superfície nos vértices regulares (valência 4)?

- A. Superfície de Bézier bicúbica ($C^\infty$).

- B. B-spline bicúbica ($C^2$).

- C. B-spline biquadrática ($C^1$).

- D. Superfície planar ($C^0$).
---
### A subdivisão de Doo-Sabin generaliza qual tipo de B-spline?

- A. B-spline bicúbica.

- B. B-spline biquadrática.

- C. B-spline linear.

- D. NURBS de grau 5.
---
### Na subdivisão de Loop, como é determinado o novo vértice de aresta?

- A. Pela média simples dos dois extremos da aresta.

- B. Por $\tfrac{3}{8}$ de cada extremo da aresta mais $\tfrac{1}{8}$ de cada vértice oposto.

- C. Pelo centroide de todos os vértices do triângulo.

- D. Pela projeção do ponto médio da aresta na normal da face.
---
### A subdivisão de Loop é projetada especificamente para qual tipo de malha?

- A. Malhas quadrangulares.

- B. Malhas hexaédricas.

- C. Malhas triangulares.

- D. Malhas mistas (triângulos e quadriláteros).
---
### Qual a diferença entre malhas hexaédricas e malhas quadrangulares?

- A. São a mesma coisa, apenas com nomes diferentes.

- B. Malhas hexaédricas são volumétricas (interior decomposto em hexaedros), enquanto quadrangulares são de superfície (faces são quadriláteros).

- C. Malhas quadrangulares têm mais vértices que hexaédricas.

- D. Malhas hexaédricas só existem em 2D.
---
### Na técnica de varredura (sweep), o que é "lofting"?

- A. A extrusão de um perfil ao longo de uma reta.

- B. A varredura com interpolação entre perfis diferentes ao longo de uma trajetória.

- C. A rotação de um perfil em torno de um eixo.

- D. A projeção de um perfil no plano $xy$.
---
### Para a iluminação de malhas, por que normais por vértice são preferíveis a normais por face?

- A. Normais por vértice são mais fáceis de calcular que normais por face.

- B. Normais por face dão aspecto "facetado" (cada face com cor chapada), enquanto normais por vértice permitem sombreamento suave.

- C. Normais por face não podem ser usadas com o modelo de Phong.

- D. Normais por vértice ocupam menos memória.
---
### O que é a técnica de "auto-smooth" para normais de malha?

- A. Uma técnica que calcula normais por face e as aplica uniformemente a todos os vértices.

- B. Uma técnica que suaviza normais entre faces adjacentes, mas preserva arestas vivas onde o ângulo entre normais excede um limiar.

- C. Uma técnica que remove todas as arestas vivas de uma malha.

- D. Uma técnica que converte normais de vértice em normais de face automaticamente.
---
### Na imagem digital, qual a diferença entre resolução espacial e resolução de intensidade?

- A. A resolução espacial define o espaço de cores e a de intensidade define o número de pixels.

- B. A resolução espacial é o número de pixels ($M\times N$) e a de intensidade é o número de níveis discretos por canal.

- C. Ambas se referem ao número de pixels, mas em eixos diferentes.

- D. A resolução de intensidade é sempre maior que a espacial.
---
### Segundo o teorema de Nyquist-Shannon, qual deve ser a taxa de amostragem $f_s$ para reconstruir um sinal sem aliasing?

- A. $f_s = f_{\max}$

- B. $f_s > 2\, f_{\max}$

- C. $f_s < f_{\max}/2$

- D. $f_s = f_{\max}^2$
---
### O que é aliasing no contexto de processamento de imagens?

- A. A perda de cor quando a imagem é convertida para tons de cinza.

- B. O fenômeno onde frequências altas se "disfarçam" de frequências baixas quando a taxa de amostragem é insuficiente.

- C. A duplicação de pixels quando a imagem é ampliada.

- D. O efeito de borramento causado por um filtro gaussiano.
---
### Ao redimensionar uma imagem, qual é a diferença principal entre interpolação por vizinho mais próximo, bilinear e bicúbica?

- A. Vizinho mais próximo usa 1 pixel, bilinear usa 4 vizinhos e bicúbica usa 16 vizinhos; cada método produz resultados progressivamente mais suaves.

- B. Todas usam o mesmo número de vizinhos, mas com pesos diferentes.

- C. Vizinho mais próximo só funciona para ampliar, bilinear para reduzir e bicúbica para ambos.

- D. Bicúbica é a mais rápida e vizinho mais próximo a mais lenta.
---
### O que é "banding" e quando ele aparece?

- A. Faixas visíveis que aparecem em gradientes suaves quando o número de níveis de quantização é insuficiente.

- B. Listras horizontais causadas por falhas na leitura do sensor.

- C. Padrões de Moiré causados pela sobreposição de duas grades.

- D. Bordas duplas causadas por filtros de realce.
---
### Qual é o princípio central do dithering?

- A. Aumentar a resolução espacial da imagem duplicando cada pixel.

- B. Trocar resolução no espaço de cores por resolução espacial, simulando tons intermediários com padrões de poucas cores.

- C. Comprimir a imagem descartando pixels de baixa importância.

- D. Converter a imagem de RGB para tons de cinza.
---
### Na difusão de erro de Floyd-Steinberg, como o erro de quantização é distribuído?

- A. O erro é descartado após a quantização de cada pixel.

- B. O erro é espalhado igualmente para todos os pixels da imagem.

- C. O erro de cada pixel é distribuído para os vizinhos ainda não processados, com pesos $\tfrac{7}{16}$, $\tfrac{3}{16}$, $\tfrac{5}{16}$ e $\tfrac{1}{16}$.

- D. O erro é acumulado e aplicado apenas ao último pixel da imagem.
---
### Por que a difusão de erro (Floyd-Steinberg) não é adequada para implementação em um fragment shader?

- A. Porque requer texturas de alta resolução que excedem a memória da GPU.

- B. Porque é serial: cada pixel depende do erro propagado pelos vizinhos já processados, o que impede a execução paralela.

- C. Porque usa apenas aritmética de ponto flutuante de 64 bits.

- D. Porque precisa de acesso à posição do mouse em cada frame.
---
### O que é a equalização de histograma e qual é o seu objetivo?

- A. Converter a imagem para tons de cinza calculando a média dos canais RGB.

- B. Redistribuir as intensidades para obter um histograma aproximadamente uniforme, maximizando o contraste global.

- C. Eliminar pixels com intensidade zero para reduzir o tamanho do arquivo.

- D. Duplicar a faixa de intensidades para simular HDR.
---
### Na correção de gama $s = c\, r^{\gamma}$, qual é o efeito de usar $\gamma < 1$?

- A. A imagem fica mais escura, pois os valores são reduzidos.

- B. A imagem fica mais clara, realçando as sombras.

- C. A imagem perde todas as cores e se torna monocromática.

- D. A imagem sofre inversão de cores.
---
### Na convolução para filtragem espacial, o que acontece se a soma dos elementos do kernel $K$ for igual a 1?

- A. A imagem resultante fica invertida.

- B. O brilho médio da imagem se mantém.

- C. A imagem se torna completamente branca.

- D. A convolução se torna não-linear.
---
### Qual é o kernel do Laplaciano e para que ele é usado?

- A. $\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}$, usado para suavização.

- B. $\begin{bmatrix}0&-1&0\\-1&4&-1\\0&-1&0\end{bmatrix}$, usado para realce de bordas e detalhes.

- C. $\begin{bmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{bmatrix}$, usado para detecção de gradiente.

- D. $\begin{bmatrix}0&0&0\\0&1&0\\0&0&0\end{bmatrix}$, usado como filtro identidade.
---
### Quais são os cinco passos do detector de bordas de Canny?

- A. Quantização, dithering, limiarização, erosão, segmentação.

- B. Suavização gaussiana, cálculo do gradiente, supressão de não-máximos, duplo limiar e histerese.

- C. Transformada de Fourier, filtragem passa-alta, inversa da FFT, limiarização, morfologia.

- D. Erosão, dilatação, abertura, fechamento, gradiente morfológico.
---
### Qual a diferença entre o LoG (Laplaciano do Gaussiano) e o DoG (Diferença de Gaussianas)?

- A. LoG e DoG produzem resultados completamente diferentes e não têm relação entre si.

- B. O DoG aproxima o LoG subtraindo dois borramentos gaussianos com $\sigma$ diferentes, sendo mais barato computacionalmente.

- C. O LoG é um filtro passa-baixa, enquanto o DoG é um filtro passa-alta.

- D. O DoG é mais preciso que o LoG em todas as situações.
---
### No domínio da frequência, o que o Teorema da Convolução afirma?

- A. Que a convolução no espaço equivale a uma soma na frequência.

- B. Que a convolução no espaço equivale a uma multiplicação na frequência.

- C. Que a multiplicação no espaço equivale a uma convolução na frequência e vice-versa.

- D. Ambas B e C estão corretas.
---
### Para que tipo de ruído o filtro de mediana é mais eficaz que a suavização linear?

- A. Ruído gaussiano de baixa intensidade.

- B. Ruído "sal e pimenta" (pixels extremos isolados).

- C. Borramento por movimento (motion blur).

- D. Distorção de lente (barrel distortion).
---
### O que é o filtro bilateral e qual sua principal vantagem?

- A. Um filtro que aplica a média simples de todos os pixels da imagem.

- B. Uma média ponderada por proximidade espacial e de cor, que suaviza sem borrar bordas.

- C. Um filtro que duplica a resolução da imagem em ambos os eixos.

- D. Um filtro que converte a imagem de RGB para HSV.
---
### No método de Otsu para limiarização automática, qual critério é usado para escolher o limiar $t$?

- A. O limiar que minimiza o brilho médio da imagem.

- B. O limiar que maximiza a variância entre as duas classes do histograma.

- C. O limiar fixo de $t = 0.5$.

- D. O limiar que maximiza o número de pixels brancos.
---
### Na morfologia matemática, qual é o efeito da operação de abertura ($A \circ B$)?

- A. Engordar o contorno do objeto e preencher buracos.

- B. Remover pequenos objetos e ruído sem encolher significativamente o que sobra.

- C. Extrair o contorno do objeto.

- D. Inverter as cores da imagem binária.
---
### Qual é a relação entre erosão e dilatação na morfologia matemática?

- A. São operações idênticas aplicadas com elementos estruturantes diferentes.

- B. São operações duais: erosão no objeto equivale a dilatação no fundo, e vice-versa.

- C. Erosão é sempre aplicada antes da dilatação, nunca o inverso.

- D. Dilatação é uma versão mais rápida da erosão.
---
### O que é o gradiente morfológico ($A\oplus B - A\ominus B$) e qual é a sua utilidade?

- A. É a diferença entre a imagem dilatada e a erodida, extraindo o contorno do objeto.

- B. É a soma das operações de abertura e fechamento.

- C. É a derivada do histograma em relação à intensidade.

- D. É a taxa de variação do ruído na imagem ao longo do eixo $x$.
---
### Na segmentação por componentes conexas, qual é o procedimento após a binarização da imagem?

- A. Aplicar um filtro gaussiano para suavizar as bordas dos objetos.

- B. Agrupar pixels vizinhos do objeto e atribuir um rótulo a cada região isolada, permitindo contar e medir objetos.

- C. Converter a imagem para o espaço de frequência e aplicar um filtro passa-alta.

- D. Calcular o histograma e aplicar equalização para melhorar o contraste.
