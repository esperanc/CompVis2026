::: center
# Computação Visual
## Aula 1 - Introdução
::: 
---
::: center
:: image {"src":"areas of modern visual computing.png"}
:::
---
# O que é Computação Visual?

O uso de computação para gerar, analisar e processar dados visuais.

- _Dado visual_ --> qualquer informação que possa ser representada gráficamente.

- A saída de uma computação visual é uma imagem, um vídeo, um gráfico, um mapa, etc.

---
::: center
:: image src="visual computing timeline.png" width=100%
:::
---
# Disciplinas relacionadas:
::: center
:: image src="relacoes.svg" width=80%
:::

---
::: center
# Alguns marcos históricos
:::
---
# 1963 - Sketchpad (Ivan Sutherland):
:::col
- O precursor dos sistemas CAD e interfaces gráficas modernas (GUI). 
- Introduziu a interação direta com a tela usando uma light pen.
- Vejam este [vídeo](https://archive.org/details/AlanKeyD1987) de Alan Kay explicando o Sketchpad
:::
:::col
:: image src="sketchpad.png"
:::
---
# 1969 - Algoritmo de Ray Casting (Arthur Appel): 

:::col
- Primeiro passo em direção ao realismo, calculando a visibilidade de superfícies.
através do disparo de raios
:::
:::col
:: image src="appel_raycasting.jpg"
:::
---
# 1971/1973 - Sombreamento (Gouraud e Phong)
- Henri Gouraud desenvolveu um algoritmo de interpolação de cores para suavizar a iluminação de superfícies poligonais.
- Bui Tuong Phong estendeu a técnica para usar normais para calcular um modelo de iluminação local.
:: image src="phong_shading.png"
---
# 1972 - A Mão de Ed Catmull
:: youtube id=lkHpoCveh4c
---
# 1975 - O Bule de Utah (Martin Newell)
::: col
- Um dos modelos 3D mais icônicos da história.
- Criado para testar algoritmos de renderização.
- Definido matematicamente por curvas de Bézier.
:::
::: col
:: image src="utah_teapot.png"
:::
---
# 1980 - Ray Tracing Recursivo (Turner Whitted)
::: col
- Introdução de reflexões e refrações realistas.
- Modelo de iluminação global que traça o caminho da luz.
:::
::: col
:: image src="ray_tracing.jpg"
:::
---
# 1982 - Tron e Star Trek II
::: col
- **Tron**: Uso pioneiro de CGI extensivo em cinema.
:: image src="tron-1982.jpg"
:::
::: col
- **Star Trek II**: Efeito Genesis -primeira cena 100% gerada por computador.
:: youtube id=Tq_sSxDE32c
:::
---
# 1986 - A Equação de Renderização (Kajiya)
:::col
- James Kajiya publica "The Rendering Equation".
- Unifica modelos de iluminação em uma formulação integral.
- Base para o Path Tracing moderno.
:::
:::col
:: image src="Rendering_eq.png"
:::
---
# 1995 - Toy Story (Pixar)
:::col
- O primeiro longa-metragem totalmente animado por computador.
- Marco na indústria de entretenimento e aceitação de CGI.
:::
:::col
:: image src="toy_story.webp"
:::
---
# 1999 - O Termo GPU (NVIDIA)
:::col
- Lançamento da GeForce 256.
- Hardware dedicado para Transform & Lighting (T&L).
- Início da era moderna das placas gráficas programáveis.
:::
:::col
:: image src="geforce_256.jpg"
:::
--- 
# WebGL (2006)
:::col
- Traz a programação com shaders para a web.
- Protótipo em Canvas introduzido pela Mozilla em 2006.
- Khronos Group define o padrão WebGL 1.0 em 2011
- Em 2017, WebGL 2.0 é lançado, trazendo suporte a mais funcionalidades.
:::
:::col
:: image src="webgl.png"
:::
---
# 2018 - Ray Tracing em Tempo Real
:::col
- Lançamento da arquitetura NVIDIA Turing (RTX).
- Hardware dedicado (RT Cores) viabilizando ray tracing híbrido em jogos.
- Também inclui Tensor Cores para acelerar operações de aprendizado de máquina.
:::
:::col
:: image src="nvidia_turing.jpg"
:::
---
# 2023 - WebGPU (W3C)
::: col
- Sucessor do WebGL para computação gráfica de alta performance na Web.
- **Maio 2023**: Primeira implementação estável no Google Chrome 113.
- **2025**: Lançamento no Firefox 141 e Safari 26.
- Atualmente uma W3C Candidate Recommendation com implementações nativas (Dawn, wgpu).
:::
::: col
:: image src="webgpu.png"
:::
---
:::center
# O que iremos aprender
:::
---
# O pipeline gráfico
- Coordenadas ==> Pixels
- Transformações
- Iluminação
- Texturas
- Shaders
---
# Uma recapitulação de Álgebra Linear
- Vetores
- Matrizes
- Sistemas de coordenadas
- Transformações
---
# Modelagem geométrica
- Curvas e superfícies
- Malhas poligonais
- Modelos paramétricos
- Modelos implícitos
---
# Iluminação
- Luz e cor
- Gouraud / Phong shading
- Modelos de iluminação
- Sombras
- Ray Tracing
- Ray Marching
---
# Processamento de imagens
- Filtros de convolução
    - Média, mediana, etc.
    - Normalização
    - Detecção de bordas    
- Segmentação de imagens
    - Segmentação por thresholding
    - Componentes conexas
---
::: center
# Plataformas para desenvolvimento
:::
---
# Desenho 2D com P5 / Py5Script
- Ferramentas para programação criativa
- P5
    - Processing para JavaScript
    - Página inicial: https://p5js.org
    - Editor online: https://editor.p5js.org
- Py5Script: 
    - Porte do p5 para Python
    - Página inicial: https://github.com/esperanc/Py5Script
    - Editor online: https://esperanc.github.io/Py5Script
---
# Desenho 3D com WebGL
- Usando P5, Py5Script ou outra plataforma Web
- Programação com shaders
---
:::center
# Obrigado!
:::