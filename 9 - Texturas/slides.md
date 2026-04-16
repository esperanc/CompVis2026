::: center
# Computação Visual
## Aula 9 - Texturas
:::
---
# Texturas servem para:
- Simular materiais mais complexos
- Acrescentar detalhes às superfícies sem mexer na geometria
- Armazenar dados que serão usados no cálculo da cor final

::img src="brickwall.png" height=60%
::img src="bookcover.png" height=60%
::img src="embossed.png" height=50%
---
# Mapeamento
:::row
:::col
- Define-se uma parametrização da superfície:
$$
\Large
T = [s,t]^T = f (P) = f([x,y,z]^T)
$$
:::
:::col
- Usa-se as coordenadas $s,t$ para obter as propriedades armazenadas numa imagem
- Semelhante a "embrulhar" um objeto
:::
:::
::img src=cubewrap.png width=50%
---
# Função de "embrulhamento"
:::row
:::col
_Wrapping function_:  $\large P = W(T)$
 - Dado um ponto na textura, encontra-se o ponto correspondente no objeto
:::
:::col
_Inverse wrapping function_:  $\large T = W^{-1}(P)$
 - Dado um ponto no objeto, encontra-se o ponto correspondente na textura
 - Mais útil!
:::
:::
::img src=wrapping.svg width=50%
---
# Superfície paramétrica
- Dois graus de liberdade
$$
\large P(u,v) = \left[\begin{array}{c} x(u,v)\\ y(u,v)\\ z(u,v)\end{array}\right]
$$
- Coordenadas de textura frequentemente baseadas nos parâmetros da superfície
$$
\large
\left[
\begin{array}{c}
s(x,y,z)\\
t(x,y,z)
\end{array}
\right] =
\left[
\begin{array}{c}
s(x(u,v),y(u,v),z(u,v))\\
t(x(u,v),y(u,v),z(u,v))
\end{array}
\right] =
\left[
\begin{array}{c}
s'(u,v)\\
t'(u,v)
\end{array}
\right]
$$
---
# Exemplo: parametrização de uma esfera
$$\large
\begin{array}{c}
x(\phi,\theta) = \sin(\phi) \cos(\theta)\\
y(\phi,\theta) = \sin(\phi) \sin(\theta)\\
z(\phi,\theta) = \cos(\phi)
\end{array} \rightarrow
\begin{array}{c}
\theta(x,y,z) = \operatorname{atan2}(y,x)\\
\phi(x,y,z) = \arccos(z)
\end{array}\rightarrow
\begin{array}{c}
s(\phi,\theta) = \frac{\theta}{2\pi}\\
t(\phi,\theta) = 1- \frac{\phi}{\pi}
\end{array}
$$
::img src=spherewrap.png width=90%
---
# Malhas: Cortar e Deformar
::img src=cutdeform.png width=80%
---
# Corte de uma malha
- Linha de corte se torna uma curva fechada no domínio da texturas
- Problemas: Minimizar deformação e emendas
::img src=cutting.png width=80%
---
# Deformação da malha cortada
- Mapear pontos da malha em pontos do plano
- Minimizar deformação dos triângulos
  - Preservar comprimentos → mapeamento isométrico 
    - Ideal, mas em geral impossível com cortes pequenos
    - Exemplo: faces de um cubo
  - Manter ângulos → mapeamento conformal (rotações e escalas)
    - Bom, mas pode levar a contrações e dilatações indesejáveis
  - Outras abordagens
    - Minimal stretch
    - Barycentric embeddings
    - Harmonic coordinates
---
# Mapeamentos conformais
::img src=conformal.png height=80%
---
:::center
::img src=minstretch.png height=80%
http://graphics.stanford.edu/courses/cs468-10-fall/LectureSlides/12_Parameterization1.pdf
:::
---
# Texturas procedurais
:::col
- Cor dada por uma função $C(s,t)$ ao invés de uma imagem
- Diversas funções interessantes usadas para isso
  - Perlin Noise
  - Simplex Noise 
  - Worley Noise
  - Gradient Noise
  - Padrões regulares
:::
:::col
::img src=proctexture.png height=85%
:::
---
# Gerando texturas com o Fragment Shader
- A geração de texturas pode ser feita dinamicamente usando
shaders, principalmente no esquema "fragment shader only"
- Este é um tópico que vale um curso inteiro!
- Alguns recursos importantes:
  - [Shadertoy](https://shadertoy.com)
  - [The Book of Shaders](https://thebookofshaders.com)
  - [Inigo Quilez](https://iquilezles.org/articles/)
  - [An introduction to Shader Art Coding](https://www.youtube.com/watch?v=f4s1h2YETNY)
- Veja também este [demo Py5Script](https://esperanc.github.io/Py5Script/view.html?sketch=demo/noise_pattern.zip)
---
# Texturas Volumétricas
:::row
:::col
- 3 Coordenadas de textura (s,t,p)
- Texels tridimensionais (_voxels_)
- Usadas para 
  - Imagens médicas
  - Modelar materiais, ex.:
    - Fumaça
    - Nuvens
    - Madeira
    - Mármore
:::
:::col
::img src="volumetexture.gif" height=80%
[Link shadertoy](https://www.shadertoy.com/view/4tK3DV&sa=D&source=editors&ust=1775060656924217&usg=AOvVaw2tbbI9vBxNdFI4sQ8lhlIv)
:::
:::
---
# Texturas com P5.js
:::col
- Carregue com a função `texture(tex)` 
 -  `tex` é um objeto de uma das classes `p5.Image`, `p5.MediaElement`, `p5.Graphics`, `p5.Texture`, `p5.Framebuffer` ou `p5.FramebufferTexture``
- Objetos 3D definidos por funções como `box()`, `sphere()`, etc, já definem coordenadas de textura padrão.
- A cor da textura é _multiplicada_ pela cor computada pelo modelo de iluminação (se ligada)
:::
:::col
:: iframe src="https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hV1AxgE5gCG8YAwiQHYBuJMqAHAAwsA0rHUA6gKIAhAOIAZdDjwBzADYB7AEYlpUZJIm5VUALwFiZMEMIlkACwCW+GFFQAWNuzstxeFZIB0i-AGtJhWYmoQVAByeTMYAEdEMGDnPFU3fDNCfGkwVAAmeyyOAEYAVid1KBkFJQJ5AH1yAA92CsqzaWlEAFti-Cra7V1ScgoTMG95WRrUACJapGJx+oAVQmi43E7qsBq3ZFkYM3gzWWprXLyil1Wmltaeoj7KQeHRiYu22agFpY6q59bN7d396ioY7sADMpzwEFkhAqUDMh3OzTa7FWtWwLjO8jcMHgAE80hMAO5mEDwEyvcbHFjIGrjZbozpY3H48aeHx+AIgWbjAnmci04CgSBQEBGAkYNF4Vm+fyBTJZOlmaAo9aJe5eMBBLDFFxTRDEVCqOlgaRwTBQbV4XX68G4RUNb6qobqzUS9FQaRmSQmeCMI0msCu9HUWQiT3e33FKFheAUA7wPzSDDFPzwfQATVQRhAZhojAgRlalBl8HQdJGY0c4iAA&name=textured_cube" 
:::
---
# Coordenadas de textura em P5.js
:::col
- A função `vertex` usada com `beginShape()`/`endShape`
 tem uma versão
  ```python
   vertex(x,y,z,u,v)
  ```
 - Onde `u,v` são as coordenadas de textura
   - Por default, correspondem às coordenadas de pixel da imagem, isto é `textureMode(IMAGE)`
   - Sugere-se usar `textureMode(NORMAL)` para usar coordenadas normalizadas que variam de 0 a 1
:::
::: col
:: iframe src="https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hV1AxgE5gCG8YAwiQHYBuJMqAHAAwsA0rHUA6gKIAhAOIAZdDjwBzADYB7AEYlpUZJIm5VUALwFiZMEMIlkACwCW+GFFQAWNuzstxeFZIB0i-AGtJhWYmoQVAByeTMYAEdEMGDnPFU3fDNCfGkwVAAmeyyOAEYAVid1KHIADyRiAFlZcFQAOQB5ACVKgEExYrKK9NVxYFBIKBAjAHcMbBdPHz8AoIysuNxZQjD4CllqeD9pDGLCdhN2am0oHPYzrL3ZeH0ADVQABQBJAHpcopc-G-IATVQjEBmGiMCBGAC2lH8m3Qiyg8jAkjM1AAyiZjOkAIoAVVaABEAPrIgAqTSeD1hEGWUDM1OORmoknS1AA1LksMUXDRJCcia0sQAqMwvagcvC0MCEMr-fn4WSMLnodgAWkOhH5MCRqAV7CF1HYHxcYolUrVsvlDMVqvVmu1uvYbOKYECqPRuxcQA&name=textured_quad_strip" 
:::
--- 
# `textureWrap()`
:::col
- Em p5.js, controla o comportamento quando as coordenadas de textura caem fora do intervalo [0,1]

- Admite três constantes para as coordenadas s / t (u/v)

 - `REPEAT` - repete a textura
 - `CLAMP` - trunca as coordenadas no intervalo [0,1] (default)
 - `MIRROR` - espelha a textura
 :::
 :::col
 :: iframe src="https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hV1AxgE5gCG8YAwiQHYBuJMqAHAAwsA0rHUA6gKIAhAOIAZdDjwBzADYB7AEYlpUZJIm5VUALwFiZMEMIlkACwCW+GFFQAWNuzstxeFZIB0EM9OmoA5PLMYAEdEMF9nPFU3GHhCWQBrMB4wM0kTeFQAZgiNdxi4xL95OIB3anD1VzdifAyODkcHNhyqz29UACIS83IOlqjYsxoZMFQARnsJjkz7GenJ5sryAA8kYgBZWXBUADkAeQAldYBBMSWwVcRiVFUWmQUlKBKjZAB9RHYnl9faT+fjV4gCzwSr-N5A2raKAAbw6FBEx3WAAUOph4YikZ8Ogc+Ei+McACqonF4wlY9YASQOB0OqMp1MOAF9Qd9EFCiKRyABlMDSMC1DAsgGINzIWQwMzwMyyajWCbsCYtME-dl6bm8-kZJXfWii8WS6Wy8bzFoQWSEKCJACeUDMsuVEPgbmtjCwlRcypFsmQUplqGtLQ9Orc3t91H9YCt4lAkCgICMJQw2Bcinw8UkcUQ1BAqAATLmnJVzQF4BQZbFZD4WoR2CZ2LKdAWOE32AXKnF4PoABqoJEUgD0ivbsk75AAmqgjECaIwIEYALaUWRZ+DoForNZJF6oB3AgDanuiGtqYBz6AAuux3bhd7UD8G4HyT2fzy15GBJHauSZjKMAIoAKrHAAIq8XIEgcFJIi01CyFyFaFKa5q2raspGNQkijNQADUYxui4LjDFCBLHABABUZj9tQ164LQYCECsk5kfg4qoMM6DsAAtHWhBkRK4bsZwFFUewhYEXgdEMRcTEsYwgk8XxdpsRhHFMMJ1AOC0YDZt+v6Ci4QA&name=textured_wrap_mode"
:::
---
# O processo de mapeamento
::img src=mapeamento.png width=80%
---
# Amostragem de texturas
- Texturas são discretas!
  - Cada pixel da textura é chamado de _texel_
- O valor de uma textura em um ponto $(s,t)$ é dado por um processo de amostragem
- A cor de um pixel na tela pode depender de vários texels
  - Texturas de objetos distantes podem ser comprimidas para uma área de poucos pixels  (filtro de minificação)
  - Texturas de objetos próximos podem ser expandidas para cobrir muitos pixels (filtro de maxificação)
---
# Mipmapping

- MIP $\rightarrow$ _Multum In Parvo_ (muito em pouco)
- Texturas em múltiplos níveis de detalhe
- Versões reduzidas e pré-filtradas da textura em resolução máxima
- Objetivo: escolher uma versão tal que texel $\approx$ pixel

::img src=mipmap.png height=60%
---
# Parâmetros de filtragem em P5.js
:::col
- WebGL permite escolher diversos parâmetros de filtragem

- P5.js assume defaults razoáveis:
    - filtros de minificação e de maxificação lineares

- Os objetos `p5.Texture` também suportam o método `setInterpolation(minfilter,maxfilter)`
  - Não há suporte para mipmaps...

- Para obter o objeto `p5.Texture` correspondente a uma imagem `img` use `_renderer.getTexture(img)`
  -  `P5._renderer` em Py5Script 
:::
:::col
:: iframe src="https://esperanc.github.io/Py5Script/view.html?code=FAEwpgZgBAzmAuBXADgCgJQC5hV1AxgE5gCG8YAwiQHYBuJMqAHAAwsA0rHUA6gKIAhAOIAZdDjzIAlgA8wAGwAiYajCnwAnqgCM4vFADm8gPYAjEvKjIDE3NagBeAsTJghhEsgAWU-DCjMnHqSBgB01MYAyvCExgDWYBi2UBDGhFBSGdRQHtQGiUxYyfqp6QBWWTk0+cxF+vUhoRBS8vKoLBnQqFIA1GXoAKQATA4OHQpwUEMArNPBDfrWoTAAjogkxN3sZey6yeQySMQAssbgqAByAPIASscAgmL7YIeIm9bzhibmlgfPMo4oAAFaahAD6xGo4GIhFC+XgABUXkdEh9-ssEABJajkQjIYzyMhSYzUS58e43PiRBHsC7kynUz5GMwWKAAWyk1Ag7HZJBk3JSYJAvngyQgQpFgIA3gAiOkUqkImWYeUMmlQGUiTGq5Va1UAX2SHK5gKIpHIkQUYHw8CS+mNEFC+LU8GJ2R0HG0LE+bL50CcZtclvk1ttPr9TuMLrdAS97AAzN6xWkoAkNJVxcKbaE04w6gsHaFjMhXSTUGnPvaI8XS6SK8BQJAoCAPAB3DDYfTmfBxAyxRBQ1BDIZJ-RpUzqCgkmIEu14QjsLzsbJOEccNfsEfJWLwVwADVQAFogZiAPRez4AYh3rgAmqgPMKaIwIB42ZRjAP4KeACzoT7yFIBhePAebJJeByhFIMCKFIhCaICCKEIgYDonA8DYri+KErWqCZiKADahZwCGNpgCAGAALrsMUJQSjaRERiRobkVRnylBklS5DUhSdgsAJOCCoS+mgUjsBwADs7CHhua6VngHEVJyVR5AU+YLHgABegJCSJqA7JJPIbjJbCjhpkiIDAXhzuZUAxM+OGJDI4nsJp8kNKYxgyKg0xmbZ+JoOIyRAA&name=texture_filter"
:::
---
# Texturas e shaders
:::col
- Texturas são acessadas através de uniforms to tipo `sampler2D`
- Use o método `setUniform(name,img)` para passar a textura
  - `name` é o nome do uniform no shader
  - `img` é um objeto `p5.Image`, `p5.Texture`, `p5.Graphics`, `p5.Framebuffer` ou `p5.FramebufferTexture` correspondente à imagem
- O shader pode então usar a função `texture2D(tex,uv)` para obter a cor da textura no ponto `uv` (tipo `vec2`)
  - Em webGL 2, use `texture(tex,uv)`
:::
:::col
:: iframe src="https://esperanc.github.io/Py5Script/view.html?zip=KoUQzgIgQggg9jRSCSBqAlgcwDYHcBuAtgAyYCaAagIrKIBiwAwkgFJIwDGATAC7YAmAcQBycADIA7KAFZGhAErYAWuii4OhCmABGXOgGsA0o30A2RuhiZkjKBO2CAnOjIB1XJm0ANbADNuABYBSoIUAJ4WVjZQPACmFI4AXgCGggZKXsiYAAoAylA6evrAXEEh4TaY6PyaYfyM0vYAEsJgyOgeyIRKYW4cAK5KXAAeidqMyAAOkda29k4u7pjJrgCMEgCyuR4r6xuYcLNWu5u5MI7IgsP4bvIs2q50Ekq5VclN8sQcTRumYmGOXArYSJfiuYj9DiCAL4IRJMRcbD6MSJEDEFHIVbCdBTGbRSYPDhhZAQUgORzBEDYHhufjYYwsOD8D7qRJwfBiADMUEmZE5wlW2ly0iBTmI2k5G3wKyo+A2ABUOHKAFYldpGGxRZhHHVyRQqKCJDLyVYcRiYSYAeQOOr5LGwZC8iioen6NToiUMEEwuA2jA8logMFwYlsTuALCa8pMxgUylU+g0dE5xjMeNsi2EACclJyWLDXNIjEHppZZmolMwLk0ebFQmB5KFIYjiLFXqWtTF4klUulMs2KMQKIXJkpCI4wkK3hR7dxHGB+E6CVwACzoUNQACOHFWFI4EhYATbAW0-ER+iEmG3gioYFSFFHpWIhik+i8uX0Vtwh01nh8-lKYJQjCSRhAEOgKH6FYlHwDRiDgLpsGAXZsHaDwHmwHRBGwT0TDleVgz9fQAHZ0y7BIUjSfQMmQAchxHMcJynapQhXLZkDabCeCUVEO3LOIKN7aj+24Qdh2kUdx0nV4WIoNicU46keNxMtokovtkDgbw-ECIDwkMKgf21bRx3lZl82SLhgDgAyjKsKFhhPQhrMDYMxG9X0Y1ASBYAQdgYDQLA8FiKBGH5fBcCQMQAA52DYJAanCepGm0Fo2k5JRsH3YRlxXTANkSYNLgoRI5GwfpkCaTKyESfZKCgWCWxWRx+ktXBJkFQhsEICUWB4S5VgCfgICoTB+AoKBJy4SYHU5eRl2kYRHXkMJki8TBSIkSDoNgkhPEeYhhFsVZ5VcRxqNcYZXBWChOVOugvi6lc2psmpHFHWwaVccrU0wWJv2sQR+DALxVga7hsGIZqKtJMaJqmma+Xm3RFuW1b1swQxVBOs6Lqum67oOjRsBXGxDkS5UjqCYAnBSJddBXNoIBAfoiM21YqG2DYQHNfyYGVUxjC8MQbIgAB6S1iBgKhEB4GAQCQfQkCgQgkwkMRCGB7hcGVRKwgh-BtEsWqg0wDINmMKQwiUVwcoNo2oDgFZ+DgM0VfJIaIDAQwJUHSrqsSUalAPYJDsNpwwjajqTO63r+qqh1EiyZIZyyrh50XZHV027bXBguCzcIa5HVGlPkdcYAc6gvPdtIbg6B4BysuVFgQEqxRYmZqudoL+vG6uZvW-b7BO+QUiLS4XQkQGgIVhXGz8lI1TbC4G2NmJFpiBJUghmGXx5BDpQw965EJACaQEWwXIMmEQ2mkHaHJHPl6dQpo6oGVLZzmH2IPlNZymSsS2MMVerh16GE3pIDYYAtgrkbpyKgboTBfjsmNTQlNbCf0sNWDuf8NDWSEHJDY6AQFrzCBA4Q6JNgwNyHAjgCCkGfhfr+McxcvCjTcMMUUIAcj5FVoQOgutGABEmBQLiLxoronQPoTcxCVxL07KOSwcBOHcNQLAyYlw6BgChEEbe+V0BwNUakEACjyz8KeC6ecEosh5CsDVHhWMoAnhrCos4WZohYJgJuSowwxDoEGqlR2ZAPybWfN5WAAQZa838gLIWjBUBCmcRQKwiBqC0EQErPm2ScktBzE6ZUyQGi4HiFAMQ0tkDAEQH5dggUcAlNCuFSKiAYpxRye0pouBmAwCgKvLwLB0Sax0SMTmuAeZ0EQIYPmjBshwDgCwAYBxsjRWIlQWAMBGBSxlhs7Z7T-JQEsM04Oh4egpTSt5OgUBMD+SDDADYMBJi7NJBM-yABeV5QA&name=tex_shader"
---
:::col
# Coordenadas de textura no shader
- O atributo `aTexCoord` já é passado para formas 3D comuns como sphere, cube, etc
 - Vertex shader tem que passar como varying para o 
   fragment shader
```glsl
attribute vec2 aTexCoord;
varying vec2 vTexCoord;
void main() {
  ...
  // Pass along texture coordinates
  vTexCoord = aTexCoord;
  ...
}
```
:::
:::col
:: img src=textured_globe.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https://esperanc.github.io/CompVis2026/9%20-%20Texturas/textured_globe.zip)
:::
---
# Outros usos para texturas
- Nem sempre texturas carregam informação de cor.
  - Podem carregar informação de altura (bump maps)
  - Podem carregar informação de normal (normal maps)
  - Podem carregar informação de especularidade (specular maps)
---
# Bump maps e normal maps
- Permitem simular relevos na superfície sem aumentar a complexidade geométrica
- O relevo só fica aparente sob iluminação
  - A geometria continua suave
- Bump maps são mais comuns pois são mais fáceis de gerar
- Normal maps são mais eficientes pois não precisam de cálculo de gradiente
---
# Bump maps
:::col
- Textura contém informação de altura 
  - Tipicamente uma imagem em preto e branco 
  - Preto = baixo, Branco = alto
- Para inferir uma perturbação da normal em um ponto, precisamos comparar a altura do ponto com a altura dos seus vizinhos, ou seja, o gradiente de $h$
 - Se $h(u,v)$ é a altura do terreno no texel $u,v$
 $$
 \Delta h =  \left( \frac{\partial h}{\partial u}, \frac{\partial h}{\partial v} \right)
 $$
 :::
 :::col
 ::img src=bump_gradient.svg
 :::
---
# Sistemas de coordenadas do bump map
:::col
- Para "colar" a textura num ponto da superfície é preciso mapear o sistema de coordenadas da textura para o sistema de coordenadas do objeto
  - "Para cima" da textura $\leftrightarrow$ direção normal da superfície
  - Os outros vetores da base devem estar alinhados com as direções de $u$ e $v$ da textura. Se $P$ é um ponto da superfície, então
$$
  T =\frac{\partial P}{\partial u},\,
  B =\frac{\partial P}{\partial v}
$$
 - São os chamados vetores _tangente_ e _bitangente_
:::
:::col
::img src=bump_frame.svg
:::
---
# Derivadas no shader
:::row
- As funções $dFdx(p)$ e $dFdy(p)$ calculam as derivadas parciais de $p$ em relação a $x$ e $y$ no espaço de tela
- Usando a regra da cadeia, podemos calcular os vetores tangente e bitangente no espaço do objeto
:::
:::col
Para o gradiente de altura $h(u,v)$:
$$
\begin{array}{c}
\large
\frac{\partial h}{\partial x} = \frac{\partial h}{\partial u} \frac{\partial u}{\partial x} + \frac{\partial h}{\partial v} \frac{\partial v}{\partial x}
\\ 
\\
\frac{\partial h}{\partial y} = \frac{\partial h}{\partial u} \frac{\partial u}{\partial y} + \frac{\partial h}{\partial v} \frac{\partial v}{\partial y}
\end{array}
$$
(Queremos isolar $\frac{\partial h}{\partial u}$ e $\frac{\partial h}{\partial v}$)
:::
:::col
Para a tangente e bitangente:
$$
\large
\begin{array}{c}
\frac{\partial P}{\partial x} = T \frac{\partial u}{\partial x} + B \frac{\partial v}{\partial x}
\\
\\
\frac{\partial P}{\partial y} = T \frac{\partial u}{\partial y} + B \frac{\partial v}{\partial y}
\end{array}
$$
:::
---
# Calculando $T$ e $B$
- Primeiro obtemos dois vetores tangentes quaisquer
```glsl
vec3 dp1 = dFdx(gl_FragCoord.xyz);
vec3 dp2 = dFdy(gl_FragCoord.xyz);
vec3 dp2perp = cross(dp2, N);
vec3 dp1perp = cross(N, dp1);
```
- Obtemos as derivadas de tela das coordenadas de textura
```glsl
vec2 duv1 = dFdx(vTexCoord);
vec2 duv2 = dFdy(vTexCoord);
```
- Agora podemos isolar $T$ e $B$
```glsl
vec3 T = normalize(dp2perp * duv1.x + dp1perp * duv1.y);
vec3 B = normalize(dp2perp * duv2.x + dp1perp * duv2.y);
```
---
# Calculando a normal perturbada
- Coeficientes do gradiente da altura
```glsl
float dhx = dFdx(h);
float dhy = dFdy(h);
```
- Aplicando o gradiente da altura em coordenadas de objeto
```glsl
vec3 grad = T * dhx + B * dhy;
vec3 bumpedNormal = normalize(N - grad * bumpScale);
```
---
:::row
::img src=bumpmap.png width=40%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https://esperanc.github.io/CompVis2026/9%20-%20Texturas/bumpmap.zip)
:::
---
:::center
# Obrigado!
:::