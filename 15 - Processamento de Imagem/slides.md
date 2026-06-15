:::center
# Computação Visual
## 15 - Processamento de Imagem
:::
---
# A imagem digital
:::col width=58%
- Uma imagem é uma função $f(x,y)$ que dá a **intensidade** (ou cor) em cada ponto do plano
- A imagem **digital** é essa função **amostrada** numa grade e **quantizada** em níveis discretos:
$$
f[m,n], \quad m=0\ldots M\!-\!1,\ n=0\ldots N\!-\!1
$$
- Cada amostra é um **pixel**; cores são tipicamente 3 canais (RGB)
- Duas resoluções independentes:
  - **espacial** — número de pixels ($M\times N$)
  - **de intensidade** — número de níveis por canal
:::
:::col width=42%
- _Processamento de imagem_: a entrada **e** a saída são imagens
  - distinto de _visão computacional_ (imagem → descrição) e de _síntese_ (modelo → imagem)
- Operações:
  - **ponto a ponto** (cada pixel isolado)
  - **locais** (vizinhança / filtros)
  - **globais** (toda a imagem)
:::
---
# O problema da amostragem
:::col width=55%
- Converter o sinal **contínuo** numa grade discreta perde informação
- Se a grade é **grossa** demais para os detalhes da cena, surgem **artefatos**:
  - serrilhado (_jaggies_), padrões de **Moiré**
- A taxa de amostragem precisa ser compatível com a **frequência** presente no sinal
:::
:::col width=45%
- Resolução espacial insuficiente $\Rightarrow$ detalhes finos viram **falsos** padrões grosseiros
- O mesmo problema aparece na renderização (antialiasing)
:::
---
# Aliasing e o teorema de Nyquist
:::col width=52%
- **Teorema da amostragem (Nyquist–Shannon)**: para reconstruir um sinal sem perdas, a taxa de amostragem deve ser
$$
f_s > 2\, f_{\max}
$$
- Abaixo disso ocorre **aliasing**: frequências altas se "disfarçam" de frequências baixas
- **Solução**: filtrar (borrar) **antes** de amostrar, removendo o que está acima de $f_s/2$ (_pré-filtragem_)
:::
:::col width=48%
::img src=sampling_aliasing.png height=70%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fresampling.zip)
:::
---
# Reconstrução e reamostragem
:::col width=58%
- Para **redimensionar**, é preciso estimar valores entre as amostras (interpolação):
  - **Vizinho mais próximo** — rápido, "blocado"
  - **Bilinear** — média ponderada dos 4 vizinhos
  - **Bicúbica** — 16 vizinhos, mais suave
- Ao **reduzir** (_downsampling_), pré-filtrar é essencial, senão, aliasing
- Ao **ampliar** (_upsampling_), a interpolação controla a suavidade vs. nitidez
:::
:::col width=42%
::img src=resampling.png height=70%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fresampling.zip)
:::
---
# Quantização de cores
:::col width=50%
- Limitar o número de **níveis** por canal: com $b$ bits há $L = 2^b$ níveis
$$
q(v) = \frac{\operatorname{round}\!\big(v\,(L-1)\big)}{L-1}
$$
- Poucos níveis $\Rightarrow$ **banding** (faixas visíveis) em gradientes suaves
- 8 bits/canal (24 bits RGB) costuma bastar para fotos; menos exige cuidado
:::
:::col width=50%
::img src=quantization.png height=70%
:::
---
# Paletas e cor indexada
:::col width=58%
- **Cor indexada**: cada pixel guarda um índice numa **paleta** (tabela) de poucas cores
  - economiza memória (ex.: GIF, sprites)
- Escolher a melhor paleta = **quantização adaptativa**:
  - **Median cut** — divide recursivamente a caixa de cores
  - **Popularidade** — cores mais frequentes
  - **Octree** — funde cores próximas numa árvore
:::
:::col width=42%
- O **erro de quantização** é a distância entre a cor original e a cor da paleta
- Reduzir a paleta degrada a imagem… a menos que distribuamos o erro: **dithering**
:::
---
# Dithering
:::col width=52%
- Ideia central: **trocar resolução no espaço de cores por resolução espacial**
- O olho **integra** pequenas regiões — um padrão de pixels de poucas cores parece, à distância, uma cor intermediária
- Permite simular muitos tons com uma paleta minúscula (até 1 bit!)
- É o princípio do **halftone** da impressão (pontos de tinta)
:::
:::col width=48%
::img src=dithering.png height=42%
- A imagem 1-bit com difusão de erro preserva muito mais detalhe que o limiar simples
:::
---
# Dithering ordenado (matriz de Bayer)
:::col width=56%
- Usa uma **matriz de Bayer**: um pequeno mapa de **limiares** $n\times n$, **ladrilhado** (repetido) sobre toda a imagem
- Cada pixel é comparado ao limiar da **sua posição** na matriz: valor $\ge$ limiar → aceso; senão → apagado
- Os valores $0,\ldots,n^2\!-\!1$ são dispostos de forma **maximamente dispersa** — posições vizinhas recebem limiares bem diferentes → textura fina, sem agrupamento
- Construída **recursivamente** a partir de $M_2=\begin{bmatrix}0&2\\3&1\end{bmatrix}$:
$$
\small
M_{2n} = \begin{bmatrix} 4M_n & 4M_n + 2 \\ 4M_n + 3 & 4M_n + 1 \end{bmatrix}
$$
:::
:::col width=44%
- Exemplo $4\times4$ (limiar = valor$/n^2$):
$$
\scriptsize
\frac{1}{16}\begin{bmatrix}
0 & 8 & 2 & 10 \\
12 & 4 & 14 & 6 \\
3 & 11 & 1 & 9 \\
15 & 7 & 13 & 5
\end{bmatrix}
$$
- **Rápido** e paralelo (cada pixel é independente), mas deixa um **padrão regular** perceptível
:::
---
# Dithering por difusão de erro
:::col width=55%
- **Floyd–Steinberg**: quantiza um pixel e **espalha o erro** de quantização para os vizinhos **ainda não processados**, percorrendo a imagem em varredura
- Pesos de distribuição do erro ($*$ = pixel atual):
$$
\small
\begin{array}{ccc}
 & * & \tfrac{7}{16} \\
\tfrac{3}{16} & \tfrac{5}{16} & \tfrac{1}{16}
\end{array}
$$
- Resultado mais "orgânico" e de **melhor qualidade** que o ordenado, mas **serial** (depende da ordem de varredura)
:::
:::col width=45%
::img src=dithering.png height=42%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fdithering.zip)
:::
---
# Dithering em shader
:::col width=52%
- Num **fragment shader**, cada pixel é processado de forma **independente e paralela**
- Por isso a **difusão de erro não cabe** num shader: é **serial** (cada pixel depende do erro propagado dos vizinhos já visitados)
- Já o **dithering ordenado** é ideal: basta comparar o pixel a um **limiar lido por posição** — totalmente paralelo
- Trocando o **mapa de limiares** da matriz de Bayer por outros, melhora-se muito a qualidade:
  - **ruído branco** (limiar aleatório por pixel): barato, mas granuloso
  - **ruído azul** (_blue noise_): o melhor visualmente
  - **IGN**: ruído azul aproximado, **sem textura**
:::
:::col width=48%
::img src=dither_masks.png height=42%
- A matriz de Bayer tem estrutura **regular** (e de baixa frequência) que o olho percebe; o ruído azul a dissolve
:::
---
# Ruído azul e IGN
:::col width=54%
- **Ruído azul** (_blue noise_): mapa de limiares com energia concentrada em **altas frequências** — sem agrupamentos de baixa frequência, padrão quase "invisível"
  - gerado **offline** (ex.: _void-and-cluster_) e amostrado como textura **ladrilhável**
  - pode ser **animado no tempo** para casar com TAA (anti-aliasing temporal)
- **Interleaved Gradient Noise** (IGN, Jimenez): hash analítico, **sem textura**:
$$
\scriptsize
\mathrm{ign}(x,y)=\operatorname{frac}\!\big(52.9829189\cdot\operatorname{frac}(0.06711\,x + 0.00584\,y)\big)
$$
- Usos em GPU: quebrar **banding** (HDR→8 bits), **transparência estocástica** (_alpha-test_ / _screen-door_), suavizar gradientes
:::
:::col width=46%
::img src=dither_shader_compare.png height=42%
- Mesmo algoritmo (limiar por pixel), só muda o mapa: o ruído azul e o IGN são bem menos "padronizados" que o Bayer
:::
---
# Histograma
:::col width=50%
- O **histograma** conta quantos pixels há em cada nível de intensidade
- Revela, num relance:
  - **exposição** (concentração à esquerda = escura; à direita = clara)
  - **contraste** (espalhamento dos valores)
  - sub/super-exposição (acúmulo nos extremos)
- É a base de várias correções **ponto a ponto**
:::
:::col width=50%
::img src=histogram.png height=72%
:::
---
# Brilho e contraste
:::col width=55%
- Transformações **ponto a ponto**: a saída de um pixel depende só do seu valor
$$
g = \alpha\, f + \beta
$$
  - $\beta$ desloca o **brilho**
  - $\alpha$ (ganho) ajusta o **contraste**
- **Alongamento de contraste** (_stretching_): mapeia o intervalo usado $[v_{\min}, v_{\max}]$ para todo o $[0,1]$
- Operações genéricas via **LUT** (_look-up table_): uma tabela de $f \mapsto g$
:::
:::col width=45%
- O alongamento "abre" um histograma comprimido, usando toda a faixa dinâmica
- Cuidado: realça também o **ruído**
:::
---
# Equalização de histograma
:::col width=55%
- Objetivo: redistribuir as intensidades para um histograma **aproximadamente uniforme** → maximiza o contraste global
- Usa a **função de distribuição acumulada** (CDF) como mapeamento:
$$
s = T(r) = (L-1)\,\mathrm{CDF}(r)
$$
- Automática, sem parâmetros; ótima para imagens "apagadas"
- Variante local: **CLAHE** (equalização adaptativa com limite de contraste)
:::
:::col width=45%
::img src=histogram.png height=72%
:::
---
# Correção de gama
:::col width=52%
- A relação entre valor do pixel e luminância **não é linear** — em monitores e na percepção humana
$$
s = c\, r^{\gamma}
$$
- $\gamma < 1$ clareia (realça sombras); $\gamma > 1$ escurece
- Essencial para exibir cores corretamente (espaço **sRGB** ≈ $\gamma \approx 2.2$)
- Operações de iluminação/_blending_ devem ser feitas em espaço **linear** (descodificar gama antes, recodificar depois)
:::
:::col width=48%
::img src=gamma.png height=55%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fhistogram.zip)
:::
---
# Filtragem espacial: convolução
:::col width=50%
- Filtros **locais**: cada pixel de saída combina sua **vizinhança** com um **kernel** (janela, ex. 3×3)
$$
g(x,y) = \sum_{i,j} K(i,j)\, f(x-i,\, y-j)
$$
- A janela "desliza" por toda a imagem
- Nas **bordas** da imagem: estender, espelhar ou zerar
- Se $\sum K = 1$, o brilho médio se mantém
:::
:::col width=50%
::img src=convolution_diagram.png height=60%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fconvolution.zip)
:::
---
# Suavização (smoothing)
:::col width=52%
- **Borra** a imagem, reduzindo ruído e detalhes finos
- **Média (box)** — todos os pesos iguais ($\tfrac19$ num 3×3)
- **Gaussiano** — pesos seguem uma gaussiana; mais natural, separável e sem "toques" de frequência
$$
\small
\frac{1}{16}\begin{bmatrix}1&2&1\\2&4&2\\1&2&1\end{bmatrix}
$$
- Trade-off: mais suavização $\Rightarrow$ mais borramento das bordas
:::
:::col width=48%
::img src=convolution.png height=42%
:::
---
# Realce (sharpening)
:::col width=55%
- Realça **transições** (bordas/detalhes) usando a 2ª derivada — o **Laplaciano**
$$
\small
\nabla^2 = \begin{bmatrix}0&-1&0\\-1&4&-1\\0&-1&0\end{bmatrix}
$$
- **Unsharp masking**: subtrai uma versão borrada e soma de volta a diferença
$$
g = f + \lambda\,(f - \mathrm{borrada}(f))
$$
- $\lambda$ controla a intensidade do realce (_high-boost_)
:::
:::col width=45%
- Realça também o **ruído** — frequentemente precede uma leve suavização
- Imagem "realce (unsharp)" no slide de convolução
:::
---
# Detecção de bordas
:::col width=52%
- Bordas = **variações bruscas** de intensidade → 1ª derivada (gradiente) alta
- **Sobel / Prewitt**: kernels que estimam $G_x$ e $G_y$
$$
\small
G_x=\begin{bmatrix}-1&0&1\\-2&0&2\\-1&0&1\end{bmatrix}\quad
|\nabla f| = \sqrt{G_x^2 + G_y^2}
$$
- Sobel sozinho dá bordas **grossas e ruidosas** → o detector de **Canny** as refina (próximo slide)
:::
:::col width=48%
::img src=edges.png height=42%
:::
---
# O detector de Canny
:::col width=50%
Considerado o detector de bordas "ótimo" (Canny, 1986). Cinco passos:
1. **Suavização gaussiana** — reduz o ruído que o gradiente amplificaria; o $\sigma$ define a **escala** das bordas
2. **Gradiente** — magnitude $|\nabla f|$ e **direção** $\theta=\operatorname{atan2}(G_y,G_x)$ (via Sobel)
3. **Supressão de não-máximos** — mantém o pixel só se for **máximo local** da magnitude **na direção do gradiente** → bordas de **1 pixel**
:::
:::col width=50%
4. **Duplo limiar** — $T_{baixo} < T_{alto}$: acima de $T_{alto}$ = borda **forte**; entre os dois = **fraca**; abaixo = descartada
5. **Histerese** — uma borda **fraca** só é mantida se estiver **conectada** a uma borda forte (segue-se a cadeia) → remove ruído isolado, preserva contornos contínuos
- Resultado: bordas **finas, conectadas e com poucos falsos positivos**
:::
::img src=canny_steps.png height=30%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fimage_filters.zip)
---
# LoG e DoG
:::col width=50%
- **LoG — Laplaciano do Gaussiano** (Marr–Hildreth): suaviza com Gaussiano e aplica o **Laplaciano** (2ª derivada), num único núcleo
$$
\small
\nabla^2 (G_\sigma * f) = (\nabla^2 G_\sigma) * f
$$
- Núcleo em **"chapéu mexicano"** (centro × entorno)
- Bordas = **cruzamentos por zero** da resposta; $\sigma$ define a **escala**
:::
:::col width=50%
- **DoG — Diferença de Gaussianas** *aproxima* o LoG subtraindo dois borramentos:
$$
\small
\mathrm{DoG} = G_{\sigma_1} * f - G_{\sigma_2} * f, \quad \sigma_2 \approx 1.6\,\sigma_1
$$
- Justificativa: $\dfrac{\partial G}{\partial \sigma} \approx \sigma\,\nabla^2 G$ → a diferença de escalas próximas $\approx$ LoG
- Mais **barato** (dois borrões separáveis + subtração) e reaproveitável numa **pirâmide de escalas**
- É um **passa-banda**: base da detecção de **blobs** / **SIFT** e modelo **centro-entorno** da visão
:::
::img src=dog_log.png height=30%
---
# O domínio da frequência
:::col width=50%
- A **Transformada de Fourier** 2D decompõe a imagem em **ondas** de várias frequências e orientações
- No **espectro de magnitude**:
  - o **centro** = baixas frequências (regiões suaves, brilho médio)
  - a **periferia** = altas frequências (bordas, texturas, ruído)
- Calculada eficientemente com a **FFT**
:::
:::col width=50%
::img src=fourier_demo.png height=42%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Ffourier.zip)
:::
---
# Filtragem no domínio da frequência
:::col width=55%
- **Teorema da convolução**: convolução no espaço = **multiplicação** na frequência
$$
f * h \;\longleftrightarrow\; F \cdot H
$$
- Filtrar = multiplicar o espectro por uma **máscara**:
  - **passa-baixa** → suaviza (mantém o centro)
  - **passa-alta** → realça bordas (mantém a periferia)
- Filtros grandes ficam **mais baratos** via FFT
:::
:::col width=45%
::img src=fourier_filter.png height=42%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Ffourier_filter.zip)
:::
---
# Ruído e filtros não-lineares
:::col width=52%
- Tipos comuns de ruído:
  - **Gaussiano** (sensor, ISO alto) — bem tratado por suavização linear
  - **Sal e pimenta** (pixels extremos) — a média só **espalha** o defeito
- **Filtro de mediana**: substitui o pixel pela **mediana** da vizinhança
  - **não-linear**; remove sal-e-pimenta **preservando bordas**
- **Bilateral**: média ponderada por proximidade **espacial e de cor** → suaviza sem borrar bordas
:::
:::col width=48%
::img src=noise_filters.png height=42%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fnonlinear_filters.zip)
:::
---
# Limiarização (thresholding)
:::col width=55%
- Converte uma imagem em **binária** (objeto × fundo) por um limiar $t$:
$$
g(x,y) = \begin{cases} 1 & f(x,y) \ge t \\ 0 & \text{caso contrário} \end{cases}
$$
- Escolher $t$ automaticamente:
  - **Otsu** — maximiza a variância entre as duas classes do histograma
  - **Adaptativo** — $t$ varia por região (iluminação desigual)
- É a porta de entrada para morfologia e segmentação
:::
:::col width=45%
- Funciona bem quando objeto e fundo têm intensidades bem separadas (histograma **bimodal**)
:::
---
# Operações morfológicas
:::col width=50%
- Atuam na **forma** de regiões em imagens binárias, usando um **elemento estruturante** $B$ (ex.: disco)
- **Erosão** ($A \ominus B$): encolhe; remove saliências e ruído fino
- **Dilatação** ($A \oplus B$): engorda; preenche buracos e conecta partes
- São duais entre si (uma no objeto = a outra no fundo)
:::
:::col width=50%
- **Abertura** $A \circ B = (A \ominus B) \oplus B$
  - remove pequenos objetos/ruído **sem** encolher o que sobra
- **Fechamento** $A \bullet B = (A \oplus B) \ominus B$
  - preenche buracos e fendas **sem** engordar o contorno
- **Gradiente morfológico** ($A\oplus B - A\ominus B$): extrai o **contorno**
- Aplicações: limpeza de máscaras, contagem, esqueletização, pré-processamento de OCR
:::
::img src=morphology.png height=40%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fmorphology.zip)
---
# Segmentação
:::col width=52%
- **Particionar** a imagem em regiões significativas (objetos)
- Famílias de métodos:
  - por **limiar** (intensidade/cor)
  - por **bordas** (fechar contornos detectados)
  - por **regiões** (crescimento, _split & merge_)
  - por **agrupamento** (_k-means_ de cor, _mean-shift_)
  - **watershed** (relevo de gradiente)
:::
:::col width=48%
::img src=segmentation.png height=42%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F15+-+Processamento+de+Imagem%2Fsegmentation.zip)
:::
---
# Segmentação: regiões e componentes conexas
:::col width=58%
- **Rotulação de componentes conexas**: após binarizar, agrupa pixels vizinhos do objeto e atribui um **rótulo** a cada região isolada
  - vizinhança-4 ou vizinhança-8
  - permite **contar** e medir objetos (área, centroide, perímetro)
- **Crescimento de regiões**: a partir de _seeds_, agrega vizinhos similares
- Métodos modernos usam **redes neurais** (segmentação semântica/por instância) — fora do escopo desta aula
:::
:::col width=42%
- A figura ao lado: moedas binarizadas por Otsu e rotuladas em componentes conexas (cada cor = um objeto)
:::
---
# Resumo
- **Imagem digital** = sinal 2D **amostrado** (resolução espacial) e **quantizado** (resolução de cor)
- **Amostragem**: respeitar **Nyquist** e pré-filtrar evita **aliasing**; interpolação para reamostrar
- **Cor**: quantização e paletas; **dithering** troca resolução de cor por espacial
- **Intensidade**: histograma, brilho/contraste, **equalização**, **gama**
- **Filtros (convolução)**: suavização, realce, **bordas**; visão dual no **domínio da frequência**
- **Ruído**: mediana/bilateral para casos que a média não resolve
- **Forma**: **morfologia** (erosão/dilatação/abertura/fechamento) e **segmentação**
---
:::center
# Obrigado!
:::
