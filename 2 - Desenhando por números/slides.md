::: center
# Computação Visual
## Aula 2 - Desenhando por números
:::

---
# Processing e seus derivados

- Plataforma de programação criativa.
- Criada por Ben Fry e Casey Reas em 2001.
- Originalmente baseada em Java
- Variante JavaScript: [p5.js](https://p5js.org)
- Variantes Python
  - [Processing.py](https://py.processing.org/) (não mais mantido)
  - [Py5](https://py5coding.org) (também baseado em Java)
  - [Py5script](https://esperanc.github.io/Py5Script)
    - Baseada em Pyodide (Python em web)
    - Usa a biblioteca p5.js
---
# Documentação
- [p5.js](https://p5js.org/reference)
  - Documentação completa da biblioteca p5.js, que também é usada por Py5Script
  - Editor online: https://editor.p5js.org
  - OpenProcessing: https://openprocessing.org
- [Py5Script](https://github.com/esperanc/Py5Script)
  - Editor online: https://esperanc.github.io/Py5Script/
  - Essencialmente é o p5.js em Python, mas tem algumas diferenças por causa da diferença entre JavaScript e Python.
  

---
# Qual devo usar?

Trabalhos e exercícios do curso serão feitos usando p5.js / Py5Script.

- Py5Script usa Python, que é mais familiar para alguns, mas o sistema ainda está em desenvolvimento.
- p5.js é mais estável e tem uma grande comunidade.
 - Em https://youtu.be/mc5AmeoclPM?si=5V82F-u9p0ns4n4s você encontra uma série de vídeos explicando como usar o p5.js 
---
# Posso usar outra coisa?

- Claro! 
- Mas todos os trabalhos têm que ser abertos em um navegador
- Se o seu trabalho requerer alguma biblioteca, ela tem que vir embutida no código da página
- O _fonte_ também tem que ser disponibilizado com um link
- Não vale usar game engines como Unity, Unreal Engine, Godot, etc.

---
# Ideia geral 
:::col
- Programas são "sketches" (esboços)
  - Termo emprestado das artes visuais
- Funções primitivas para desenho 2D, ex:
  - `rect`, `circle`, `line`, `point`, etc.
- Variáveis globais para estado do programa, ex:
  - `width`, `height` para tamanho da tela
  - `mouseX`, `mouseY` para posição do mouse
  - `key` para tecla pressionada
:::
:::col reveal
- Funções callback chamadas automaticamente, ex:
  - `setup` (apenas uma vez)
  - `draw` (repetidamente)
  - `mousePressed` (quando o botão do mouse é pressionado)
  - `keyPressed` (quando uma tecla é pressionada)
:::
---
# O sistema de coordenadas
:: image src="./sistema coordenadas p5.svg" width="60%"
---
# Exemplo simples
:::col
### p5.js

```js
function setup() {
  createCanvas(windowWidth, windowHeight); // cria uma tela do tamanho da janela
  let d = min(width,height) * 0.8
  background ('gray')
  fill('white')
  circle (width/2, height/2, d)
}
```
::: 
:::col
### Py5Script
```python
def setup():
  createCanvas(windowWidth, windowHeight); # cria uma tela do tamanho da janela
  d = min(width,height) * 0.8
  background ('gray')
  fill('white')
  circle (width/2, height/2, d)
```
:::
---
[Exemplo simples (p5.js)](https://editor.p5js.org/esperanc/sketches/O-y8IRd4W)
:::center
:: iframe src="https://editor.p5js.org/esperanc/sketches/O-y8IRd4W"
:::
---
[Exemplo simples (py5script)](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgIQMYCcQBDWEAYSIDsA3IqZAdwEtLgB7BgdSeFgAsANBGasOACRBMA5n1ioA3NgjAIAXggBbFox78BfSTLkQAVBAAMAOgAcSgEZFcAayn428VhGQByV0QCe3qhKYEwANmE+DHxMpEFKuEz4uGEgXsy8fAD0AExCBtKyuULAwUA)
:::center
:: iframe src="https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgIQMYCcQBDWEAYSIDsA3IqZAdwEtLgB7BgdSeFgAsANBGasOACRBMA5n1ioA3NgjAIAXggBbFox78BfSTLkQAVBAAMAOgAcSgEZFcAayn428VhGQByV0QCe3qhKYEwANmE+DHxMpEFKuEz4uGEgXsy8fAD0AExCBtKyuULAwUA"
:::
--- 
# `setup()` e `draw()`

`setup()`: função chamada uma vez no início do programa
  - Responsável pela criação do canvas
    - `createCanvas(largura, altura)`
    - Para usar toda a janela,
      - `createCanvas(windowWidth, windowHeight)`

`draw()`: função chamada repetidamente (se definida)
  - Usada para _animação_ ou desenho interativo
---
# Primitivas de desenho
- `background(color)`
- `circle(x,y,r)`
- `rect(x,y,w,h)`
- `line(x1,y1,x2,y2)`
- `triangle(x1,y1,x2,y2,x3,y3)`
- `quad(x1,y1,x2,y2,x3,y3,x4,y4)`
- `ellipse(x,y,w,h)`
- `arc(x,y,w,h,start,end)`  
---
# Exemplo

:::col
```python
def setup():
  createCanvas(500, 500);
  background('gray')
  circle(100, 100, 80); 
  rect(210, 60, 80, 80); 
  triangle(400, 60, 360, 140, 440, 140);
  ellipse(100, 250, 100, 60);
  line(210, 210, 290, 290);
  quad(380, 220, 440, 210, 430, 280, 370, 270);
  arc(250, 400, 80, 80, 0.52, 5.76, PIE); 
```
[-> editor](https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hSgYwCcwBDeMAYWIDsA3YmVAVgAZmAaKF59AbhygBGxPAGsA5gQD2iKiFQByCcQCe89PzwBLAngA2YVAEZWHY+ygAObjyj8ieeKgBMxjgDZzVjld63c8Ak1qMX1UABYTKA8OAGZoqEMIjjCkhIjefjBdXU1kOCNIpxZTSI8M3ByqAxdzGo4nAE5apvKoAEdEYjkYrygnJ3MU2tcoMJja3piAdlqZ1uIdZ2LRyN7e5gA6RicORg2ptw4ABQBJAFFfYCA)
:::
:::col
:: iframe src="https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hSgYwCcwBDeMAYWIDsA3YmVAVgAZmAaKF59AbhygBGxPAGsA5gQD2iKiFQByCcQCe89PzwBLAngA2YVAEZWHY+ygAObjyj8ieeKgBMxjgDZzVjld63c8Ak1qMX1UABYTKA8OAGZoqEMIjjCkhIjefjBdXU1kOCNIpxZTSI8M3ByqAxdzGo4nAE5apvKoAEdEYjkYrygnJ3MU2tcoMJja3piAdlqZ1uIdZ2LRyN7e5gA6RicORg2ptw4ABQBJAFFfYCA"
:::

---
# Cores

- 1 número de 0 a 255 => Tom de cinza
- 3 números de 0 a 255 => RGB
- 4 números de 0 a 255 => RGBA
- String com especificação css:
  - Nome de cor: `yellow`, `brown`, etc
  - Hexadecimal: `#ff0000`, `#00ff00`, `#0000ff`
  - RGB: `rgb(255, 0, 0)`, `rgb(0, 255, 0)`, `rgb(0, 0, 255)`
  - RGBA: `rgba(255, 0, 0, 0.5)`, `rgba(0, 255, 0, 0.5)`, `rgba(0, 0, 255, 0.5)`
  - HSL: `hsl(0, 100%, 50%)`, `hsl(120, 100%, 50%)`, `hsl(240, 100%, 50%)`
  - HSLA: `hsla(0, 100%, 50%, 0.5)`, `hsla(120, 100%, 50%, 0.5)`, `hsla(240, 100%, 50%, 0.5)`
---
# Cor de traçado e de preenchimento
- `stroke(color)`
- `fill(color)`
- `noStroke()`
- `noFill()`
- `strokeWeight(width)`
---
# Exemplo

:::col
```python
def setup():
  createCanvas(500, 500);
  background(200)
  strokeWeight(2);
  fill('cyan');
  circle(100, 100, 80); 
  fill('#F0F');
  rect(210, 60, 80, 80); 
  fill(0,0,255);
  triangle(400, 60, 360, 140, 440, 140);
  fill('hsl(20,70%,50%)');
  ellipse(100, 250, 100, 60);
  stroke('#ff0077')
  strokeWeight(4);
  line(210, 210, 290, 290);
  strokeWeight(2); 
  fill('orange');
  quad(380, 220, 440, 210, 430, 280, 370, 270);
  fill('red');
  noStroke()
  arc(250, 400, 80, 80, 0.52, 5.76, PIE);
```
[-> editor](https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hSgYwCcwBDeMAYWIDsA3YmVAVgAZmAaKF59AbhygBGxPAGsA5gQD2iKiFQAmVun4x4UkWADqYAJZiAFvAW9+EHQBtzqAOR4AntWsnceHQTzmwqAIysOv9igADm4eKFMLK2sAYgAxZlinPlwiPCN5Xw4ANkCQjhDecNwzS1R2dnlGRmcoNR1qMU9UABY-KByOAGYOqG9Wjmb+3taakqj9GCtFNgB2ZgBSNhZ59CT+MEsdZDgfNsrAgOzQlTVJDRtoiAhWGZmnE-UtXQMjZprzHSovDMCfjnkAJy-IE1VSPbR6QzGMIRUrWSQEBpgNa4ACOiGIck6eSg8mmUEGv0yBM6vxxnTm-zmo0iNiIIBRUCokgAyqdzspcMR3AoWAM2jiccwAHSMeQcRjCmZZDgABQAkgBRXhAA)
:::
:::col
::iframe src="https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hSgYwCcwBDeMAYWIDsA3YmVAVgAZmAaKF59AbhygBGxPAGsA5gQD2iKiFQAmVun4x4UkWADqYAJZiAFvAW9+EHQBtzqAOR4AntWsnceHQTzmwqAIysOv9igADm4eKFMLK2sAYgAxZlinPlwiPCN5Xw4ANkCQjhDecNwzS1R2dnlGRmcoNR1qMU9UABY-KByOAGYOqG9Wjmb+3taakqj9GCtFNgB2ZgBSNhZ59CT+MEsdZDgfNsrAgOzQlTVJDRtoiAhWGZmnE-UtXQMjZprzHSovDMCfjnkAJy-IE1VSPbR6QzGMIRUrWSQEBpgNa4ACOiGIck6eSg8mmUEGv0yBM6vxxnTm-zmo0iNiIIBRUCokgAyqdzspcMR3AoWAM2jiccwAHSMeQcRjCmZZDgABQAkgBRXhAA"
:::
--- 
# Polígonos e linhas poligonais

- Usa-se uma combinação de
  - `beginShape()` para iniciar uma linha poligonal 
  - `vertex(x,y)` para adicionar vértices
  - `endShape()` para finalizar a linha poligonal
- Pode-se usar `CLOSE` como argumento de `endShape()` para fechar o polígono
---
# Exemplo

:::col
```python
def setup():
    createCanvas(500, 500)
    background(200)
    polygon(250,250,150,5)
    
def polygon (cx,cy,r,n):
    beginShape()
    for i in range(n):
        ang = i/n*TAU # TAU = 2 * pi
        x = cx + r * cos(ang)
        y = cy + r * sin(ang)
        vertex(x,y)
    endShape(CLOSE)
```
[-> editor](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZAVgAZmAaCF51bXAI2J4A1gHMCAe3hVgyAEyseuCInEAbAJ4jxVOSzay9ARj2NFuTKEgqNWqhGR4AHmzzq2BNlQy8cfECIBLKgBlAAtiRBA0HwgwcQIIAMS7AmoRKK8sJSU0iABeRIB6KgAqABUAQQBVCABiCEqagtkIEuUAmKVHfPxugGoIBLa8cQY0s2yIdR7XCAGh6CDkcc7cGhACMkdkZ3UJiBBpMIio8gAZAHlggFFUIAhttps://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZAVgAZmAaCF51bXAI2J4A1gHMCAe3hVgyAEyseuCInEAbAJ4jxVOSzay9ARj2NFuTKEgqNWqhGR4AHmzzq2BNlQy8cfECIBLKgBlAAtiRBA0HwgwcQIIAMS7AmoRKK8sJSU0iABeRIB6KgAqABUAQQBVCABiCEqagtkIEuUAmKVHfPxugGoIBLa8cQY0s2yIdR7XCAGh6CDkcc7cGhACMkdkZ3UJiBBpMIio8gAZAHlggFFUIA)
:::
:::col
::iframe src="https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZAVgAZmAaCF51bXAI2J4A1gHMCAe3hVgyAEyseuCInEAbAJ4jxVOSzay9ARj2NFuTKEgqNWqhGR4AHmzzq2BNlQy8cfECIBLKgBlAAtiRBA0HwgwcQIIAMS7AmoRKK8sJSU0iABeRIB6KgAqABUAQQBVCABiCEqagtkIEuUAmKVHfPxugGoIBLa8cQY0s2yIdR7XCAGh6CDkcc7cGhACMkdkZ3UJiBBpMIio8gAZAHlggFFUIA"
:::
--- 
# Funções matemáticas

A biblioteca P5, que é importada por default, já contém funções como

- `abs(x)`
- `sin(x)`
- `cos(x)`
- `tan(x)`

e constantes como 
- `PI`
- `TAU`

Para usar as funções matemáticas do Python, precisamos importar a biblioteca `math`.
---
# Exercício

Reproduza o desenho abaixo: 
::iframe src="https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZAdwEsrgB7RgdWeFgAsANBBZtOACRDMA5v1ipsuALbEC01hAC8EAAwA6AIyKcUAF5aISjU14Dh-KbPkQAVBGQGAtCrWsFuCAAPCxs+fk8zVAgAeggAJmMIAE8Qhxk5CNMo2ISAgCNiPABraQJ2eDYPHR1-XCp2AGVYMqKQNESoAEd4VRB3QMEkwUjE4AszaIAWRLBmABs59wNq2pwwdgJ8AbwU62BBYFRBZABmF33D4-2zy9PzwRuMRIC8ZgI8Ob7kQIBqPAGkn8hsAXHEFEA"

--- 
# E este?
::iframe src="https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZAdwEsrgB7RgdWeFgAsANBBZtOACRDMA5v1ipsuALbEC01hAC8EAAwA6AIyKcUAF5aISjU14Dh-KbPkQAVBGQGAtCrWsFuCAAPCxs+fk8zVAgAeggAJmMIAE8Qhxk5CNMo2ISAgCNiPABraQJ2eDYPHR1-XCp2AGVYMqKQNESoAEd4VRB3QMEkwUjE4AszGPjEgnHzHNcIWGp3AAUASWiADiiAYggAFgBWaLiIUFKQEChEsGYAGzv3A2ranDB2GbwBvBTrYEECKhBMh-mZPIDgQRBMAgcgwVCYVgAgE8MwCHg7n1kIEANRfQZ4oYEFxxBRAA"

--- 
# Raciocínio geométrico
 - Vamos precisar dos nossos conhecimentos de **geometria** para resolver problemas
 - Também vamos precisar de noções de **álgebra linear**!
---
# Programação criativa
 - Realizar desenhos usando código
 - Resultados interessantes requerem imaginação e conhecimento da técnica
--- 
# Alguns desenhos sugeridos pela AI::
:: image src="exerciciosP5-1.png" width = 90%
---
# Mais alguns:
:: image src="./exerciciosP5-2.png" width = 90%
---
::: center
# Para casa!

## Tenho certeza que vocês podem fazer muito melhor do que isso!
---
::: center
# Até a próxima!
:::