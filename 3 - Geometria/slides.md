::: center
# Computação Visual
## Aula 3 - Geometria e Programação Geométrica
:::
---
# Motivação
- Posição, orientação e tamanho de objetos em 3D.
- Problemas de interseção.
- Construções geométricas.
- Sistemas de coordenadas.
- Iluminação.

---
# Tipos de Geometria
- **Afim**: Lida com objetos 'planos' mas não tem noção de distâncias (tamanho) e ângulos. Seus elementos são escalares (números reais), pontos (posição no espaço) e vetores livres (direção, sentido e magnitude).
- **Euclidiana**: É a Geometria Afim mais o produto escalar (ou produto interno), introduzindo a noção de distâncias, ângulo e orientação.
- **Projetiva**: Considera pontos 'ideais' no infinito e é usada para projeção perspectiva.

---
# Geometria Afim
3 elementos:
- Escalares → números reais
- Pontos → posição no espaço
- Vetores livres → direção, sentido e magnitude

**Importante:**
- Vetores e pontos em são ambos representados com $n$ escalares
- Mas não são “a mesma coisa”
---
# Operações da geometria afim
- Soma de vetores: $\vec{v} + \vec{u} = \vec{w}$
- Subtração de vetores: $\vec{v} - \vec{u} = \vec{w}$
- Multiplicação por escalar: $\lambda \vec{v} = \vec{w}$
- Adição de ponto e vetor: $P + \vec{v} = Q$
- Subtração de pontos: $P - Q = \vec{v}$
---
# Combinação afim
$$
Q = \alpha_1 P_1 + \alpha_2 P_2 + \cdots + \alpha_n P_n = \sum_{i=1}^n \alpha_i P_i
$$

Expressão ilegal! 
:::reveal
A menos que $\sum_{i=1}^n \alpha_i = 1 $. Pois nesse caso,

$$
Q = P_1 + \alpha_2 (P_2 - P_1) + \cdots + \alpha_n (P_n - P_1) = P_1 + \sum_{i=2}^n \alpha_i (P_i - P_1)
$$
:::
---
# Exemplos
:: image src="exemplosAfim.png" width="90%"
---
# Combinações convexas
São combinações afim onde todos os coeficientes são não-negativos
Conjunto com todas as combinações convexas de 
- 2 pontos não coincidentes → segmento de reta
- 3 pontos não colineares → triângulo
- 4 pontos não coplanares → tetraedro
- 4 pontos quaisquer → tetraedro, quadrilátero convexo, triângulo, segmento de reta ou ponto
- N pontos quaisquer → algum politopo convexo

---
# Coordenadas baricêntricas
:::col
Qualquer ponto $Q$ dentro de um triângulo $P_1 P_2 P_3$ pode ser escrito como uma combinação convexa de $P_1$, $P_2$ e $P_3$.

$$
Q = \alpha_1 P_1 + \alpha_2 P_2 + \alpha_3 P_3 = \sum_{i=1}^3 \alpha_i P_i
$$

Onde $\alpha_i = \frac{\text{area}(T_i)}{\text{area}(T)}$
:::
:::col
::image src="baricentricas.png" width="90%"
:::
---
# Geometria Euclidiana
Geometria Afim + produto escalar

$$
\vec{u} \cdot \vec{v} = \sum_{i=1}^n u_i v_i
$$

Propriedades:
- Comutatividade: $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$
- Distributividade: $\vec{u} \cdot (\vec{v} + \vec{w}) = \vec{u} \cdot \vec{v} + \vec{u} \cdot \vec{w}$
- Multiplicação por escalar: $(\lambda \vec{u}) \cdot \vec{v} = \lambda (\vec{u} \cdot \vec{v}) = \vec{u} \cdot (\lambda \vec{v})$
- Positividade: $\vec{u} \cdot \vec{u} \ge 0$
---
# Aplicações do produto escalar
- Comprimento de um vetor: $\Vert \vec{v} \Vert = \sqrt{\vec{v} \cdot \vec{v}}$
- Vetor normalizado: $\hat{v} = \frac{\vec{v}}{\Vert \vec{v} \Vert}$
- Distância entre dois pontos: $d(P, Q) = \Vert P - Q \Vert$
- Ângulo entre dois vetores: 
:::col
$$\cos \theta = \frac{\vec{u} \cdot \vec{v}}{\Vert \vec{u} \Vert \Vert \vec{v} \Vert} = \hat u \cdot \hat v$$
:::
:::col
::image src="angulo.png" width="50%"
:::
--- 
# Projeção Ortogonal
:::col
$$\vec{u_1} = (\vec u \cdot \hat v) \hat v = \frac{\vec u \cdot \vec v}{ \vec v \cdot \vec v } \vec v$$

$$\vec{u_2} = \vec u - \vec u_1$$
:::
:::col
::image src="projecao.png" width="100%"
:::
---
# Bases
:::col
Em $d$ dimensões, vetores ${\vec u_1, \cdots, \vec u_d}$ formam uma base se são _linearmente independentes_

Qualquer vetor $\vec v$ pode ser expresso como uma combinação linear dos vetores da base:

$$\vec v = \sum_{i=1}^d \alpha_i \vec u_i$$

Um conjunto de vetores é linearmente independente se nenhum deles pode ser expresso como uma combinação linear dos demais
:::
::: col
:: img src="base.svg" width="80%"
:::
---
# Sistema de coordenadas
:::col
Para gerar um espaço afim (pontos e vetores), além de uma base precisamos postular um ponto especial $O$ chamado origem

$$P = O + \sum_{i=1}^d \alpha_i \vec u_i$$

Os escalares $\alpha_i$ são as coordenadas do ponto ou vetor
:::
:::col
:: img src="sistema_coordenadas.svg" width="80%"
:::
---
# Coordenadas homogêneas
Uniformiza a representação de pontos e vetores

Usa-se uma coordenada extra para incluir ou não a origem, por exemplo:
- Vetores: $\vec v = [x\;  y\;  0]^T$
- Pontos: $P = [x\;  y\;  1]^T$
$$
\vec v = [\vec u_1\;\vec u_2\; O] \left[ \begin{array} {c} x \\ y \\ 0 \end{array} \right] , \quad P = [\vec u_1\;\vec u_2\; O] \left[ \begin{array}{c} x \\ y \\ 1 \end{array} \right]
$$
---
# Operações afim com coordenadas homogêneas
- Se a última coordenada é 1 → ponto
- Se a última coordenada é 0 → vetor
- Caso contrário → operação sem sentido

Por isso, 
- Ponto + Vetor → Ponto
- Ponto - Ponto → Vetor
- Vetor + Vetor → Vetor
- Vetor - Vetor → Vetor
- Escalar * Vetor → Vetor
- Ponto + Ponto → Operação sem sentido
---
# Sistemas de coordenadas usando matrizes

:::col
- Os vetores do S.C. e a origem são escritos como matrizes coluna. Ex:
$$
\vec u_1 = \left[ \begin{array}{c} u_{1x} \\ u_{1y} \\ 0 \end{array} \right], \quad \vec u_2 = \left[ \begin{array}{c} u_{2x} \\ u_{2y} \\ 0 \end{array} \right], \quad O = \left[ \begin{array}{c} O_x \\ O_y \\ 1 \end{array} \right]
$$
- Pode-se usar uma única matriz onde as $d$ primeiras colunas são vetores do S.C. e a última coluna é a origem.
$$
M = \left[ \begin{array}{ccc} \vec u_1 & \vec u_2 & \cdots & \vec u_d & O \end{array} \right]
$$

:::