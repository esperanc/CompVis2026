::: center
# Computação Visual
## Aula 8 - Iluminação
:::
---
# Luz
Radiação eletromagnética no espectro visível (380 - 700 nm)
::img src="luzvisivel.webp" height=65%
---
# Cor
Sensação provocada pela luz (fenômeno psico-físico)
- Depende de como a luz é capturada (olho/câmera)
- Espaço de dimensão 3 
  -3 tipos de células “cone” na retina
- Várias distribuições espectrais são percebidas como a mesma “cor”
::img src="cones.jpg" height=50%
---
# Modelos de iluminação
- Modelam cor, não luz
- Mais barato computacionalmente
- Objetivo = modelar imagens digitais
- Assumem situação de iluminação normalizada
  - Abertura do diafragma / pupila
  - Tempo de exposição, sensibilidade do filme / CCD
- Aproximações mais ou menos grosseiras dos fenômenos de interação entre a luz e os objetos materiais
---
# Interações Luz-Superfície
::img src="fenomenos.png" width=100%
---
# Modelos locais
:::col
- Luz direta refletida num objeto
- Luz emitida por um objeto
- Não ilumina outros objetos
- Desconsidera sombras
- Ex: modelo de Phong
:::
:::col
::img src="ilum local.svg" height=85%
:::
---
# Modelos globais
:::col
- Luz refletida indiretamente
- Luz refratada
- Luz transmitida
- Outros fenômenos
- Ex.: Ray tracing, Photon mapping
:::
:::col
::img src="ilum global.svg" height=85%
:::
---
# Cálculo por vértice / fragmento
:::col
### Por vértice
- Modelo é calculado para cada vértice
- Cor resultante é interpolada pelo rasterizador
- OpenGL "antigo"
- Conhecido como “Gouraud Shading”
:::
:::col 
### Por fragmento
- Propriedades geométricas calculadas por vértice
  - Ex: normal, posição em coordenadas do mundo
- Propriedades interpoladas pelo rasterizador
  - Coordenadas baricêntricas
  - Modelo é calculado por fragmento
  - "Phong shading"
  - P5 faz isso por default.
:::
---
# Geometria da iluminação
:::col
- $P \rightarrow$ Ponto da superfície
- $\vec n \rightarrow$ Vetor normal
- $L \rightarrow$ Posição da luz
- $E \rightarrow$ Posição da câmera
- $d_e = ||E-P|| \rightarrow$ Distância à câmera
- $d_\ell = ||L-P|| \rightarrow$ Distância à luz
- $\vec e = \frac{E-P}{d_e} \rightarrow$ Vetor à câmera 
- $\vec \ell = \frac{L-P}{d_{\ell}} \rightarrow$ Vetor à luz 
- $\vec r \rightarrow$ Vetor reflexão
:::
:::col
::img src="geometria iluminacao.svg" height=85%
:::
---
# Cálculo do vetor de reflexão
:::col
$$
\Large \vec \ell_{||} = \vec n (\vec \ell \cdot \vec n) \\
~\\
\vec \ell_{\perp} = \vec \ell - \vec \ell_{||} \\
~\\
\vec r = \ell_{||} - \ell_{\perp}\\
~\\
\vec r = 2(\vec \ell \cdot \vec n)\vec n - \vec \ell
$$
:::
:::col
::img src="reflection vector.svg" height=85%
:::
---
# Modelo de Phong

- Fontes de luz pontuais, direcionais ou spots
- Modela reflexão e atenuação
- Luz refletida calculada como a soma de 3 parcelas
    - Reflexão direta _**difusa**_ (objetos foscos)
    - Reflexão direta _**especular**_ (objetos polidos)
    - Reflexão _**ambiente**_ (luz indireta)
- Atenuação leva em conta distância entre ponto iluminado e fonte de luz
    - Afeta apenas as componentes difusa e especular
- Opcionalmente, adiciona-se uma componente _**emissiva**_
    - Modela objetos que emitem luz (mas não iluminam outros objetos)
---
# Cores no modelo de Phong

- Cores são dadas pelas propriedades da fonte luminosa e do material do objeto:
  - $L \rightarrow$ cor da luz
  - $C \rightarrow$ cor do objeto
  - $\rho \rightarrow$ coeficiente de atenuação
- Codificadas em vetores RGB com coordenadas no intervalo [0,1]
- Multiplicação de cores significa modulação
  - Ex: luz branca (1,1,1) multiplicada por cor de material vermelho (1,0,0) resulta em cor vermelha (1,0,0)
  - Ex: luz amarela (1,1,0) multiplicada por cor de material azul (0,0,1) resulta em cor preta (0,0,0)
---
# Reflexão difusa
- Também chamada _lambertiana_ (lei de Lambert)
- Assume que o material é perfeitamente fosco
  - Espalha luz incidente em todas as direções
- Intensidade proporcional ao cosseno do ângulo entre a luz e a normal: $\vec n \cdot \vec \ell$
- Nula se luz vem "por trás": $\vec n \cdot \vec \ell < 0$

::img src="reflexao difusa.svg" height=50%
---
# Componente de reflexão difusa
- $C\rightarrow$ cor do material
- $L \rightarrow$ cor da luz
- $\rho_d \rightarrow$ coeficiente de reflexão difusa
$$
\huge I_d = \max(0, \vec n \cdot \vec \ell) \, C\, L\, \rho_d
$$
---
# Reflexão especular
- Proporcional ao cosseno do ângulo entre $\vec r$ e $\vec e$
- Depende da posição do observador
::img src="iluminacao especular.svg" height=70%
---
# Componente de reflexão especular
- $\large L \rightarrow$ Cor da luz
- $\large \vec e \rightarrow$ Vetor da câmera
- $\large \vec r \rightarrow$ Vetor de reflexão ideal
- $\large \rho_s \rightarrow$ Coeficiente de reflexão especular
- $\large \alpha \rightarrow$ Expoente de Phong (_shininess_)
$$
\huge I_s = \max(0, \vec e \cdot \vec r)^\alpha \, L \, \rho_s
$$
---
# Shininess
- Controla o tamanho do _highlight_ especular
::img src="grafico shininess.png" height=70%
---
# Atenuação
- Modela a intensidade da luz em função da distância à fonte
- Coeficiente de atenuação quadrática:

$$
\Large
\mathrm{Aten} = \frac{1}{a_0 + a_1 d_\ell + a_2 d_\ell^2}
$$

Onde 
 - $\Large d_\ell = ||L-P||$ e
 - $\Large a_i$ são os coeficientes de grau $i$
---
# Reflexão ambiente
- Modela luz indireta
- Assume que a luz é espalhada uniformemente no ambiente
- Não sujeita à atenuação
- Normalmente uma fração pequena da iluminação total
$$
\huge I_a = C \, L \, \rho_a
$$
Onde:
- $\large C \rightarrow$ Cor do objeto
- $\large L \rightarrow$ Cor da luz
- $\large \rho_a\rightarrow$ coeficiente de reflexão ambiente
---
# Emissão
- Luz constante emitida pelo objeto
- Independe de fontes luminosas
- Não ilumina outros objetos
$$
\huge
I_e = C \rho_e
$$
Onde
- $\large C \rightarrow$ cor do objeto
- $\large \rho_e \rightarrow$ coeficiente de emissão
---
# Modelo completo
Para uma luz:
$$
\Large
I = I_e + I_a + \frac{1}{a_0 + a_1 d_\ell + a_2 d_\ell^2} ( I_d + I_s )
$$

Para múltiplas luzes:
$$
\Large
I = I_e  + \sum_{i=1}^n I_{a_i} + \frac{1}{a_{i,0} + a_{i,1} d_{\ell_i} + a_{i,2} d_{\ell_i}^2} ( I_{d_i} + I_{s_i} )
$$
---
# Fonte luminosa direcional
:::col
- Fontes de luz distantes
- Ao invés de uma posição, tem-se o vetor $\vec \ell$ diretamente
- Não suporta atenuação
:::
::: col
::img src="fonte direcional.svg" height=85%
:::
---
# Fontes Spotlight
:::col
- Fontes pontuais com iluminação mais intensa 
numa direção $\vec v$ dada
- A intensidade diminui conforme o ângulo entre $\vec v$ e $\vec \ell$ aumenta
$$
\large
L'= (\vec v \cdot \;- \vec \ell) ^\beta L
$$
- Pode-se especificar um ângulo máximo $\theta$ além do qual a iluminação é nula, i.e., 
$$ 
\large
\vec v \cdot \; - \vec \ell < \cos \theta
$$
:::
:::col
:: img src="fonte spotlight.svg" height=85%
:::
---
# Modelo de Phong no P5
### Propriedades de material
| Componente | P5 | Descrição |
| --- | --- | --- |
| Difusa + Ambiente | `ambientMaterial()` | Define a cor principal. Ela reage à ambientLight (ambiente) e a luzes direcionais/pontuais (difusa). |
| Difusa (Alternativa) | `fill()` | Define a cor difusa básica se nenhum ambientMaterial for declarado. |
| Especular (Cor) | `specularMaterial()` | Define a cor do brilho (o highlight). Geralmente configurado como branco (255) ou cinza claro. |
| Especular (Expoente) | `shininess()` | Controla o quão concentrado é o reflexo. |
| Emissiva | `emissiveMaterial()` | Adiciona uma cor constante que não depende de nenhuma fonte de luz externa. |
---
# Modelo de Phong no P5
## Fontes luminosas

- `directionalLight(color, direction)`
- `pointLight(color,position)`
- `spotLight(color, position, direction, angle, concentration)`
- `ambientLight(color)`
- `lightFalloff(constant, linear, quadratic)` (atenuação)

Onde 
- `color` é um objeto p5.Color (função `color()`)
- `position` e `direction` são objetos p5.Vector (função `createVector()`)
- Esses argumentos também podem ser substituidos por coordenadas. Ex: `directionalLight(255, 0, 0, 0, -1, 0)`
- `angle` é a abertura do cone de luz em radianos
- `concentration` é o quão suave é a queda da luz nas bordas do cone (o "falloff")
---
::: center
# Demo Iluminação
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https://esperanc.github.io/CompVis2026/8%20-%20Ilumina%C3%A7%C3%A3o/ilumination_demo.zip)
:::
---
::: center
# Obrigado!
:::