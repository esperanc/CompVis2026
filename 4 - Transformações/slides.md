::: center
# Computação Visual
## Aula 4 - Transformações
:::
---
# Transformações lineares
São operadores _lineares_
- Mapeiam pontos e vetores em outros pontos e vetores
- Preservam a origem
- Preservam retas e paralelismo
- Preservam razões entre distâncias

Em 2D
$$
\begin{array}{l}
x^\prime = a x + b y \\
y^\prime = c x + d y
\end{array}
$$
---
# Transformações lineares afim
Estendem as transformações lineares permitindo _translações_
- Observe que "translação" só faz sentido para _pontos_!

$$
\begin{array}{l}
x^\prime = a x + b y + e \\
y^\prime = c x + d y + f
\end{array}
$$
---
# Transformações com coordenadas homogêneas

Vetores:
$$
\left[
\begin{array}{c}
x' \\
y' \\
0 
\end{array}
\right]
= 
\left[
\begin{array}{ccc}
a & b & e \\
c & d & f \\
0 & 0 & 1
\end{array}
\right]
\times
\left[
\begin{array}{c}
x \\
y \\
0 
\end{array}
\right]
$$

Pontos:
$$
\left[
\begin{array}{c}
x' \\
y' \\
1
\end{array}
\right]
= 
\left[
\begin{array}{ccc}
a & b & e \\
c & d & f \\
0 & 0 & 1
\end{array}
\right]
\times
\left[
\begin{array}{c}
x \\
y \\
1
\end{array}
\right]
$$
---
# Transformações e Mudanças de Base

São duas visões da mesma operação. 

- __Transformação__: o objeto muda de lugar
- __Mudança de base__: o sistema de coordenadas muda de lugar
---
# Translação
:::col
Em p5: `translate(dx,dy)`
$$
\left[
\begin{array}{ccc}
1 & 0 & dx \\
0 & 1 & dy \\
0 & 0 & 1
\end{array}
\right]
$$
:::
:::col
::img src="./translate.png" width="80%"
:::
---
# Rotação
:::col
Em p5: `rotate(ang)`
$$
\left[
\begin{array}{ccc}
\cos(\theta) & -\sin(\theta) & 0 \\
\sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 1
\end{array}
\right]
$$
:::
:::col
::img src="./rotate.png" width="80%"
:::
---
# Escala
:::col
Em p5: `scale(sx,sy)`
$$
\left[
\begin{array}{ccc}
sx & 0 & 1 \\
0 & sy & 1 \\
0 & 0 & 1
\end{array}
\right]
$$
:::
:::col
::img src="./scale.png" width="80%"
:::
---
# Inclinação (cisalhamento)
:::col
Em p5: `shearX(ang)` e `shearY(ang)`
$$
\left[
\begin{array}{ccc}
1 & \tan(\theta) & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}
\right]
$$
:::
:::col
::img src="./shearx.png" width="80%"
:::
---
# Composição de transformações 

A ordem é importante!

Interpretando como **mudança de base**
- Cada transformação é aplicada no sistema de coordenadas anterior
- Leitura de cima para baixo 

---
**[Exemplo](https://esperanc.github.io/Py5Script/view.html?code=C4JwhgdgzgZg9iAtlABAXhQbQFArygIgAUBWAOlEigBsxgBTFACgEYAaAWgCYBKAt3PmLkQcYHXpNSZIgEkA9ABY+A-IWlQAxmGqSADGRJsWhvoLwBdbNgAm9GCgBu9TcwAebAJ48AXChD0wACuIBAomgESAGouwAhMHt7Wdg5QgUEADky+5uGRDADCkI5gUEwAbHp6bCiVejy5AObUcABGOijAmnBBEMC5XT196Ch6yfYoANb0nkQBUGk22T5NLe3Und29-WoAlg7Tnii7YQRQAMoEfrlqUGDOTDAElNDwSCgA3oPbAL5kGRBGgQGmp6NQ0is1GpvsMMEwYcAANQsHgAUiYugg8PArwQyB4yJB+FsExs4AA7stcu1NJNGqJejZmFwqkS8DBdtRqEx6rkoKA4NMeWzOvQ3MBzrsAF6SADMvLUb2ObBeqBOKHoECCiHo4AY2Kob2QmB8CIsOSh+GAI1VZACGVomkkwjI-AIwJuVrFwHhbBZbFlJAAVExdoSRQxxcwzgBHIJgAI8tjVFH8FD+lCBkMI8MDHE0CTMcm7GzAAAW8i4NTL9F2jTLwErIq0OkYrFZfIF0wA6rX69amFx5CwO4rOdyFfgAIJsABCbAKI2cmiT9TYy9YyZ465cSZRuSnIFElJnKHnLEr9TIZLAlJFh+PTFPBWMl5414p2U7oh7fYbg+HUd8A5LlBxIIwWC4AAOZsnQgSQGhJVI4IQyFgIQTp8wcdVVSNKATTNNDLXoEpuVw+85wXJdd2qNcN3YOiaOMe8jzgE8anPN8P1vL81AfNinxqF8LxZd8bzvNRcggOBzi7BC+TjBM21o5jrE0WgFhQIg4BOYAiJQFIUAAfSMk5dmAEymDSagYDYDI2FoVowTQd0LUtFBrJgf4RgyT08E8shHOcoLqFyXJDPEqywRgNzLU0XYQHUtsAoyMgPA86L-jITwahgvyUAyIIoDLXj3P5H96F7Ot-33dzRSjKKbMCsAnOoGoUrS9rMtSzwOEgkU1AyOAsgG4l1NKVB+PJfTDJMsyLKMxrbIKmoY3akYDBRfTbm6nz8oCmMRhjfbMtQDAoBOprlyOshugyTxsjIKAglaJgMlG-zMscEYAuXW7hoe99pKQHRpXk8LSU-TzYqhey1scNgzoypr7ORry1rRsgEYCi66uoE5JFSjwerYGNOrJpI6qCJd-vux7RHEfU5CbJ7AgAWTARorI+-wbruwGnpephHFpgW0mADmuagINeB5sARhAUXHrAGwliCHnWgVpX32e171fy0BdkgZo2zATqUDNnKUDJ9KKZqVpzYdyn3IAYg8vmAeV1Xhe11mJc51hZfyt3CuK0rLTd8rBUqv8fVq136oHAKIDAHV2vNqBsp5kPhq-IA)**
:::col
::img src="./transform 0.png" width="80%"
:::
:::col
::img src="./transform 1.png" width="80%"
:::

---
**[Exemplo](https://esperanc.github.io/Py5Script/view.html?code=C4JwhgdgzgZg9iAtlABAXhQbQFArygIgAUBWAOlEigBsxgBTFACgEYAaAWgCYBKAt3PmLkQcYHXpNSZIgEkA9ABY+A-IWlQAxmGqSADGRJsWhvoLwBdbNgAm9GCgBu9TcwAebAJ48AXChD0wACuIBAomgESAGouwAhMHt7Wdg5QgUEADky+5uGRDADCkI5gUEwAbHp6bCiVejy5AObUcABGOijAmnBBEMC5XT196Ch6yfYoANb0nkQBUGk22T5NLe3Und29-WoAlg7Tnii7YQRQAMoEfrlqUGDOTDAElNDwSCgA3oPbAL5kGRBGgQGmp6NQ0is1GpvsMMEwYcAANQsHgAUiYugg8PArwQyB4yJB+FsExs4AA7stcu1NJNGqJejZmFwqkS8DBdtRqEx6rkoKA4NMeWzOvQ3MBzrsAF6SADMvLUb2ObBeqBOKHoECCiHo4AY2Kob2QmB8CIsOSh+GAI1VZACGVomkkwjI-AIwJuVrFwHhbBZbFlJAAVExdoSRQxxcwzgBHIJgAI8tjVFH8FD+lCBkMI8MDHE0CTMcm7GzAAAW8i4NTL9F2jTLwErIq0OkYrFZfIF0wA6rX69amFx5CwO4rOdyFfgAIJsABCbAKI2cmiT9TYy9YyZ465cSZRuSnIFElJnKHnLEr9TIZLAlJFh+PTFPBWMl5414p2U7oh7fYbg+HUd8A5LlBxIIwWC4AAOZsnQgSQGhJVI4IQyFgIQTp8wcdVVSNKATTNNDLXoEpuVw+85wXJdd2qNcN3YOiaOMe8jzgE8anPN8P1vL81AfNinxqF8LxZd8bzvNRcggOBzi7BC+TjBM21o5jrE0WgFhQIg4BOYAiJQFIUAAfSMk5dmAEymDSagYDYDI2FoVowTQd0LUtFBrJgf4RgyT08E8shHOcoLqFyXJDPEqywRgNzLU0XYQHUtsAoyMgPA86L-jITwahgvyUAyIIoDLXj3P5H96F7Ot-33dzRSjKKbMCsAnOoGoUrS9rMtSzwOEgkU1AyOAsgG4l1NKVB+PJfTDJMsyLKMxrbIKmoY3akYDBRfTbm6nz8oCmMRhjfbMtQDAoBOprlyOshugyTxsjIKAglaJgMlG-zMscEYAuXW7hoe99pKQHRpXk8LSU-TzYqhey1scNgzoypr7ORry1rRsgEYCi66uoE5JFSjwerYGNOrJpI6qCJd-vux7RHEfU5CbJ7AgAWTARorI+-wbruwGnpephHFpgW0mADmuagINeB5sARhAUXHrAGwliCHnWgVpX32e171fy0BdkgZo2zATqUDNnKUDJ9KKZqVpzYdyn3IAYg8vmAeV1Xhe11mJc51hZfyt3CuK0rLTd8rBUqv8fVq136oHAKIDAHV2vNqBsp5kPhq-IA)**
:::col
::img src="./transform 2.png" width="80%"
:::
:::col
::img src="./transform 3.png" width="80%"
:::
---
# Composição de transformações II

Interpretando como **cascata de transformações**
- Leitura de baixo para cima!
- Assume-se que o sistema de coordenadas não muda!
---
**Exemplo**
:::col
::img src="./transform 0.png" width="80%"
:::
:::col
::img src="./scale.png" width="80%"
:::
---
**Exemplo**
:::col
::img src="./transform 2 b.png" width="80%"
:::
:::col
::img src="./transform 3.png" width="80%"
:::
---
# Aplicação: Braço articulado
:::col
```python
joints = [[100,50],[100,-20],[100,90]]

def setup():
    createCanvas(600, 600)
    angleMode (DEGREES)

def draw_joints (joints):
    for sz,ang in joints:
        rotate(ang)
        rect(0,-5,sz,10)
        translate(sz,0)
    
def draw():
    background(220)
    fill (255,50)
    translate(width/2,height/2)
    draw_joints(joints)
```
:::
:::col
::img src="./joints.png" width="80%"
[link](https://esperanc.github.io/Py5Script/view.html?code=FYewlgdgLgzgBAXjgbWQRgAwYDQFYMC626W2AtAEyHGY4CchBAUEwCYCmAZnDO1AK4AHABQBKAFxM40uAGMATuwCGUdgGElEAG5KYwgGyk4hjKKkzNAcwA27ALIgOcYQBEAogHEASm7cBlMxk5RRV2AH1+MDEWDm5WeSUAdzDQSFhnVOgYCXNpThB5HjCYazAOeWwlYtLyuEg4AC8wERhKnKCgmAbKiEtEIpKy9nkAOh1rfnYxSuqh0fHJ6I6ZeRAoUOErQOW4RVkoYRwyXGwu7Ext5agEiBKNs9NcuDYuOHiksUkggCMlWQBrSyrfgQVjCChUS5wThgazWZwUXAnfBQ66aO6qYSJMpQAAWAHoKNhcewwJZcVBCVD3slMrBhHTsk8XtwFMpVBEou0ZDYQL94a04Eonq0lP1kEQJU98oUwMQzlYCHUIHB2BB+ABbYYbRnc5YwWa1JBs0J+GrDYSYbBUHBoKGdQ3DEaCEAwMBQMAgCDgnBUABUwjAAGo7faZAbBuUxkoJlMumHpDARkpBII1WCI+b5AmhY7CsaQqozXNhGQ0AAOW2V845qqRp0ut0er0+30YAPB0NPIJ1rPR2ObXq15Op9ObPM5phAA)
:::
---
# `push()` e `pop()`

São instruções P5 para salvar e restaurar o estado do sistema de coordenadas e também dos atributos de renderização.
:::col
```python
def setup():
    createCanvas(600, 600)
    background(200)
    translate(width/2,height/2)
    angleMode(DEGREES)
    for ang in range(0,360,20):
        push()
        rotate(ang)
        translate(200,0)
        circle(0,0,40)
        pop()
```
[link](https://esperanc.github.io/Py5Script/view.html?code=CYUwZgBAziAuCuAHAFASgFwCgI4gYwCcQBDWEAYWIDsA3YqZANgAZmAaCF51bXAI2J4A1gHMCAe3hVgyAEyseuCLALUoAG1IhkAdwCWwWAAsA9LLZGQekUdhnFuaiPUgAsuNDIAIgFEA4gBKPj4Ayg44YOIEEE4QelQQqlQi2uwAzCxs8hi8SjiI8FBGaLl5ErBayE7heSpqmmRyrGzcpUp4egR4Lsjs7AAsrXm4iOIoNUpAA)
:::
:::col
::img src="./circles.png" width="80%"
:::
---
:::center
# Obrigado!
:::