:::center
# Computação Visual
## Aula 10 - Ray Tracing
:::
---
# Lançamento e traçado de raios
- Método conceitual para sintetizar imagens de cenas sintéticas
- Modela luz como uma semi-reta (raio)
- Principal operação: determinar ponto de interseção entre raio e objetos da cena
    - Visibilidade
        - Determinar interseção mais próxima do olho
    - Sombras
        - Determinar se luz é visível a partir da superfície
    - Modelo de iluminação global
        - Reflexão especular recursiva
        - Refração recursiva
        - (não modela iluminação difusa indireta)
---
# Lançamento de raios
:::col
- Ray Casting (Appel 1968)
- Raios lançados da câmera (olho)
- Para cada pixel:
    - Teste de interseção entre cada objeto da cena e raio
    - Pixel é pintado com cor do objeto mais próximo (do olho)
    - Sombras são calculadas lançando raios desde o ponto do objeto até a fonte de luz
:::
:::col
::img src="appel.png" width="90%"
:::
---
# Traçado de raios recursivo
:::col
- Paper seminal de Whitted (1980)
 - Estende as ideias de Appel
- _Backwards_ ray-tracing
    - Raios traçados no sentido contrário ao da luz
- Modelo de iluminação global recursivo
    - Reflexão e refração 
- Antialiasing
- Texturas
- Alta complexidade computacional
- Estendido e aperfeiçoado ao longo dos anos
:::
:::col
::img src="whited.jpeg" width="90%"
:::
---
# Exemplo
::img  src=rt_example.png height=55%
---
# Ideia geral
::img src=idea.png width=90%
---
# Tipos de raios
- Raio **primário** ou de visibilidade
  - Lançado do olho passando pelo centro do pixel
- Raio de detecção de **sombra**
  - Lançado do ponto atingido pelo raio primário em direção às fontes de luz
  - Ponto na sombra $\rightarrow$ raio atinge outro objeto primeiro
- Raio de **reflexão** ideal
  - Lançado na direção da reflexão do raio primário com relação à normal
- Raio de **refração** ideal
  - Lançado na direção dada pela lei de Snell:
  
  $$ \large  \eta_1 \sin \theta_1 = \eta_2 \sin \theta_2 $$
---
# Algoritmo $Trace(R)$

- Determinar o ponto $P$ de interseção do objeto mais próximo $X$
- Se não houver interseção, retornar cor de fundo
- Se $X$ tem componente **especular**
  - $C_{e} \leftarrow Trace (R_{e})$, onde $R_e$ é o raio de reflexão ideal 
- Se $X$ tem componente **transparente**
  - $C_t \leftarrow Trace (R_t)$, onde $R_t$ é o raio de refração ideal 
- Se $X$ tem componente **difusa**, para cada fonte $L_i$
  - Lançar um raio na direção de $L_i$
  - Se o raio atinge $L_i$
    - $C_{d_i} \leftarrow $ Iluminação difusa devida a $L_i$
- Computar componente ambiente $C_a$
- Retornar $C_e + C_t + C_a + \sum C_{d_i}$

---
# Computando o raio primário
::img src=computando_raio.svg height=80%
---
# Interseção com objeto implícito
- Objeto é dado por $f(x,y,z) = 0$
- Raio é dado por $R(t) = [R_x(t),R_y(t),R_z(t)]^T$
- Substituindo, temos $f(R(t)) = 0$
- Resolve-se para achar as raízes $t_i$
  - Queremos o menor $t_i > 0$
---
# Interseção com um plano
:::col ratio=60%
- $f (x,y,z) = ([x,y,z]^T - P) \cdot \vec n = 0$
- $R(t) = E + t \vec v = [E_x+t v_x, E_y+tv_y, E_z+tv_z]^T$
- Substituindo, temos:
  - $(E + t \vec v - P) \cdot \vec n = 0$
  - $(E - P) \cdot \vec n + t (\vec v \cdot \vec n) = 0$
  - $\Large t = \frac{(P - E) \cdot \vec n}{\vec v \cdot \vec n}$
:::
:::col ratio=30%
::img src=plane.svg
:::
---
:::col ratio=55%
# Interseção com esfera
- $f (x,y,z) = ||[x,y,z]^T - C||^2 - r^2 = 0$
- $R(t) = E + t \vec v = [E_x+t v_x, E_y+tv_y, E_z+tv_z]^T$
- Transladando a esfera para a origem, temos:
    - $f(x,y,z) = ||[x,y,z]^T||^2 - r^2 = 0$
    - $R(t) = E-C + t \vec v$
- Substituindo, temos:
  - $(E-C + t \vec v) \cdot (E-C + t \vec v) - r^2 = 0$

:::
:::col ratio=40%
::img src=esfera.svg width=50%
- Equação de 2o grau em $t$
  $ \large a t^2 + b t + c = 0 $
  onde
    - $a = \vec v \cdot \vec v$
    - $b = 2 (E-C) \cdot \vec v$
    - $c = (E-C) \cdot (E-C) - r^2$
:::
---
# Normais de objetos implícitos
- Precisamos da normal para o modelo de iluminação!
- Para um objeto dado por $f(x,y,z) = 0$, a direção normal é dada pelo _gradiente_ de $f$:
  $$ \large \vec n = \nabla f = \left[\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right]^T 
  $$
- Como precisamos de vetores unitários, usamos $\large\hat n = \frac {\vec n}{||n||}$
- Ex: Para um ponto $P=[x,y,z]^T$ na superfície de uma esfera centrada na origem
    - $\vec n = P$ 
---
# Interseção com malhas (triângulo)
- Seja $P$ o ponto de interseção com o plano que contém o triângulo $V_1, V_2, V_3$
- Observe que o triângulo está em 3D!
- Sabemos dizer se um triângulo contém um ponto dado em 2D
  - Basta checar se as coordenadas baricêntricas são positivas
- Para resolver o problema, projeta-se o ponto e o triângulo num dos planos coordenados $xy$, $xz$ ou $yz$.
- Escolhe-se o plano que dá o maior triângulo projetado
 - Se a normal do triângulo é $\vec n = [n_x, n_y, n_z]^T$
    - Se $|n_x|$ é o maior, projeta-se em $yz$
    - Se $|n_y|$ é o maior, projeta-se em $xz$
    - Se $|n_z|$ é o maior, projeta-se em $xy$
---
# Interseção com objetos transformados
- As rotinas de interseção normalmente lidam com objetos primitivos de tamanho, posição e orientação fixas (ex.: esfera de raio unitário na origem)
- Para obter objetos genéricos, usa-se transformações lineares afim
- Para computar a interseção de um raio $R$ com um objeto transformado $S = T S’$:
    - Leva-se o raio para o sistema de coordenadas da primitiva: $R’ = T^{–1} R$
    - Computa-se o ponto $P’$ resultante da interseção $R’ \times S’$
    - O ponto de interseção é trazido de volta ao sistema de coordenadas do mundo: $P = T P’$
---
:::center
::img src=raio_transformado.svg width=85%
:::
---
# Estruturas de indexação espacial
- Usadas para acelerar o processo de interseção
    - Uma malha pode ter milhares de triângulos. 
    - Uma cena pode ter milhares de objetos.
- Estruturas comuns:
    - Grades (grids)
    - Árvores binárias de espaço particionado (BSP)
    - Octrees
    - K-d trees
    - BVH (Bounding Volume Hierarchy)
--- 
# Usando uma estrutura de indexação espacial
:::col
- A estrutura é construida uma única vez para cenas / objetos estáticos
- Cada célula/partição da estrutura contém um pequeno número de objetos / triângulos
- Algoritmo visita células intersectadas pelo raio em ordem de distância do observador
- Para cada célula, testa-se a interseção do raio com os objetos / triângulos contidos nela
 - Se não há interseção com nenhum, visita-se a próxima célula
- O processo termina com uma interseção ou até todas as células terem sido visitadas
:::
:::col
::img src=estruturas.svg
:::
---
# O uso de volumes envolventes
- Antes de testar o raio contra o objeto, testa-se contra seu volume envolvente
 - Se não há interseção com o volume envolvente, não há interseção com o objeto
 - Caso contrário, o teste contra o objeto é feito
:: img src=bv.png width=70%
---
# _Bounding Volume Hierarchies_
- Conjugam estruturas de indexação e volumes envolventes
:: img src=bvh.png width=70%
