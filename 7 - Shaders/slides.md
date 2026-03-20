::: center
# Computação Visual
## Aula 7 - Introdução aos shaders
:::
---
# Por que programar GPUs?

- Extrair o máximo desempenho possível do pipeline gráfico
- Conseguir efeitos visuais que não são possíveis com o pipeline padrão
- Usar o pipeline gráfico para realizar tarefas não gráficas (GPGPU)
---
# Programação de GPU's
Pode ser feita usando diferentes frameworks

- WebGL
- OpenGL
- Vulkan
- DirectX
- Metal

Vamos abordar apenas **WebGL** neste curso
--- 
# Outros recursos

- [Tutorial sobre shaders do P5.js](https://p5js.org/tutorials/intro-to-shaders/) (Usamos bastante aqui)

- [WebGL 1.0 cheat sheet](https://www.khronos.org/files/webgl/webgl-reference-card-1_0.pdf) (Refêrência da API para WebGL 1.0)

- [WebGL 2.0 cheat sheet](https://www.khronos.org/files/webgl20-reference-guide.pdf) (Referência da API para WebGL 2.0)

- [WebGL 2.0 Fundamentals](https://webgl2fundamentals.org/) (Excelente tutorial para WebGL 2.0)
---
# O pipeline gráfico WebGL
:::center 
::img src="pipeline shader.svg" width="85%"
:::
---
# Shaders
São programas que rodam em estágios do pipeline gráfico. 

Em WebGL dois shaders são usados:

- Vertex shader
- Fragment shader

Um "Shader Program" requer os dois

Ambos são escritos em GLSL (OpenGL Shading Language)
---
:::center
# A linguagem GLSL
:::
---
# Variantes de GLSL

Existem diferentes versões de GLSL, cada uma com suas características.

Em WebGL 1.0 usamos GLSL ES 1.0

Em WebGL 2.0 usamos GLSL ES 3.0

Hoje WebGL 2.0 é amplamente suportado, mas muitos shaders ainda estão
escritos em GLSL ES 1.0

Aqui vamos usar apenas GLSL ES 1.0 
---
# Sintaxe básica
Inspirada na linguagem "C"

Todo shader contém pelo menos a função main e uma declaração de precisão para floats.

```glsl
precision highp float; // Pode ser lowp, mediump ou highp

void main() {
  // código do shader
}
```

O mínimo que um vertex shader deve fazer é computar a variável global `gl_Position`

O mínimo que um fragment shader deve fazer é computar a variável global `gl_FragColor`
---
# Classes de variáveis GLSL

- Uniforms: são variáveis definidas no programa CPU e passados para os shaders
  - O valor é o mesmo para todos os vértices e fragmentos
- Varyings: são variáveis passadas do vertex shader para o fragment shader
  - O valor é _interpolado_ (coordenadas baricêntricas) entre os vértices
- Atributos: são variáveis passadas do programa CPU para o vertex shader
  - O valor é diferente para cada vértice
---
:::center
:: img src="webgl vars.svg" width=90%
:::
---
# Tipos de variáveis GLSL

- `float`: número real
- `vec2`: vetor de 2 floats
- `vec3`: vetor de 3 floats
- `vec4`: vetor de 4 floats
- `mat2`: matriz de 2x2 floats
- `mat3`: matriz de 3x3 floats
- `mat4`: matriz de 4x4 floats
- `sampler2D`: textura 2D
- `samplerCube`: textura cúbica
---
# Os tipos vec2, vec3 e vec4
:::col
São tipicamente usados para armazenar pontos, vetores e cores.

Podem ser acessados por índices ou por nomes.

Pontos e vetores têm coordenadas com nomes (x, y, z, w).

Cores em glsl usam o modelo rgba com valores entre 0 e 1.

Existem também as variantes ivec2, ivec3, ivec3 (vetores de inteiros)
:::
:::col
```glsl
vec4 v = vec4(1.0, 2.0, 3.0, 1.0);

float x = v.x; // 1.0
float y = v.y; // 2.0
float z = v.z; // 3.0
float w = v.w; // 1.0
float r = v.r; // 1.0
float g = v.g; // 2.0
float b = v.b; // 3.0
float a = v.a; // 1.0
```
:::
---
# Exemplo de _vertex shader_ para o P5.js

```glsl
precision highp float;

attribute vec3 aPosition;
uniform mat4 uModelViewMatrix;
uniform mat4 uProjectionMatrix;

void main() {
  vec4 viewModelPosition = uModelViewMatrix * vec4(aPosition, 1.0);
  gl_Position = uProjectionMatrix * viewModelPosition;  
}
```
---
# Exemplo de _fragment shader_ para o P5.js
```glsl
precision highp float;

void main() {
  vec4 myColor = vec4(1.0, 0.0, 0.0, 1.0);
  gl_FragColor = myColor;
}
```
---
# Shaders com P5.js

Chame na callback padrão `preload()` do p5 uma das funções 
 - `loadShader(arquivoVS, arquivoFS)` ou
 - `createShader(codigoVS, codigoFS)`

Retornam um objeto que é passado para a função `shader()` antes de desenhar em `setup()` ou `draw()`

`shader()` só tem efeito para a parte "fill" do desenho 
  - Carrega os atributos correspondentes aos vértices
  - Passa os uniforms para o shader

---
# Exemplo
:::col
```python
def preload():
    global my_shader
    my_shader = loadShader(
        "vertex_shader.glsl",
        "frag_shader.glsl")

def setup():
    createCanvas(600, 600, WEBGL)

def draw():
    background(220)
    noStroke()
    shader(my_shader)
    ellipse (0,0,400,400)
```
:::
:::col
:: img src="shader simples.png" width=80%
:::
---
# Uniforms e atributos comuns no P5.js

Uniforms:

- `mat4 uModelViewMatrix`: Matriz ModelView
- `mat4 uProjectionMatrix`: Matriz Projection
- `mat3 uNormalMatrix`: Matriz para transformação das normais

Attributes:

- `vec3 aPosition`: Posição do vértice
- `vec3 aNormal`: Normal do vértice
- `vec2 aTexCoord`: Coordenada de textura do vértice
- `vec4 aVertexColor`: Cor por vértice

Mais informações:

[Documentação do P5.js WEBGL mode](https://github.com/processing/p5.js/blob/main/contributor_docs/webgl_mode_architecture.md)
---
# Usando uniforms
Além dos uniforms pré-definidos pelo P5, é possível definir e usar uniforms próprios.

O objeto shader tem um método chamado `setUniform (nome,valor)` que pode
ser usado para isso.

Por exemplo, se no vertex shader temos
```glsl
uniform float t;
```

Então no P5.js podemos fazer:

```python
my_shader.setUniform("t", 0.1)
```
---
# Exemplo
:: img src="uniform.png" height = 80%
[link](https://esperanc.github.io/Py5Script/view.html?zip=KoUQzgIgQggg9jRSQBcCMATAYgDwFoDKALAK4BKA0jCIgMIDmsiAUkjAMYBMKANhgOIA5OABkAdlACsefgDUAtgEkAElACeeAOo4AbgE1NARTgUAKicW0Y9RfwxgARp2YALB7SgoAprICcALwBDfiwAazwADUUKS2tbNEkIgGZhAzIedgBLGF9bXTTTYLDIxThabJsrSrixPAyxQxI8Thx-d0Uwcriq2Jt5PDUDdiaWttpFAAcGCfDNPXouWQAGDAj4MwseoQ1NLCW8YEE3Wpd2NXpOAFkIGDBFCD0Ad0vaR-pl2VoyJcep+hmtPM8MpXBhzhMAPL0ODVeh6eRYABWgU4YIcSVkTQYakuiJgUwqligJAcaEES3Y8l8ACdCP8upUoEEQuEonAHBEeAAzLguFwyWRqCjGWEc7m8-lyNTiQR8LCYwKaPA6SlLegUWjMJaKTJvPBiVwOTSyCDozEYWgADhwL1CMS2skc-B4jy4wHVNzAL0eS2ut0EN0ewomhgIzxADDYiAIGKWEWYvkyEDUzGAMEMiFk1CQoSQUE4kS1Ink9i4OFd8lkyIiggmTiI9GCPDEgWU1jw8nyEUMAHZpi4MMoyGpFcxMPx3RhK4jLmooC5gPwAoEImQ65wiH2xAqlSr5GqjXtBB40KZNL5ZjhNIrZEkz3tKTwiBDfmgHPIePJ0cwUPEBxBDHoDBZHUJwJh4PQkjXJxJEEPRVxHCJ6D7f43w-L8kh-Ww8EcTg9hUXtpk4JweFCP9FSIEwCCgPsKinKtj3zG873PS9DHRWsBB4HQHGyXJlFkQQnHSBwsDwCZIgwOCEJXeh1UyfMtEuJYKBCdiUgmLieN1ehLmIINTDAe0mONFiLy0HB1M451tMkIhLDAXIIBAR4RDxeSmQouALRgakVHEyShM4ESsCgFVOB4JZFV8EhxFCeSYFcxEQEhR4YVsewIjQMKuEi6KSHuNVgNAzhwMg6DOFg+Dh1kjzOGYs9zO0KzNJshxETAGx8V8UBIFgBAo1QTBcFkS0IREWgHDYfhHjYVgkH1VwBkkMQHGUQQwHYEEIIioJzwK-gXAkzgXEebDcL2F8TCnXwJI8FADB4EgNXirw0psZQ6j0fxALFU0WhVPj-Ign64D0ohXKsJLbnuGASG9XT9LMIyiVWrBfH4SksAaThfEcJJFHoAAFajvEOHilzUF8Jh68BYBcDNIyjGNlgiLAeBETJJBABAMxgKgaEQXMoxF0WkHW2lV2RWhJEeHwoBEdNFDTeARaG7A1C5eZLUyLNBawQwmBgeaxdFkBLSYRT4yWYtSxaUNHgjLBECoKMFdWMh2FkLkIF1eRZsQKAwDYWg+dNqMICoehEEW-k1BWtaNt60Lo7YG4YEufEw72dO2AAXjzoA)

---
# Usando Geometry

Na renderização usando primitivas como `rect()`, `circle()`, `box()`, etc, os vértices são gerados e enviados para a GPU a cada chamada.

Isto pode se tornar um gargalo quando muitas primitivas precisam ser renderizadas a cada quadro.

Uma alternativa interessante é usar Objetos da classe `p5.Geometry`.

- `p5.Sphere()`
- `p5.Box()`
- `p5.Cylinder()`
- `p5.Cone()`
- `p5.Torus()`
- `p5.Plane()`
- `p5.TorusKnot()`
- `p5.Icosahedron()`
- `p5.Octahedron()`
- `p5.Dodecahedron()`
- `p5.Tetrahedron()`
- `p5.Pyramid()`
- `p5.Cylinder()`
- `p5.Cone()`
- `p5.Torus()`
- `p5.Plane()`
- `p5.TorusKnot()`
- `p5.Icosahedron()`
- `p5.Octahedron()`
- `p5.Dodecahedron()`
- `p5.Tetrahedron()`
- `p5.Pyramid()