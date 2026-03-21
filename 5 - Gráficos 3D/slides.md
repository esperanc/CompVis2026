::: center
# Computação Visual
## Aula 5 - Gráficos 3D
:::
---
# O que muda de 2D para 3D?

Modelagem da cena
- Sólidos são delimitados por superfícies 
- Figuras planas são delimitadas por curvas

Projeção
- Em 2D precisamos de um _modelo de câmera_
- Transformações projetivas

Visibilidade
- Quais partes de quais objetos são visíveis?

---
# Placas gráficas (GPUs)

_Graphical Processing Unit_

Hardware com processadores em paralelo em arquitetura SIMD
- _Single Instruction, Multiple Data_

Alto paralelismo é necessário para processar grande quantidade primitivas e pixels.

APIs de baixo nível visam modelar o mais fielmente possível a arquitetura da GPU.

---
# APIs gráficas

APIs de baixo nível
- Vulkan (padrão desktop Khronos Group)
- WebGPU (padrão web Khronos Group)
- DirectX 12 (desktop Windows)
- Metal (desktop Apple)

APIs de nível médio
- OpenGL (padrão desktop Khronos Group)
- WebGL (padrão web Khronos Group)
- DirectX 11 (desktop Windows)

Bibliotecas
- P5, Three.js, etc
---
# O pipeline gráfico
:::center
::img src="./pipeline gráfico.png" width="80%"
:::
---
# Shaders

São programas que rodam na GPU.

No pipeline gráfico, tipicamente temos o vertex shader e o fragment shader.

Dependendo da API, podemos ter outros tipos de shader.
- Compute shader (WebGPU / Vulkan / DirectX 12 / Metal)
- Tessellation shader (OpenGL / Vulkan / DirectX 12 / Metal)
- Geometry shader (OpenGL / Vulkan / DirectX 12 / Metal)
---
# Bibliotecas

Permitem abstrair detalhes do pipeline gráfico.

Tipicamente incluem shaders pré-configurados para iluminação, texturização, construção de matrizes de transformação, etc.

Exemplos:
- P5 (2D e 3D)
- Three.js (3D)
- Processing (2D e 3D)

---
# P5 em 3D

Requer que o canvas seja criado com a opção `WEBGL`

Sistema de coordenadas:
- Posição (0,0,0) é o centro da tela!
- Câmera padrão gera projeção perspectiva.
- Vértices sobre o plano $z = 0$ são projetados sem distorção.

Primitivas 2D como `line`, `rect`, `circle` etc assumem coordenada $z = 0$.

Primitivas 3D incluem `box`, `cone`, `cylinder`, `ellipsoid`.
---
# Exemplo

:::col
```python
def setup():
    createCanvas(600, 600, WEBGL)

def draw():
    background(220)
    rotateX(radians(frameCount))
    box(400,400,50)
```
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZANgAZmAaCF9iAdQFEAQgHEAMqkyZQkYAWIB3NFlwQARsTwBrAOYEA9vCrBkAJmPNxyvbFIgAGslnAAltQZhZAWwr6qsVBdwVXQAPZAAWVjYI9gBWc0wgA)
:::
:::col
::img src="./3dsimples.png" width="80%"
:::
---
# Usando Geometry

Na renderização usando primitivas como `box()`, `sphere()` etc, os vértices são gerados e enviados para a GPU a cada chamada.

Isto pode se tornar um gargalo quando muitas primitivas precisam ser renderizadas a cada quadro.

Uma alternativa interessante é usar Objetos da classe `p5.Geometry`.

Um objeto `p5.Geometry` armazena os vértices e outros dados em buffers na memória da GPU.

Para desenhar um objeto `p5.Geometry` usa-se a função `model(my_geometry)` do objeto.
---
# Criando objetos `p5.Geometry`

Use `beginGeometry()` para indicar que você vai criar uma geometria.

Todas as primitivas desenhadas em seguida são armazenadas em
um objeto `p5.Geometry`.

`endGeometry()` retorna o objeto `p5.Geometry`.

Uma vez que o objeto não é necessário, use `freeGeometry()` para liberar a memória da GPU.
---
# Exemplo
:::col
```python
def setup():
    createCanvas(800,800, WEBGL)
    
    beginGeometry()
    sphere(200)
    geom = endGeometry()
    
    background(200)
    translate (-200,0,0)
    model(geom)
    translate (400,0,0)
    model(geom)
    
    freeGeometry(geom)
```
:::
:::col
:: img src="Geometry.png" width=80%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9iAdQFEAhAOIAZVNlzicAIxABzAJZVBIAPYBbOAQCeaSdEQALEEWQAmVmNwRZqtRAC8EEFWDL1mnZYlWpxPAGtZAhV4FzMLPVgCaigAG1IQCGQAWnN2dNQAbgg1FVBY5Bt1LxwomPiyJIAWVjYM7Jy8kAKitRKIPTAiEDcNKJ1WsSA)
:::
---
# `lights()` e  `orbitControl()`

Em 3D, é útil usar um modelo de iluminação para ter algum realismo.
- `lights()` liga um modelo de iluminação padrão
- `noLights()` desliga o modelo de iluminação

Uma função bastante útil para interagir com objetos 3D é a `orbitControl()`.

Ela permite que o usuário orbite em torno do objeto usando o mouse.

Chame `orbitControl()` em `draw()` para habilitar a interação.
---
# Exemplo
:::col
```python
def setup():
    createCanvas(800, 800, WEBGL)
    global geom
    beginGeometry()
    for i in range(100):
        push()
        p = [p5.random(-200,200) for i in (0,1,2)]
        translate(*p)
        sphere(40)
        pop()
    geom = endGeometry()

def draw():
    background(100)
    orbitControl()
    lights()
    noStroke()
    model(geom)
```
:::
:::col
::img src="orbit_light.png" width="80%"
[link](https://esperanc.github.io/Py5Script/view.html?code=E4QwdgJgBAvFAKBWAdKSB7AtgKGxApgGZQDO+ALgK4AOAFAJQBc2UrUAxsPiOfgMLgAbiBK0AHAAYJAGiiSZUAOoBRAEIBxADL0WbAOYAbdACMQBqHvxZdrY-j0BLMOquYKwAJ4MbUQumBQDoFgUGiWtACMUkw+bFDUlCQAFt5xcdSwUADaaBC0ALQATFLSxRL0vv6BwVC0MhGl9AC6sWzkaCQGPPi0AFTUOmlsJNRJ+Fy0ACzlrazU6HSD+q6Z+JAuWO5eOnhEUBCgAO4MzHGm7ADWesDolJCR0T7+xg7kfOhg7egGqWwGDnokuRREtWGB0ABlL4XHqgqCYdAEH6WLA6IA)
:::
---
# Transformações em 3D

Em 3D, as transformações são representadas por matrizes 4x4.

Translação e escala são extensões naturais de 2D

Rotação é bem mais complicado!
---
# Rotação em torno dos eixos
Em P5: `rotateX(ang)`, `rotateY(ang)`, `rotateZ(ang)`
$$
R_z(\theta)=\left[
    \begin{array}{cccc}
    \cos(\theta) & -\sin(\theta) & 0 & 0 \\
    \sin(\theta) & \cos(\theta) & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{array}
\right]
$$

$$
R_x(\theta)=\left[
    \begin{array}{cccc}
    1 & 0 & 0 & 0 \\
    0 & \cos(\theta) & -\sin(\theta) & 0 \\
    0 & \sin(\theta) & \cos(\theta) & 0 \\
    0 & 0 & 0 & 1
    \end{array}
\right]
\quad
R_y(\theta)=\left[
    \begin{array}{cccc}
    \cos(\theta) & 0 & \sin(\theta) & 0 \\
    0 & 1 & 0 & 0 \\
    -\sin(\theta) & 0 & \cos(\theta) & 0 \\
    0 & 0 & 0 & 1
    \end{array}
\right]

$$
---
# Rotação em torno de um eixo arbitrário

Em P5: `rotate(ang, vector)`, onde vector é criado com `createVector(x,y,z)`.

_Fórmula de Rodrigues_: Seja $\hat{u} = (u_x, u_y, u_z)$ um vetor unitário que define o eixo de rotação. Então, a rotação de um vetor $\vec{v}$ em torno de $\hat{u}$ é dada por:

$$\vec{v}_{rot} = \vec{v} \cos \theta + (\hat{u} \times \vec{v}) \sin \theta + \hat{u} (\hat{u} \cdot \vec{v}) (1 - \cos \theta).$$

Em notação matricial:
$$R = \begin{bmatrix} 
\cos\theta + u_x^2(1-\cos\theta) & u_x u_y(1-\cos\theta) - u_z\sin\theta & u_x u_z(1-\cos\theta) + u_y\sin\theta & 0 \\ 
u_y u_x(1-\cos\theta) + u_z\sin\theta & \cos\theta + u_y^2(1-\cos\theta) & u_y u_z(1-\cos\theta) - u_x\sin\theta & 0\\ 
u_z u_x(1-\cos\theta) - u_y\sin\theta & u_z u_y(1-\cos\theta) + u_x\sin\theta & \cos\theta + u_z^2(1-\cos\theta) & 0\\ 
0 & 0 & 0 & 1
\end{bmatrix}$$
---
# Exemplo

:::col
```python
def setup():
    createCanvas(600, 600, WEBGL)

def draw():
    background(220)
    rotate(radians(frameCount), 
        createVector(1,1,1))
    box(300,300,300)
```
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZANgAZmAaCF9iAdQFEAQgHEAMqkyZQkYAWIB3NFlwQARsTwBrAOYEA9vCrBkAJmPNxyvbFIhks4AEtqDMLIC2FfVVioOhEmQAaiB4sLoEyACMbNGRqBa4KroAHsgAzKxsGezZ4kA)
:::
:::col
::img src="./3drotate.png" width="80%"
:::
---
# Produto vetorial

:::col
O produto vetorial $\vec u \times \vec v$ é um vetor com as seguintes características:
- é ortogonal a $\vec u$ e $\vec v$ (regra da mão direita)
- tem comprimento $|\vec u| |\vec v| \sin \theta$ onde $\theta$ é o ângulo entre $\vec u$ e $\vec v$ 

Propriedades:
- Antissimétrico: $\vec u \times \vec v = -(\vec v \times \vec u)$
- Distributivo: $\vec u \times (\vec v + \vec w) = (\vec u \times \vec v) + (\vec u \times \vec w)$
- Associativo: $(k \vec u) \times \vec v = \vec u \times (k \vec v) = k (\vec u \times \vec v)$
:::
:::col
::img src="./prodvetorial.png" width="80%"
:::
---
# Operador de orientação

:::col
Dados dois pontos $A$ e $B$ em 2D, como determinar de que lado da reta $AB$ está um ponto $C$?
 - Como nomear o que é um lado ou outro?

Dados três pontos $A, B, C$ em 3D, como determinar se um ponto $D$ está acima ou abaixo do plano que passa por $A$, $B$ e $C$?
 - Como saber o que é acima e abaixo?

Para tanto precisamos do _operador de orientação_
:::
:::col
::img src="./Orientacao.svg" width="90%"
:::
---
# O operador de orientação

É o sinal do determinante da matriz formada pelos pontos em coordenadas homogêneas, porém com o $1$ na primeira linha.

 - Em 3D: $o(A,B,C,D) = \textrm{sign} \left(\left| \begin{array}{cccc} 1 & 1 & 1 & 1\\ x_A & x_B & x_C & x_D\\ y_A & y_B & y_C & y_D\\ z_A & z_B & z_C & z_D \end{array} \right|\right)$

 - Em 2D: $o(A,B,C) = \textrm{sign} \left(\left| \begin{array}{ccc} 1 & 1 & 1\\ x_A & x_B & x_C\\ y_A & y_B & y_C \end{array} \right|\right)$
---
# Operador de orientação
_Significado_: posição do último ponto com relação ao _simplex_ formado pelos pontos anteriores
- positivo : do lado "positivo" (regra da mão direita)
- negativo: do lado "negativo"
- zero: coplanar / colinear 
---
# O tipo `p5.Vector`

Criado com a função `createVector(x,y,z)`

Suporta um grande repertório de métodos para manipulação de vetores, ex.:
- `copy()`: cria uma cópia do vetor atual
- `add(v)`: soma o vetor `v` ao vetor atual
- `sub(v)`: subtrai o vetor `v` do vetor atual
- `mult(s)`: multiplica o vetor atual pelo escalar `s`
- `div(s)`: divide o vetor atual pelo escalar `s`
- `mag()`: retorna o comprimento do vetor
- `normalize()`: normaliza o vetor
- `cross(v)`: retorna o produto vetorial do vetor atual com o vetor `v`
- `dot(v)`: retorna o produto escalar do vetor atual com o vetor `v`
- `dist(p)`: retorna a distância entre o ponto atual e o ponto `p`
- `heading()`: retorna o ângulo do vetor em relação ao eixo x
- `rotate(ang)`: rotaciona o vetor em relação ao eixo z

---
:::center
# Obrigado!
:::


 