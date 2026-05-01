### Qual foi a principal inovação do sistema Sketchpad de Ivan Sutherland em 1963 para a computação visual?

- A. A introdução da interação direta com a tela através de uma caneta óptica (light pen).

- B. A criação da primeira cena 100% gerada por computador no cinema.

- C. O desenvolvimento do primeiro modelo 3D matemático complexo, o Bule de Utah.

- D. A primeira implementação do algoritmo de Ray Tracing recursivo.
---
### Diferencie as técnicas de sombreamento propostas por Gouraud (1971) e Phong (1973).

- A. Gouraud utiliza modelos de iluminação global, enquanto Phong utiliza modelos de iluminação local.

- B. Ambos utilizam o mesmo modelo matemático, mas Gouraud foca em transparências e Phong em reflexões.

- C. Phong criou a interpolação de cores, enquanto Gouraud introduziu o conceito de Ray Casting.

- D. Gouraud interpola cores entre vértices, enquanto Phong interpola as normais para calcular a iluminação local.
---
### Qual a importância da 'Equação de Renderização' publicada por James Kajiya em 1986?

- A. Definiu matematicamente as curvas de Bézier usadas no Bule de Utah.

- B. Ela unificou diversos modelos de iluminação em uma formulação integral, servindo de base para o Path Tracing moderno.

- C. Introduziu pela primeira vez o conceito de unidades de processamento gráfico (GPU).

- D. Permitiu a criação do primeiro longa-metragem totalmente animado, Toy Story.
---
### Na Geometria Afim, qual condição deve ser satisfeita para que uma combinação linear de pontos $Q=\sum_{i=1}^{n}\alpha_i P_i$ seja considerada uma operação legal (ponto resultante)?

- A. Todos os coeficientes $\alpha_i$  devem ser positivos e menores que 1.
- B. Os pontos $P_i$ devem ser linearmente independentes entre si.
- C. A soma dos quadrados dos coeficientes deve ser igual a 1.
- D. A soma dos coeficientes deve ser igual a 1, ou seja, $\sum \alpha_i = 1$

---
### Como se define uma 'Combinação Convexa' de um conjunto de pontos?

- A. É a média aritmética simples das coordenadas de todos os pontos envolvidos.

- B. É qualquer soma de vetores cujo resultado é um vetor unitário.

- C. É uma combinação afim onde todos os coeficientes $\alpha_i$  são não-negativos.

- D. É uma operação que resulta em um ponto ideal no infinito.
---
### Utilizando coordenadas baricêntricas, um ponto Q está localizado estritamente dentro de um triângulo $P_1 P_2 P_3$  se:

- A. As coordenadas homogêneas do ponto tiverem o valor $w=0$.

- B. O produto escalar entre os vetores posição for nulo.

- C. $\alpha_1+\alpha_2+\alpha_3=1$ e todos os $α_i >0$.

- D. A soma das áreas dos subtriângulos formados por $Q$ e os vértices do triângulo original for maior que a área do triângulo original.
---
### Qual é a aplicação do produto escalar (dot product) para determinar o ângulo $\theta$ entre dois vetores $u$ e $v$?

- A. $\theta= u \cdot v - || u || || v ||$

- B. $\cos \theta= \frac{||u|| ||v||}{u\cdot v }$

- C. $\cos \theta = \frac{u\cdot v }{||u|| ||v||}$ 

- D. $\sin \theta = \frac{u\cdot v }{||u|| ||v||}$ 
---
### No sistema de coordenadas homogêneas, como diferenciamos a representação de um ponto de um vetor?

- A. Um ponto possui a última coordenada (coordenada w) igual a 1, enquanto um vetor possui a coordenada w igual a 0.

- B. A norma de um ponto deve ser 1, enquanto a de um vetor pode ser qualquer valor escalar.

- C. Pontos são sempre positivos, enquanto vetores podem ter componentes negativas.

- D. Vetores são representados por matrizes linha e pontos por matrizes coluna.
---
### Seja um ponto $P_A$ no sistema de coordenadas $A$. Qual a fórmula correta para encontrar suas coordenadas $P_B$ no sistema B, dada a matriz de mudança de base $B_A$ (colunas de $B$ expressas em $A$)?

- A. $P_B = B_A^{-1} P_A$

- B. $P_B = B_A + P_A$

- C. $P_B = P_A^T B_A$

- D. $P_B = B_A P_A$

---
### Qual é a estrutura da matriz de transformação de translação bidimensional $T$ em coordenadas homogêneas para um deslocamento $(dx,dy)$? 
:::col
- A. $\left[    \begin{array}{ccc}     dx & 0 & 0 \\     0 & dy & 0 \\     0 & 0 & 1 \\     \end{array}     \right]$

- B. $\left[ \begin{array}{ccc}    \cos dx & \sin dx & 0 \\    -\sin dy & \cos dy & 0 \\      0 & 0 &1    \end{array}    \right]$
:::
:::col
 ​- C. $\left[    \begin{array}{ccc}   1 & 0 & dx \\   0 & 1 & dy \\    0 & 0 &1    \end{array}    \right]$ 

​ - D. $\left[    \begin{array}{ccc}   1 & 0 & -dx \\   0 & 1 & -dy \\    0 & 0 &1    \end{array}    \right]$ 
:::
---
### Dado que $R(\theta, u)$ é uma matriz de rotação de ângulo $theta$ em torno do eixo $u$, e $T(v)$ é uma matriz de translação pelo vetor $v$, como podemos realizar a rotação de um objeto ao redor de um ponto arbitrário $C$? 
- A. $T(C)\times R(\theta, u) \times T(-C)$
- B. $R(\theta, u)\times T(C)\times T(-C)$
- C. $R(\theta, u)\times T(C)\times T(-C)$
- D. $T(-C)\times R(\theta, u)\times T(C)$
---
### Em p5.js, as instruções `push()` e `pop()` servem para
- A. Salvar e restaurar o frame corrente
- B. Salvar e restaurar matrizes de transformação
- C. Realizar operações aritméticas em notação polonesa reversa
- D. Resetar todas as variáveis do sketch
---
### Na geometria afim, não é possível realizar quais operações da geometria euclidiana?
- A. Adição de vetores
- B. Medir comprimento de vetores
- C. Transformações lineares
- D. Translações
---
### O que caracteriza a Geometria Projetiva em comparação com a Geometria Afim?

- A. A capacidade de realizar apenas translações e rotações simples.

- B. O uso exclusivo de escalares inteiros para representação de coordenadas.

- C. A inclusão de pontos 'ideais' no infinito, essencial para o cálculo de projeções perspectivas.

- D. A introdução da noção de ângulos e distâncias métricas.
---
### Qual foi o impacto do lançamento da NVIDIA GeForce 256 em 1999 para o campo da computação visual?

- A. Estabeleceu o padrão de modelos 3D icônicos como o Bule de Utah.

- B. Foi a primeira placa a suportar Ray Tracing em tempo real através de RT Cores.

- C. Permitiu a execução de shaders pela primeira vez em um navegador web.

- D. Introduziu o termo GPU e forneceu hardware dedicado para Transformação e Iluminação (T&L).
---
### Como é calculada a projeção ortogonal de um vetor $\vec u$ sobre um vetor unitário $\hat v$?

- A. $\vec{u}_{||} = \vec u \cdot \hat v$

- B. $\vec{u}_{||} = (\vec u + \hat v) \cdot \hat v$

- C. $\vec{u}_{||} = (\vec u \cos \hat v) \hat v$

- D. $\vec{u}_{||}= (\vec u \cdot \hat v) \hat v$
---
### Considere a matriz de cisalhamento (shear) em $x$: $M= \left[    \begin{array}{ccc}1 & \tan \theta & 0 \\0 & 1 & 0 \\0 & 0 & 1 \end{array}\right].$ O que acontece com um ponto $[x,y,1]^T$ ao ser transformado por $M$?

- A. O ponto é transladado em $x$ por uma distância fixa igual a $\tan \theta$. 

- B. O objeto sofre uma escala uniforme em ambos os eixos baseada em $\tan \theta$.

- C. O ponto é rotacionado em torno da origem por um ângulo $\theta$.

- D. A nova coordenada $x'$ torna-se $x+y \tan \theta$, enquanto $y$ permanece inalterada.
---
### Qual a principal diferença técnica entre WebGL e o novo padrão WebGPU?

- A. O WebGL não suporta programação com shaders, dependendo apenas de funções fixas.

- B. WebGPU é projetado para computação gráfica de alta performance, oferecendo acesso mais direto ao hardware moderno e suporte a Compute Shaders.

- C. WebGPU é uma biblioteca JavaScript escrita em cima do WebGL para facilitar o uso de shaders.

- D. WebGL permite apenas desenhos em 2D, enquanto WebGPU introduz o suporte a 3D no navegador.
---
### Na Geometria Afim, a operação $P−Q= v$  representa:

- A. A criação de um novo ponto médio entre $P$ e $Q$.

- B. A distância euclidiana escalar entre os dois pontos.

- C. A obtenção de um vetor livre que representa o deslocamento de $Q$ para $P$.

- D. Uma operação ilegal, pois não se pode subtrair pontos diretamente.
---
### O que define um conjunto de vetores $\{u_1, u_2 \cdots u_d\}$ como uma 'Base' de um espaço de dimensão $d$?

- A. O produto escalar entre qualquer par de vetores deve ser zero.

- B. Todos os vetores devem ter comprimento unitário.

- C. Eles devem ser linearmente independentes.

- D. Eles devem estar alinhados aos eixos cartesianos X,Y,Z, etc.
---
### Qual das seguintes representações de cor em p5.js define uma cor vermelha com 50% de transparência?

- A. `color('#FF000050')`

- B. `color(255, 0, 0, 127)`

- C. `color(255, 0, 0, 0.5)`

- D. `color(127, 0, 0)`
---
### A arquitetura das GPUs modernamente é descrita como SIMD (Single Instruction, Multiple Data). No contexto do processamento de fragmentos, o que isso implica fundamentalmente?

- A. Cada processador da GPU executa uma instrução diferente para o mesmo dado de pixel.

- B. O pipeline gráfico é desativado para permitir que a CPU controle cada thread individualmente.

- C. A GPU processa um pixel por vez de forma sequencial para evitar conflitos de memória.

- D. A GPU executa a mesma instrução de um shader simultaneamente em múltiplos pixels/primitivas.
---
### Ao utilizar o p5.js no modo `WEBGL`, qual é a principal diferença de desempenho e gerenciamento de memória entre chamar `box()` diretamente e utilizar um objeto `p5.Geometry`?

- A. O `p5.Geometry` armazena os dados em buffers na memória da GPU, reduzindo o gargalo de transferência CPU-GPU a cada quadro.

- B. O `p5.Geometry` consome menos memória RAM total, pois não requer buffers de transformação.

- C. Primitivas como `box()` são processadas na CPU, enquanto `p5.Geometry` é processado na GPU.

- D. A função `model()` usada para desenhar geometrias é mais lenta que as primitivas básicas por exigir cálculos extras de iluminação.
---
### Dada a Fórmula de Rodrigues para rotação em torno de um eixo arbitrário unitário $\hat u$, qual termo representa a componente do vetor original que permanece inalterada pela rotação?

- A. $\hat u (\hat u ⋅ v)$

- B. $v \cos \theta$

- C. $(\hat u × v) \sin \theta$

- D. $\hat u (\hat u ⋅ v)(1 - \cos \theta)$


---
### Qual operador vetorial é utilizado na Fórmula de Rodrigues para isolar a componente ortogonal (perpendicular) do vetor $v$ em relação ao eixo de rotação $\hat u$?

- A. Produto escalar $(\hat u \cdot v)$

- B. Produto vetorial $(\hat u \times v)$

- C. Módulo (magnitude) $|v|$

- D. Cosseno da projeção $\cos \theta$

---
### O operador de orientação em 3D, $o(A,B,C,D)$, é definido pelo sinal do determinante de uma matriz 4×4. O que significa quando esse determinante é exatamente zero?

- A. O ponto D está localizado na origem do sistema de coordenadas.
- B. Os pontos formam um tetraedro regular.
- C. Os quatro pontos são coplanares.
- D. A matriz de transformação é uma translação pura.
---
### No pipeline de projeção, qual é o objetivo fundamental das Coordenadas Normalizadas de Dispositivo (NDC)?

- A. Garantir que todos os objetos 3D sejam convertidos em círculos perfeitos antes da rasterização.

- B. Converter cores RGB em coordenadas espaciais para o processamento de shaders.

- C. Eliminar a necessidade de uma matriz ModelView no processo de renderização.

- D. Abstrair a resolução e proporção da tela, mapeando o volume de visualização para um cubo unitário de −1 a 1.
---
### Na projeção perspectiva, o cálculo final das coordenadas de tela envolve a divisão por $w$. No p5.js e WebGL, de onde vem o valor de $w$ que causa o efeito de encurtamento perspectivo?

- A. Ele é um valor constante definido pelo programador através da função `pixelDensity()`.

- B. Ele é calculado pelo fragment shader comparando a distância entre dois vértices adjacentes.

- C. O valor de $w$ é sempre 1, e a distorção é feita por uma escala linear simples.

- D. Ele é derivado da coordenada $−z$ do espaço de câmera através de um termo na quarta linha da matriz de projeção.
---
### Qual transformação geométrica fundamental é responsável por mapear o volume de visualização (View Frustum) para o cubo unitário das Coordenadas Normalizadas de Dispositivo (NDC)?

- A. Transformação de Modelagem (Model Transformation)
- B. Transformação de Câmera (View Transformation)
- C. Transformação de Projeção (Projection Transformation)
- D. Transformação de Rasterização (Rasterization Transformation)
---
### Qual é a principal limitação técnica da projeção ortográfica (`ortho()`) em comparação com a perspectiva no contexto de realismo visual?

- A. Não é possível aplicar texturas ou cores em objetos projetados ortograficamente.

- B. Objetos mantêm o mesmo tamanho na tela independentemente da distância em relação à câmera.

- C. O ângulo de visão (fovy) torna-se infinito, causando distorção esférica.

- D. A projeção ortográfica não suporta o uso de um Depth Buffer (Z-buffer).
---
### Em GLSL, qual é a diferença fundamental entre as classes de variáveis `uniform` e `attribute`?

- A. Attributes são interpolados automaticamente entre vértices, enquanto uniforms não são.

- B. Uniforms são variáveis de leitura e escrita, enquanto attributes são apenas para leitura.

- C. Uniforms só existem no fragment shader e attributes só no vertex shader.

- D. Uniforms são constantes para todo o objeto em uma chamada de desenho, enquanto attributes variam por vértice.
---
### Considere o seguinte trecho de código GLSL: `vec4 v = vec4(1.0, 2.0, 3.0, 4.0); vec2 sub = v.zy;`. Qual será o valor armazenado em `sub`?

- A. O valor será `vec2(3.0, 4.0)`, pois 'z' e 'y' são os últimos componentes.

- B. O valor será `vec2(1.0, 2.0)`, pois ele pega os dois primeiros componentes por padrão.

- C. O código resultará em um erro de compilação, pois não se pode extrair `vec2` de `vec4`.

- D. A técnica de swizzling resultará em `vec2(3.0, 2.0)`.
---
### Em um Signed Distance Field (SDF), o que define matematicamente a superfície do objeto sendo modelado?

- A. Onde o gradiente da função é igual a zero.

- B. A interseção da função com o plano $z = −1$.

- C. Apenas os pontos onde a função retorna valores negativos.

- D. O conjunto de pontos onde a função $f(x,y,z)=0$.
---
### No Modelo de Iluminação de Phong, por que a componente especular depende da posição da câmera (vetor $e$), enquanto a componente difusa não?

- A. O modelo de Phong assume que a câmera emite sua própria luz ambiente.

- B. A componente difusa usa a posição da câmera para calcular o cosseno do ângulo de incidência.

- C. A reflexão especular modela o brilho direcional que só atinge o olho se estiver alinhado ao raio de reflexão ideal.

- D. A componente especular é calculada na CPU antes de enviar os dados para o shader.
---
### Qual é o efeito de aumentar significativamente o valor do parâmetro `shininess` (expoente α) no cálculo da reflexão especular de Phong?

- A. A cor do objeto muda de sua cor difusa para a cor da luz incidente de forma global.

- B. A intensidade total da luz refletida aumenta, tornando o objeto mais claro em todas as direções.

- C. O highlight especular torna-se menor e mais concentrado, simulando uma superfície mais polida.

- D. O objeto passa a emitir luz própria, ignorando as fontes de luz pontuais.
---
### Ao calcular o vetor de reflexão ideal $\vec r$ para o modelo de Phong, qual é a fórmula correta utilizando o vetor da luz $\vec \ell$ e a normal $\vec n$ (ambos unitários)?

- A. $\vec r = \vec \ell \times \vec n$ 
- B. $\vec r = \frac {\vec \ell \cdot \vec n} {||\vec \ell||}$
- C. $\vec r = 2(\vec \ell \cdot \vec n)\vec n - \vec \ell$ 
- D. $\vec r = \frac{\vec \ell + \vec n}{2}$
--- 
### Sobre a atenuação da luz no modelo de Phong, o parâmetro `lightFalloff(a0, a1, a2)` utiliza uma fórmula quadrática. O que acontece com a intensidade da luz se apenas o termo `a2` for maior que zero e a distância $d_\ell $ dobrar?

- A. A luz manterá a mesma intensidade, pois `a2`só afeta a componente ambiente.

- B. A intensidade da luz cairá pela metade (1/2).

- C. A luz se tornará quatro vezes mais intensa devido ao expoente positivo.

- D. A intensidade da luz será reduzida a um quarto (1/4) do valor original.
--- 
### Qual é a função do `varying` em um programa de shader WebGL?

- A. Transmitir dados do vertex shader para o fragment shader com interpolação automática baseada em coordenadas baricêntricas.

- B. Declarar constantes que não podem ser alteradas em nenhum estágio do pipeline.

- C. Permitir que o usuário altere variáveis em tempo real através da interface do mouse.

- D. Armazenar a posição final do vértice no sistema NDC.
---
### Ao simular uma 'luz amarela' incidindo sobre um material com 'cor azul' no modelo de Phong, qual será a cor resultante da componente difusa (assumindo coeficientes padrão)?

-  A. Preto (ou ausência de luz).

- B. Verde, pois é a mistura de azul com amarelo.

- C. Cinza médio, representando a neutralização das cores primárias.

- D. Branco, devido à soma das frequências espectrais.
---
### A função `orbitControl()` do p5.js manipula internamente qual aspecto da cena?

- A. A matriz de Projeção, alterando o campo de visão (fovy).

- B. O shader de fragmento, alterando a forma como a iluminação é calculada.

- C. A matriz ModelView, alterando a posição e orientação virtual da câmera em relação à origem.

- D. A geometria bruta dos objetos, rotacionando seus vértices na memória da GPU.
---
### Qual é a principal diferença entre uma fonte de luz `directionalLight` e uma `pointLight` no p5.js?

- A. A luz direcional projeta sombras automáticas, enquanto a pontual não.

- B. A luz direcional tem raios paralelos e não sofre atenuação por distância, enquanto a pontual emite em todas as direções a partir de um local fixo.

- C. A luz pontual requer o uso de shaders customizados, enquanto a direcional é parte do pipeline fixo.

- D. Luzes direcionais só podem ser brancas, enquanto luzes pontuais aceitam qualquer cor RGB.
---
### No GLSL, o que o operador swizzling `v.rgba` faz se `v` for um `vec4` que armazena uma cor?

- A. Ele converte a cor de RGB para o espaço de cor CMYK.

- B. Ele normaliza os valores dos componentes para que a soma seja 1.0.

- C. Ele retorna o próprio vetor `v`, sendo apenas uma forma semântica de acessar os componentes x,y,z,w.

- D. Ele inverte a ordem dos componentes, colocando o canal Alpha no início.
---
### Entre as APIs gráficas citadas, quais são classificadas como de baixo nível, visando maior controle sobre a arquitetura da GPU?

- A. OpenGL e WebGL.

- B. DirectX 11 e OpenGL ES.

- C. Three.js e P5.js.

- D. Vulkan, WebGPU, DirectX 12 e Metal.
---
### O que acontece com a iluminação de um objeto se o ângulo entre o vetor normal $\vec n$ e o vetor da luz $\vec \ell$  for maior que 90 graus (ou seja, $\vec n \cdot \vec \ell < 0$)?

- A. A superfície fica com brilho especular máximo.

- B. O objeto torna-se transparente.

- C. A cor do objeto é invertida.

- D. A intensidade da luz difusa torna-se nula.

---
### No algoritmo de Ray Marching, por que a utilização de uma SDF (Signed Distance Function) permite passos de tamanho variável em vez de um tamanho de passo fixo?

- A. Porque a SDF fornece a distância mínima garantida até o objeto mais próximo em qualquer direção.

- B. Porque a SDF converte a cena em uma malha de triângulos de alta resolução antes do traçado.

- C. Porque a SDF elimina a necessidade de testar limites de iteração ou distâncias máximas.

- D. Porque a SDF calcula automaticamente a interseção exata usando raízes algébricas de polinômios.
---
### Dadas duas SDFs, $A$ e $B$, qual operação matemática é necessária para representar a interseção geométrica $A \cap B$ no espaço?

- A. $\min(A, B)$

- B. $A + B$

- C. $\max(A, -B)$

- D. $\max(A, B)$
---
### Ao aplicar uma escala uniforme $s$ a um objeto representado por uma SDF, qual ajuste deve ser feito no cálculo da distância para manter a integridade da função?

- A. Subtrair $s$ de todos os valores retornados pela SDF.

- B. Aplicar a escala $s$ apenas às coordenadas $x$ e $y$ no fragment shader.

- C. Dividir a distância final por $s$ após avaliar o ponto $P$ original.

- D. Multiplicar a distância resultante da SDF avaliada em $P/s$ pelo fator de escala $s$.
---
### Como a normal de uma superfície é tipicamente aproximada em Ray Marching quando não há uma solução analítica para o gradiente?

- A. Utilizando a média ponderada das normais dos triângulos adjacentes ao ponto de impacto.

- B. Pela inversão do vetor de direção do raio primário no ponto de interseção.

- C. Usando diferenças finitas para estimar as derivadas parciais: ∇f≈[f(x)−f(x−ϵ),…].

- D. Calculando o produto vetorial entre o raio de visão e o vetor 'up' da câmera.
---
### No Ray Tracing recursivo de Whitted, o que define um 'raio de sombra'?

- A. O raio primário que não consegue encontrar nenhuma interseção na cena.

- B. Um raio gerado pela lei de Snell para simular a passagem da luz por meios transparentes.

- C. Um raio que viaja no sentido oposto ao raio de reflexão para escurecer a cor final.

- D. Um raio lançado do ponto de interseção em direção a cada fonte de luz para verificar oclusões.

---
### Ao transformar um objeto no Ray Tracing, por que a normal original $\vec n$  deve ser multiplicada pela transposta da inversa da matriz de transformação $(T^{-1})^\top$ ?

- A. Para garantir que a normal permaneça perpendicular aos vetores tangentes da superfície após distorções de escala não uniforme.

- B. Porque as normais em Ray Tracing devem sempre apontar para a origem do sistema de coordenadas.

- C. Porque a matriz de transformação T só pode ser aplicada a pontos, nunca a vetores de direção.

- D. Para converter a normal do sistema de coordenadas da câmera para o sistema de coordenadas da tela.
---
### Qual é o principal desafio ao calcular a interseção de um raio com um triângulo em um espaço tridimensional?

- A. Resolver uma equação de quarto grau para encontrar as raízes de $t$.

- B. Determinar se o ponto de interseção no plano infinito está contido dentro dos limites dos três vértices.

- C. A impossibilidade de usar o produto escalar para calcular a distância ao longo do raio.

- D. Garantir que o triângulo seja projetado exatamente no plano $xy$ antes de qualquer cálculo.
---
### Em relação à modelagem CSG (Constructive Solid Geometry), como o Ray Tracing lida com a operação de diferença entre dois objetos?

- A. Encontrando todos os intervalos de interseção e combinando-os de acordo com a lógica de conjuntos.

- B. Subtraindo os valores de cor dos pixels resultantes de cada objeto individualmente.

- C. Ignorando as normais do segundo objeto para criar um buraco visual.

- D. Usando apenas o ponto de interseção mais próximo de qualquer um dos dois objetos.
---
### O que caracteriza a estrutura de aceleração conhecida como BVH (Bounding Volume Hierarchy)?

- A. Uma organização hierárquica onde volumes envolventes maiores contêm volumes menores e a geometria real.

- B. Uma grade uniforme que subdivide o espaço em cubos de tamanho idêntico chamados voxels.

- C. Um método que substitui todos os objetos da cena por esferas perfeitas para simplificar as equações.

- D. Uma técnica que processa apenas os objetos que estão fora do campo de visão da câmera.
---
### No contexto de texturização, o termo MIP (Multum in Parvo) refere-se à técnica de Mipmapping. Qual é a sua finalidade principal?

- A. Reduzir artefatos de aliasing ao selecionar versões pré-filtradas da textura com base na distância do objeto.

- B. Permitir que uma única textura seja aplicada a múltiplos objetos sem repetição de padrões.

- C. Aumentar a resolução da textura dinamicamente quando o observador se aproxima muito da superfície.

- D. Substituir o mapeamento UV por um sistema baseado em coordenadas polares automáticas.

---
### Qual é a principal diferença conceitual entre um Bump Map e um Normal Map?

- A. O Bump Map altera a geometria real da malha, enquanto o Normal Map é apenas um efeito de luz.

- B. Bump Maps são mais eficientes computacionalmente por não utilizarem o fragment shader.

- C. Normal Maps só podem ser aplicados a superfícies planas, enquanto Bump Maps funcionam em esferas.

- D. O Bump Map armazena alturas (escalares), enquanto o Normal Map armazena direções de vetores (RGB).

---
### Na implementação de Bump Mapping em Shaders, por que os vetores Tangente (T) e Bitangente (B) são necessários?

- A. Para calcular a refração da luz conforme ela entra em superfícies metálicas.

- B. Para estabelecer um sistema de coordenadas local na superfície onde o gradiente da textura possa ser aplicado.

- C. Para converter as cores da textura de sRGB para o espaço linear de cores.

- D. Para substituir o vetor normal principal e simplificar o modelo de iluminação de Phong.

---
### No Ray Marching, o que acontece se o valor de $\epsilon$ (limite de proximidade) for definido como um número excessivamente pequeno?

- A. A cena ficará borrada devido ao excesso de amostras processadas por pixel.

- B. A iluminação global será desativada automaticamente para compensar o custo computacional.

- C. O número de iterações necessárias para convergir aumentará drasticamente, podendo causar 'acne' na superfície ou erros de precisão.

- D. O objeto desaparecerá da cena, pois a SDF nunca retornará um valor menor que $\epsilon$.
---
### Como o espelhamento de um objeto é implementado de forma eficiente em uma SDF sem duplicar a geometria?

- A. Invertendo o sinal da distância retornada pela SDF original.

- B. Aplicando a função valor absoluto `abs()` às coordenadas do ponto de amostragem antes de avaliar a SDF.

- C. Calculando a média entre a posição do ponto e a posição do centro do objeto.

- D. Multiplicando a direção do raio por −1 sempre que ele se aproximar de um plano.
---
### Qual é a função do parâmetro k em uma operação de 'Smooth Minimum' entre duas SDFs?

- A. Definir o número de amostras extras para o cálculo do gradiente da normal.

- B. Controlar o raio da zona de transição onde ocorre a mistura suave entre as superfícies.

- C. Determinar a distância de corte (far plane) para o traçado do raio.

- D. Ajustar o índice de refração para simular materiais translúcidos.
---
### No cálculo da interseção raio-esfera, o discriminante $\Delta = b^2 - 4ac$ da equação quadrática indica o quê?

- A. O número de pontos de interseção: se negativo, o raio não atinge a esfera.

- B. A cor final do pixel baseada na intensidade da luz ambiente.

- C. O ângulo de incidência entre o raio primário e o raio de sombra.

- D. A rugosidade da superfície para o modelo de iluminação especular.
---
### Qual é o objetivo de projetar um triângulo 3D em um dos planos coordenados (xy, xz ou yz) durante o teste de interseção?

- A. Reduzir o consumo de memória de vídeo ao descartar a coordenada z.

- B. Simplificar o teste de inclusão do ponto transformando-o em um problema 2D mais fácil de resolver.

- C. Garantir que as sombras projetadas sejam sempre perpendiculares ao chão.

- D. Permitir que o triângulo seja renderizado usando apenas o comando `line()` do p5.js.

---
### Ao utilizar um Cubemap para reflexões em Ray Marching, como é determinado o vetor para amostrar a textura do ambiente?

- A. Refletindo o vetor de visão em relação à normal da superfície no ponto de impacto.

- B. Usando as coordenadas UV do objeto para buscar o pixel correspondente na face 'front' do cubo.

- C. Projetando a posição 3D do ponto diretamente no plano da tela.

- D. Calculando a média entre o vetor 'up' do mundo e a direção da luz principal.
---
### O que acontece matematicamente quando utilizamos o operador de módulo `mod()` nas coordenadas de entrada de uma SDF?

- A. O espaço é subdividido em células repetitivas, criando infinitas cópias do objeto original.

- B. A superfície do objeto torna-se transparente e permite a passagem de raios de refração.

- C. O objeto é cortado pela metade em todos os eixos onde o módulo foi aplicado.

- D. A distância calculada é normalizada entre −1 e 1 para evitar estouro de memória.
---
### No modelo de câmera utilizado em Ray Marching explicado em aula, qual é o papel do parâmetro `flen` (focal length)?

- A. Definir a distância máxima que um raio pode viajar antes de ser descartado.

- B. Controlar a intensidade da luz difusa que atinge o sensor da câmera.

- C. Determinar a espessura da superfície para cálculos de colisão com SDFs.

- D. Ajustar o campo de visão (Field of View), controlando o 'zoom' da cena.
---
### Qual das seguintes funções é comumente usada para a criação de texturas procedurais que pareçam naturais, como mármore ou nuvens?

- A. Distribuição de Poisson

- B. Operador de Bitwise AND

- C. Função Tangente

- D. Perlin Noise
---
### Por que o p5.js sugere o uso de `textureMode(NORMAL)` ao lidar com mapeamento de textura?

- A. Para que as coordenadas UV variem de 0 a 1, independentemente do tamanho em pixels da imagem.

- B. Para forçar a textura a se comportar como um Normal Map em todos os objetos.

- C. Para garantir que a textura não sofra distorções de perspectiva ao ser renderizada.

- D. Para desativar o cálculo de iluminação e mostrar a textura com brilho total.
---
### O que define o comportamento `textureWrap(MIRROR, MIRROR)` no p5.js?

- A. O objeto reflete o ambiente ao seu redor como se fosse um espelho metálico.

- B. A textura é repetida, mas cada repetição é invertida em relação à anterior.

- C. A imagem é esticada para cobrir todo o objeto, ignorando as coordenadas UV originais.

- D. A textura é aplicada apenas na parte interna de objetos transparentes.
---
### No cálculo de derivadas parciais dentro de um shader, para que servem as funções `dFdx` e `dFdy`?

- A. Para aumentar a taxa de quadros (FPS) ao pular o processamento de fragmentos idênticos.

- B. Para gerar números aleatórios baseados na posição do mouse.

- C. Para calcular a taxa de variação de um valor entre pixels vizinhos na tela.

- D. Para converter coordenadas 3D do mundo em coordenadas 2D da tela.
---
### Qual é a principal limitação do método 'Step Tracing' simples (passo fixo) comparado ao Ray Marching com SDF?

- A. Dependência obrigatória de uma GPU para realizar qualquer cálculo.

- B. Necessidade de converter todas as cores para tons de cinza antes do processamento.

- C. Incapacidade total de representar objetos com curvatura suave.

- D. Ineficiência computacional, pois exige muitos passos pequenos para evitar 'atravessar' objetos finos.
---
### Na representação paramétrica de uma esfera para texturização, as coordenadas u e v são derivadas de quais ângulos?

- A. Ângulos azimutal ($\theta$) e de inclinação ($\phi$).

- B. Ângulos internos de uma malha de triângulos.

- C. Ângulos de rotação do mouse (Arcball).

- D. Ângulos de reflexão e refração da luz.
---
### Por que o cálculo de sombras em Ray Tracing é considerado mais simples do que em algoritmos em espaço de imagem como Shadow Maps?

- A. Porque as sombras em Ray Tracing são sempre processadas em baixa resolução.

- B. Porque basta lançar um raio adicional; se houver qualquer interseção antes da luz, o ponto está em sombra.

- C. Porque ele utiliza apenas a cor preta sólida, ignorando a luz ambiente.

- D. Porque Ray Tracing não precisa de fontes de luz reais para gerar sombras.
---
### O que define um mapeamento de textura como 'Conformal' ao deformar uma malha cortada?

- A. A preservação dos ângulos originais dos triângulos ao serem mapeados no plano.

- B. A exigência de que a malha seja composta apenas por triângulos equiláteros.

- C. O uso obrigatório de apenas três cores na paleta da textura.

- D. A garantia de que todas as áreas da textura tenham o mesmo brilho.

---
### No Ray Marching, ao implementar a técnica de 'Arcball', como é calculado o eixo de rotação da câmera?

- A. Pela diferença entre a posição atual do mouse e o centro da tela.

- B. Multiplicando a velocidade do mouse pela constante de gravidade simulada.

- C. Usando a componente z do vetor de visão no momento do clique.

- D. Através do produto vetorial entre os vetores que representam o início e o fim do arraste do mouse na esfera virtual.

---
### Em um shader de Ray Marching, qual é a utilidade prática de retornar um valor de 'material' junto com a distância da SDF?

- A. Substituir a necessidade de calcular as normais da superfície.

- B. Permitir que diferentes objetos na mesma cena tenham propriedades ópticas (como cor ou brilho) distintas.

- C. Aumentar a velocidade de convergência do raio ao atingir superfícies metálicas.

- D. Evitar que raios de sombra atravessem objetos transparentes.






















