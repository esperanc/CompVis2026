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
- $d_l = ||L-P|| \rightarrow$ Distância à luz
- $\vec e = \frac{E-P}{d_e} \rightarrow$ Vetor à câmera 
- $\vec l = \frac{L-P}{d_l} \rightarrow$ Vetor à luz 
- $\vec r \rightarrow$ Vetor reflexão
:::
:::col
::img src="geometria iluminacao.svg" height=85%
:::
---
# Cálculo do vetor de reflexão
:::col
$$
\vec l_{||} = \vec n (\vec l \cdot \vec n) \\
~\\
\vec l_{\perp} = \vec l - \vec l_{||} \\
~\\
\vec r = l_{||} - l_{\perp}\\
~\\
\vec r = 2(\vec l \cdot \vec n)\vec n - \vec l
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
