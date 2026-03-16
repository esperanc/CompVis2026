::: center
# Computação Visual
## Aula 6 - Transformações projetivas
:::
---
# Transformações projetivas

Em essência, são mapeamentos de pontos em pontos onde se "perde" uma dimensão.

Podemos pensar em uma projeção de $\mathbb{R}^3$ em $\mathbb{R}^2$ como uma sombra de um objeto em uma parede.

O processo matemático normalmente consiste em calcular uma transformação  $\mathbb{R}^d \to \mathbb{R}^{d}$, seguido do "descarte" de uma coordenada.

Estamos interessados em transformações que preservam retas, ou seja, que transformam retas em retas.
---
# Projeções paralela e perspectiva

:::col
São as transformações mais comuns em computação gráfica.

- Paralela ou ortográfica: a "sombra" é formada por raios de luz paralelos (fonte luminosa infinitamente distante) e perpendiculares ao plano de projeção.
- Perspectiva: a "sombra" é formada por raios de luz que partem de um ponto (fonte luminosa finita).
:::
:::col
:: img src="Projecao.svg" width="90%"
:::
---
# _Pipeline_ de projeção

WebGL e outros sistemas assumem que os objetos estão em um cubo de _coordenadas normalizadas de dispositivo_ (NDC), que vai de -1 a 1 em todas as coordenadas.

As transformações de projeção consistem em levar os objetos de suas coordenadas originais (_coordenadas de mundo_ ou WC) para o cubo NDC.

As _coordenadas de tela_, ou seja, coordenadas dos pixels, são obtidas a partir das coordenadas NDC, através de uma transformação afim.
- Essa é a chamada transformação de _viewport_ 
---
# Pipeline de projeção
::img src="Pipeline projecao.png" width="80%"
---

# Matrizes Modelview e Projection

A transformação WC $\to$ NDC é feita por duas matrizes que correspondem a duas etapas conceituais

1. Transformação _ModelView_ (WC $\to$ VC)
   - Transforma os vértices dos objetos para colocá-los defronte a câmera (_View Coordinates_).
   - Pode também ser pensada como levar a câmera para um ponto e orientação conveniente do mundo.

2. Transformação _Projection_ (VC $\to$ NDC)
   - Corresponde a escolher a lente que vai ser usada para enquadrar a cena.
   - Pode ser ortográfica (paralela) ou perspectiva.
   
---
# Modelview com `camera()`

:::col
Em P5, a função `camera()` define a posição e orientação da câmara. 

```python
camera (eye_x, eye_y, eye_z, 
    center_x, center_y, center_z, 
    up_x, up_y, up_z)
```
- Default: `camera(0,0,800, 0,0,0, 0,1,0)`
- Responsável pela parte "view" da matriz ModelView. 

Outras transformações são tipicamente executadas depois de `camera()`
- Responsáveis pela parte "model" da matriz ModelView

:::
:::col
:: img src="Camera.png" width=90%
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    camera()
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
:: img src="cam0.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3HmIBbENLTZcUPCCohPcXBoX395LxxYaSooc1IAgFoARgBWdnTHHCVtAA9kJNZMiCjqWPjkAGZWNgyI6EQbdwCWIpKYuLJkZLSamqKdWHiADWQABQBJIrxtMJY2AtNMIA)
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    camera(400,-400,400)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
:: img src="cam1.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3HmIBbENOQAWVmwC039gDHHCg8ECoQNDEJaDCI+WxcWGkqKHNSSN8ARgBWdnzg5W0AD2Qs1kLk6jSM5ABmHwLEkMQbd0iWSpSasmRsvLYmxR1YDIANZAAFAElCvG14ljZy00wgA)
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    camera(400,-400,400,
           150,0,0)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
:: img src="cam2.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3HmIBbENOQAWVmwC039gC2bEVQiABGAFZ2GMccKDwQKhA0MQloROT5EJxYaSooc1IU3yiYtlMc5W0AD2Rw1jiIPOpC4uQAZh9YqqhEG3cUliaWgqKyZFLoioqmnVhigA1kAAUASSa8bSyWNgbKoA)
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    camera(400,-400,400,
           150,0,0, 1,0,0)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
:: img src="cam3.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3HmIBbENOQAWVmwC039gC2bEVQiABGAFZ2GLYIthjHHCg8ECoQNDEJaFT0+RCcWGkqKHNSDN8o2NMC5W0AD2Rw1iSIIupS8uQAZh9E2qhEG3cMllb2krKyZErohITWnVhygA1kAAUASVa8bTyWNmaaoA)
:::
---
# Projection com `perspective()`
:::col
Projeção default do p5.
```python
perspective(fovy,aspect,near,far)
```
- fovy: ângulo de visão vertical
- aspect: razão entre largura e altura
- near: distância do plano próximo
- far: distância do plano distante

Por default:
```python
perspective(2*atan(height/2/800), 
   width/height, 800/10, 800*10)
```
:::
:::col
::img src="perspective.png" width=90%
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    perspective(2*atan(height/2/800), 
      width/height, 800/10, 800*10)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
::img src="persp0.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3IhAEozvLEs0QRgFSlqZBsQazsAekMwzlQ2CGxFXBlLYFgbMODQ2FjOMIBGdghOX3zHHCg8ECofUXFwaAqq+XicWGkqKHNSHwBaXIBWdkHS5W0AD2R802aIVuoOruQAZlY2Iem3YKImKcVZ9s6yZF6B1dXhnVgugA1kAAUASWG8bUaWNkmaoA)
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    perspective(1.5*atan(height/2/800), 
      width/height, 800/10, 800*10)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
::img src="persp1.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3IhAEozvLEs0QyAIwA6AFYAKlJqZBsQazsAekMYzlQ2CGxFXBlLYFgbGMjo2GTOGN92CE5gksccKDwQKh9RcXBoWvr5VJxYaSooc1IfAFpfQPZRquVtAA8-VnGu6l7+5ABmVjYxjuhESKImU035nr6yZCGR9fXxnVh+gA1kAAUASXG8bTaWNhL9zCA)
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    perspective(atan(height/2/800), 
      width/height, 750, 800*10)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
::img src="persp2.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3IhAEozvLEs0QyAIwA6AFYAKlJqZBsQazsAekMYzlQ2CGxFXBlLYFgbGMjo2GTOGN92CE5gksccKDwQKh9RcXBoWvr5VJxYaSooc1IfAFpfQPZRquVtAA8-VnGu6l7+5ABmVjYxjuhESKImU035nr6yZCGR9fXxnVh+gA1kAAUASXG8bTaWNhL9zCA)
:::
---
# Projection com `ortho()`

:::col
Configura uma projeção ortográfica.

Os argumentos são as cotas do paralelepípedo que define o volume de visualização.

```python
ortho(left,right, 
      bottom,top,
      near,far)
```

Observe que `camera()` tipicamente leva os objetos para o semi-espaço z negativo!
:::
::: col
:: img src="ortho.png" width="90%"
:::
--- 
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    ortho(-400,400,-400,400,0,1000)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
:: img src="ortho0.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3NoKwb25AFoALKzY-23r7+bOwAjKym2LhQeCBUIGhiEtCx8fJROLDSVFDmpAkeoQCs7KWOOEraAB7I4ZGKWdS5+cgAzL5lGdCINiBETPW4jTl5ZJ7FpSHlEDqw+QAayAAKAJLTeNppLGx1ophAA)
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    ortho(-200,200,-200,400,0,1000)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
:: img src="ortho1.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3NoKwb25AFoT7b2y+s2X3YARlZTbFwoPBAqEDQxCWho2PkInFhpKihzUjiPYIBWdmLHHCVtAA9kUPDFDOps3OQAZgCStOhEGxAiJlrceqycsk9C4rZ+nB1YXIANZAAFAElS-G0UljYa0UwgA)
:::
---
:::col
```python
def setup():
    createCanvas(800,800,WEBGL)

def draw():
    background(220)
    lights()
    ortho(-300,300,-300,300, 750,1000)
    scene()

def scene():
    translate(-150,0,0)
    box(100)
    translate(300,0,0)
    sphere(80)
    translate(-150,0,0)
    rotateX(PI)
    cone(80,100)
```
:::
:::col
:: img src="ortho2.png" width=90%
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZADgAZmAaF9gdQFEAhAOIAZVJkyhIwAsQDuaLLggAjYngDWAcwIB7eFWDIATIeajFAGwCWGgBawGZ3NoKwb25AFoAzKzY-23r7+bBAA7ACs7ACMrKbYuFB4IFQgaGIS0Ekp8vE4sNJUUOakqR5RkWzscYpK2gAeyDHVuPnURSXIwVWOOFCINiBETM15Be1knuVVlT0QOrAlABrIAAoAkrN42tksbE2imEA)
:::
---
# Matemática da projeção perspectiva
:::col
A matriz modelview traz os objetos para o semi-espaço $z<0$.

O observador está na origem olhando ao longo do eixo $z$ negativo.

O plano de projeção é o plano $z = -1$ (por default).

A matriz projection leva um ponto $P=(x,y,z)$ em um ponto $P'=(x',y',-1)$
- *Problema*: Nenhuma transformação afim pode fazer isso!
:::
:::col
::img src="visao perspectiva.svg" width=90%
:::
---
# Matemática da projeção perspectiva
:::col
Projeção perspectiva envolve uma divisão:
$$
x' = \frac{x}{-z}, \quad y' = \frac{y}{-z}.
$$
Essa divisão é feita pela operação de **_normalização perspectiva_**
:::
:::col
::img src="projecao x.svg" width=90%
:::
---
# Normalização perspectiva

Antes de rasterizar as primitivas, todos os vértices passam por essa operação:
$$
NP ([x,\,y,\,z,\,w]^T) = 
[x/w,\,y/w,\,z/w,\,1]^T
$$

Matrizes montadas por `perspective()` têm um termo cruzado na linha 4, ex:
$$
\left[\begin{array}{cccc} 
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & A & B \\
0 & 0 & -1 & 0
\end{array}\right] \times \left[\begin{array}{c} x \\ y \\ z \\ 1 \end{array}\right] = \left[\begin{array}{c} x \\ y \\ Az+B \\ -z \end{array}\right]
$$
---
# Depth buffer

As coordenadas $x$ e $y$ dos vértices dão origem à posição do pixel na tela.

A coordenada $z$ vai dar origem à _profundidade_ do pixel
- Distância do observador ao ponto 
- Usada no _depth buffer_ ou _z-buffer_.

Esse é o motivo de incluirmos o parâmetro $near$ e $far$ na função `perspective()`.

- Vão dar origem aos valores $A$ e $B$ na linha 3 da matriz
---
:::center
#Obrigado!
:::