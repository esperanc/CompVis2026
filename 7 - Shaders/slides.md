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

Pontos, vetores, cores têm coordenadas com nomes 
 - `x`, `y`, `z`, `w` ou `r`, `g`, `b`, `a`

Usando mais de um nome depois do ponto pode-se construir novos vetores.
 - Ex.: `v.xy` é o mesmo que `vec2(v.x, v.y)`
 - Ex.: `v.zyxw` é o mesmo que `vec4(v.z, v.y, v.x, v.w)`
 

Cores em glsl usam o modelo rgba com valores entre 0 e 1.

Existem também as variantes ivec2, ivec3, ivec3 (vetores de inteiros)
:::
:::col
```glsl
vec4 v = vec4(1.0, 2.0, 3.0, 1.0);

float x = v.x; // 1.0
float y = v.g; // 2.0
vec2 u = v.rg; // vec2(1.0, 2.0)
vec3 color = v.rgb / 4.; // vec3(0.25, 0.5, 0.75)
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
# Uniforms do tipo vec2, vec3, vec4

Para passar valores para uniforms desses tipos, pode-se usar arrays do tamanho adequado.

Para quem usa _Py5Script_ é necessário converter listas em arrays javascript usando o utilitário `js_array()`.

Exemplo:
```python
my_shader.setUniform("v", js_array([1.0, 2.0, 3.0]))
```
---
# Campos de distância com sinal (SDF)

Ao invés de codificar geometria com vértices, é possível descrever formas usando funções implícitas da forma:

- $f(x,y,z) = 0$ para pontos na superfície
- $f(x,y,z) < 0$ para pontos dentro da superfície
- $f(x,y,z) > 0$ para pontos fora da superfície

Se além disso, $f(x,y,z)$ for a distância euclidiana do ponto $(x,y,z)$ à superfície, então $f$ é um campo de distância com sinal (SDF)

---
# SDFs com fragment shaders

SDFs em 2D podem ser trivialmente desenhados usando fragment shaders.

- Desenha-se um retângulo cobrindo toda a tela
  - Use a primitiva `plane()` para isso
- O vertex shader básico é suficiente
- O fragment shader aplica a SDF à coordenada do fragmento
  - varying embutido `gl_FragCoord`
  - a cor depende do valor do SDF
- Atenção com displays ``retina''!
  - A dimensão do canvas pode ser maior do que width x height!
  - Use `pixelDensity(1)` para evitar problemas
  - Ou multiplique as dimensões por `pixelDensity()`
---
:::col ratio=70%
```python
def preload():
    global my_shader
    my_shader = loadShader("vert.glsl", "frag.glsl")
    
def setup():
    createCanvas(800, 800, WEBGL)
    pixelDensity(1)

def draw():
    background(220)
    shader(my_shader)
    noStroke()
    plane(800,800)
```
Fragment shader:
```glsl
precision highp float;
void main() {
    vec2 v = gl_FragCoord.xy - vec2(400.,400.);
    if (length(v)>300.0) gl_FragColor = vec4(1);
    else gl_FragColor = vec4(1,0,0,1);
}
```
:::
:::col ratio=30%
::img src="fragcircle.png" width=80%

[link](https://esperanc.github.io/Py5Script/view.html?zip=KoUQzgIgQggg9jRSDiyBSATANgTwB4DyAbFAJYDUA5kgAoJJpIwDGATAC5YbIBycAMgDsoAVgBayAGoBbAJIAJKDjEB1PADcAmioCKcANIAVA7IDCMSrOQYwAI1ZoAFrdNR2AU0kBOAF4BDZAAxAGsxAA1ZfTMLKwBGETCAZj5tACUsZlIYLysNNMMAkPDZOFlBMQzBHQBXMVY8HxdZMDM0aWZpQMF+aRs2AHdSfT1Lc0pTaXSxUigfcNTY5lNKAAcCSjhRi01EtCxNMPSdVkDqjE6ffQhKfoBZU37KAggYfv5XQ+A0eUNTYKixgooCt3FIwKkpNU2FgAAzuADKlDwwwMEhkVlSOAOzAMxgBMXQjk0HEEHS8sVs0j0twAVrJ+iitpQ2I5HGicPpkPEkikVOlMv9opZkCJ1MBEpj7Jx9H98ZZFGBtCIsFcbvd+gAWW4vFamLBQfivHT6JiIKCOUhhMRsABO2Uc6g1SAg5CYph0SHkFWYVVq9UaimUKh4K2h6lsMzgfhUGDgSyg0lsyC8jgwEDAMs6MIw8jQK00gkkMLE8KgrFUtx8VkCOlsyRW3Cw4ZpGYwKhEKzE0i8OFspfYBx0MIUkh49nStkCYk7YQwPAOmL8YUoAHZTIXqtGxOoOjDKLYVIEYTxXLFgLn1H5pJIaY3w8FYqncyD0zLypfdPvDysI6sFBmzDLCthy9Gc53HLBJygHdWFhaMvGqWQID3DBgFidQ0TAGQsC4GFHxzPN3HMABHBQKk0Hw9E0SRoOhGF4Oqd4YDwfgaRgNZ+k2KwbDCWJaNg+iVAQpCUJo3tWBWfYJR-VgRHnQ4cCXShKH0GZWGjSREkMITQjUWt6zvWwW0sdivFASBYHoJhUEwLA8BaOBqhAVh+iQHgwCYRgkDEQQnDEHAREEWx5Hc5hc32WD-CExDkEcTtWEcforDEOwThhAhOP0c4vE7VwBxULBqhlYJKHcTimXOG9bjUkTKDqPAADNUl8tlj3DXZgiERwRDMFDrxparKBhbUYEYiAdDuUwNQ4rixmjTQVOQPBIN6ejTEcVgjH6HwRuqe5BUBQ6oCCwIvGQDoumOLw7ESWRKBoUtyxUW4YSuEA9oeSh7g1N5zDeNiWggd79rXLJRigSCQqwUwwaFIV6qalqxDapMe1qyqaRPJFWJgQHgc+254R+piWLYjiVjM8BYEcD1llNGBNE0LBWDCfgQBXOBkH4IgmCoJhgnpwWhZgEKbXmGk-FMER+k8A0YB0WRgEQKyUHQbB-EgVhkAAemoRAaCdBhhaF0wQFgGAgLCNAYR6Pp6h0eF+hAUxAkQE1TXNS1rRcfR+EcdznVsN0PWNj3kAsRAfL8gKgpCsBzMCKA9edRBbnYkOYBASgXlNABeXOgA)
:::
---
# Modelando SDF's

Uma grande compilação de SDFs implementados com fragment shaders pode ser encontrada [neste artigo](https://iquilezles.org/articles/distfunctions2d/) do mestre Inigo Quilez.

Utilizam funções primitivas glsl como:
- clamp(val,a,b) -> retorna val se a <= val <= b, senão retorna a ou b
- step(edge,x) -> retorna 0 se x < edge, senão retorna 1
- smoothstep(edge0,edge1,x) -> retorna 0 se x <= edge0, 1 se x >= edge1, e interpola suavemente entre 0 e 1 no intervalo [edge0,edge1]
- min(a,b) -> retorna o menor entre a e b
- max(a,b) -> retorna o maior entre a e b
- abs(x) -> retorna o valor absoluto de x
- sign(x) -> retorna -1 se x < 0, 0 se x == 0, e 1 se x > 0
- mod(x,y) -> retorna o resto da divisão de x por y
- fract(x) -> retorna a parte fracionária de x
- length(v) -> retorna o comprimento do vetor v
- dot(a,b) -> retorna o produto escalar dos vetores a e b
- cross(a,b) -> retorna o produto vetorial dos vetores a e b
- normalize(v) -> retorna o vetor unitário na direção de v
- mix(a,b,t) -> retorna uma interpolação linear entre a e b com parâmetro t
---
# Derivação da SDF para caixas
:::center
::img src="inigobox.png" width=70%
[link](https://www.youtube.com/watch?v=62-pRVZuS5c)
:::
---
# Exemplo: caixa
:: iframe src="https://esperanc.github.io/Py5Script/view.html?zip=KoUQzgIgQggg9jRSCSBXAjgEwDYE8AeA8gGxQCWA1AOZIAKCSAUkjAMYBMALtpgOIBycADIA7KAFYAWrwBqAW2QAJKLkkB1fADcAmmoCKcANIAVI8gDCMKsl6YwAI3aMAFvfNROAUxkBOAF4AhrwAYgDWkgAayIYWVjYAjOIRAMyCugBK2KxkMD42WhnGQWGRyHDIIpJZInqokuz4fm7IYBaMcqxywSJCcnYcAO5khgbWllTmcpmSZFB+kenxrOZUAA6EVHBjVtrJjNjaEZl67MGomF1+hhBUAwCy5gNUhBAwA0LuR8CMisbmoTFxkooKtPLIwOlZKgONgAAyeADKVHwIyM0nkNnSuEOrCMpkBcV4Lm0XBEnR88XscgMdwAVsgBqjtlQOM5nOjcIZeIkUmk1JlsgDYtZeOJNMBkljHNxDP8CdZlGBdOJsNdbg8BgAWO6vVbmbBQIRvPSGFiIcxCdCVDgAJ1yzk0mqQEAoLHMeiQiiqrBqdQaTWUqjU-FWMM09lmcACakwcGWUDk9l4PmcmAgYFlXVhmEUjFW2hEMlhkgRUHY6jufhswT09lSqz42HDtIzmDU4lWkjkPlw9lLnEOelhShk-EcmXswUknYimH4hyxAQiVAA7OZC6ho5JNJ1YVR7GpgrD+O54sBc5oAnIZLTG+HQvFU7nQenZZVL-p94fVhG1koMxYZYVsOXoznO47YJOUA7uwcLRj4qDIBAe6YMA8SaOiYDyNgPCwo+OZ5p4ljoEoVTaH4BjaDI0EwrC8GoB8MD4EItIwOsAxbDYdgRPENGwXRagIUhKHUb27CrAcko-uw4jzkcuBLlQVCGLM7DRjIyTGIJ4QaLW9Z3vYLbWGxPigJAsAMCwaBYHgTSamIwQwMgiBQHoliIMwSCSCILiSLg4giPYij8GArC5gcsGBIJiG8M4nbsM4Aw2JIDinLChAcYYXYFBEegsuw6TmHWmwXDedyzO87jlmody4DYyDKaWa45GMQE1XVvB5bQpbOAWdxxv8A4tvKSj7DmMi9rMYDqAFfCbAewSalyehgA8mqMgioTKbgHjRpqcALUtnWoER+ChKIoSrEIryoA8oRriIsJvmRfh3FQJI+A4yQNVyKWOEeNh6Ks-7yuYCIAByaDY-DhsmCntiI5gtYB1WVtD4aWHk5jOKEtCsbd-xULQO2o1cN2EAiAzvLS2ireYmpXAiMDEKRByvXAa3sPwlPU1Q8TXSABP3UjcTuKEFjg3kEB3Pc9MDBlnHjB9rTmHAUuCw8MCcDYMiassVCcPwZDrYYXRkKwuA44Ym1rlQ2C0o4TyGLSe5rZqFhgFQa2cnIMMW8i-DGDABOrACxgZuYERjYoE0Rrty7lAIGNPKVtK1ciLFsYxzGsZwHDoXW6RxpKWQrNTMB0+tdwIvgvUiP1kj-MD-wrhlqw+CsqzsI42Di9yzh7UYTUi61ibJqmYvCflhXFXAI-CsK9T4AAZukPnsse4Z7OdIjOOIFgodeadkFQsI6hX-CvBtTzz0C4yp+VyLn6trEbcLyPuIFwQ+LwnTdCcn06wNW6m1O4T0k5Jh7MtK6EBBYmAzMvaiRo9DIGAIgSyKAMA4AICQcg1A6AYM8maYhJCXKBHYEWEkVBoSKGwHoSmIBzCORgKaM0ForSSFtPaR0zpXRIHdKQwRzgYAehgKVXAmBzABSCiFMysBnAehWMQsgxAu4RCEDDc2IA0E0BgI5ZyiBQiCNIekYyMBeB+V0KwP0jQoJCFctoYhAwYCvEMGg80UBYBmgALxAA"
---
:::center
# Obrigado!
:::