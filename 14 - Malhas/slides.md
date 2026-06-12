:::center
# Computação Visual
## 14 - Malhas
:::
---
# Modelos geométricos
:::col width=60%
- São **estruturas de dados que representam formas geométricas**
- Principais paradigmas:
  - **Fronteira explícita** — modela a curva (2D) ou superfície (3D) que delimita o objeto
    - Polígonos, malhas poligonais
    - Modelos curvos por equações paramétricas
  - **Funções implícitas** — $f(x,y,z) \le 0$ indica o interior
    - SDFs (_signed distance functions_), CSG
  - **Divisão do espaço** — grades, octrees, BSPs
:::
:::col width=40%
- Nesta aula: **malhas poligonais**, a representação de fronteira dominante na computação gráfica
- São a saída natural de modeladores, scanners e do _hardware_ gráfico
:::
---
# B-Rep
:::col width=55%
- Abreviação de _Boundary Representation_
- O objeto é descrito pela(s) **superfície(s) que o delimita(m)**
- Superfícies podem ser **retalhos "costurados"**
  - A interconexão dos retalhos é uma **estrutura combinatória**
  - O resultado precisa ser "fechado" → conceito de **2-variedade** (topologia)
- Cada retalho é descrito por superfícies mais simples:
  - Polígonos planos
  - Superfícies paramétricas ($\mathbb{R}^2 \to \mathbb{R}^3$): Bézier, B-splines, NURBS
:::
:::col width=45%
::img src=brep_car.png height=75%
:::
---
# Fórmula de Euler-Poincaré
:::col width=55%
- Característica topológica de superfícies **fechadas** (2-variedades)
- Precisa ser válida para uma malha poligonal ser "fechada":
$$
\large V - E + F = 2 - 2G
$$
- Onde:
  - $V$ = número de **vértices**
  - $E$ = número de **arestas** (_edges_)
  - $F$ = número de **faces**
  - $G$ = _genus_ (número de **buracos**)
:::
:::col width=45%
::img src=genus.png height=45%
- Esfera: $G=0$ → $V-E+F=2$
- Toro: $G=1$ → $V-E+F=0$
:::
---
# Malhas
:::col width=55%
- Estrutura semelhante a um **grafo**, mas com geometria associada:
  - **Vértices** → vértices do grafo, com um ponto $(x,y,z)$ associado
  - **Arestas** → arestas do grafo
  - **Faces** → ciclos do grafo
- Faces com mais de 3 vértices precisam ser **trianguladas** para a maioria dos usos
  - Faces planares convexas admitem triangulações triviais (em leque)
:::
:::col width=45%
::img src=sphere_brep_vs_mesh.png height=70%
:::
---
# Malhas triangulares
:::col width=55%
- Todas as faces são **triângulos**
- Sempre planares e convexas → renderização e processamento simples
- Modeladas manualmente ou por **processos automatizados**:
  - **3D-scan**
  - **Fotogrametria**
  - Conversão a partir de modelos implícitos (**Marching Cubes** / Surface Nets)
:::
:::col width=45%
::img src=dolphin_mesh.png height=75%
:::
---
# Marching Cubes
:::col width=50%
- Converte uma **função implícita** em malha triangular
- A função é amostrada regularmente em $x,y,z$
- Cada célula (cubo) que **intersecta a superfície** (pelo menos um vértice dentro e outro fora) é convertida em triângulos
- O padrão dos $8$ sinais nos cantos seleciona a triangulação, reduzido por simetria a **15 casos**
:::
:::col width=50%
::img src=marching_cubes.png height=75%
:::
---
# Marching Tetrahedra
:::col width=50%
- Variante onde cada cubo é subdividido em 6 tetraedros
- Cada tetraedro é poligonizado de forma exata e **sem ambiguidade**
- O padrão dos 4 sinais nos cantos seleciona a triangulação, reduzido por simetria a **5 casos**
- É possível usar outros arranjos de tetraedros com melhor razão de aspecto
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F14+-+Malhas%2Ftetrahedral_tiling.zip)
:::
:::col width=50%
::img src=marching_tetrahedra.png height=75%
[demo](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F14+-+Malhas%2Fmarching_cubes.zip)
:::
---
# Malhas quadrangulares
:::col width=50%
- Malha de **superfície** (B-Rep): cada face é um **quadrilátero** (triangulação trivial, se preciso)
- Muito usadas em **modelagem artística**
- **Parametrização natural** da superfície (grade $u\times v$ local)
- As arestas tendem a se alinhar com as feições e a curvatura do modelo
- Base natural da **subdivisão de Catmull-Clark**
:::
:::col width=50%
::img src=quad_mesh.png height=70%
:::
---
# Malhas hexaédricas
:::col width=55%
- Atenção: não confundir com as quadrangulares!
- É uma malha **volumétrica** — o **interior** do objeto é decomposto em **hexaedros** (células de 6 faces, tipo "cubo")
- A **superfície que a delimita** é justamente uma **malha quadrangular**
- Usadas em **simulação numérica** (FEM, CFD), onde importa o **volume**, não só a fronteira
  - Hexaedros dão elementos mais regulares e precisos que tetraedros
- Gerar boas malhas hexaédricas é um problema difícil (e ainda em aberto)
:::
:::col width=45%
::img src=hex_mesh.png height=70%
[link](https://www.hexalab.net/)
:::
---
# Varredura (sweep)
:::col width=50%
- Técnica para obter formas 3D a partir de formas 2D
- Uma curva (perfil) é **"varrida" ao longo de outra curva** (trajetória)
- Casos comuns:
  - **Extrusão linear**: perfil ao longo de uma reta
  - **Extrusão circular** (revolução): perfil em torno de um eixo
  - **_Lofting_**: varredura com **interpolação** entre perfis diferentes
:::
:::col width=50%
::img src=sweeping.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F14+-+Malhas%2Fsweep_modeling.zip)
:::
---
# Tabelas de vértices e faces
:::col width=55%
- Estrutura **mais simples** para representar uma malha poligonal:
  1. Uma tabela com as **posições** dos $n$ vértices
  2. Uma tabela com **tuplas de índices** de vértices (uma por face)
- **Convenção**: faces com orientação **positiva** (anti-horária) quando vistas de fora → a normal aponta para fora
- Compacta, mas consultas de adjacência (vizinhança) custam $O(n)$
:::
:::col width=45%
::img src=vertex_face_table.png height=70%
:::
---
# Estruturas combinatórias
:::col width=55%
- Permitem responder com facilidade a **consultas sobre a topologia** da malha, ex.:
  - Dada uma **aresta**, quais faces a compartilham?
  - Dado um **vértice**, quais arestas/faces lhe são incidentes?
  - Dada uma **face**, quais outras lhe são vizinhas por aresta?
- As tabelas de vértices/faces não respondem a isso em tempo constante
- Exemplo:
  - **Half-edge** (ou DCEL: _doubly connected edge list_)
:::
:::col width=45%
::img src=half_edge_diagram.png height=70%
:::
---
# A estrutura half-edge (DCEL)
:::col width=55%
- Cada aresta é representada por **duas _half-edges_ gêmeas** (`twin`), percorridas em sentidos opostos
- Cada half-edge `e` armazena referências para:
  - `origin` — vértice de partida (e `dest = twin.origin`)
  - `twin` — a gêmea (atravessa a aresta)
  - `next` / `prev` — vizinhas no **anel da face**
  - `face` — a face à sua **esquerda**
- **Circuladores** (tempo proporcional ao grau, não a $n$):
  - Anel da **face**: repetir `next`
  - Leque do **vértice**: repetir `twin.next`
- Bordo: half-edges com `face = None`
:::
:::col width=45%
::img src=halfedge.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F14+-+Malhas%2Fhalf_edge.zip)
:::
---
# Operadores de Euler
- Conjunto **mínimo e completo** de operações que constroem e editam malhas (B-Reps) garantindo que permaneçam **topologicamente válidas**
- Operadores que preservam a fórmula de Euler-Poincaré (estendida)
  $ V - E + F - L = 2\,(S - G)$
  (_shells_ $S$, _loops_ $L$, _genus_ $G$):
- Vêm em **pares inversos** — _Make X_ / _Kill X_
- Operam sobre a estrutura **half-edge** e são a base dos núcleos de modelagem de sólidos (CAD)
- Operações de alto nível (extrudar, chanfrar, …) são **compostas** de operadores de Euler
---
# Operadores de Euler (Exemplos)
::img src=euler_ops.png height=75%
---
# Limite do produto tensorial
- Na aula anterior, construímos superfícies de subdivisão por **produto tensorial** — mas isso só funciona sobre grades **retangulares** com vértices de valência $4$
- Modelos reais têm **topologia arbitrária**: vértices com $3$, $5$ ou mais arestas, faces triangulares ou $n$-laterais, buracos…
- Precisamos de esquemas que operem sobre **malhas poligonais arbitrárias** — agora que temos a estrutura **half-edge**, isso é natural
- Os esquemas clássicos **generalizam** exatamente as superfícies de produto tensorial:
  - **Catmull-Clark** → generaliza a B-spline **bicúbica**
  - **Doo-Sabin** → generaliza a B-spline **biquadrática**
  - **Loop** → para malhas **triangulares**
---
# Subdivisão de malhas
:::col width=55%
- A ideia, como nas curvas, tem **dois passos** por iteração:
  1. **Refinar** a topologia (mais faces, novos vértices)
  2. **Reposicionar** os vértices por **médias locais**
- Esquemas **aproximantes** (CC, DS, Loop) suavizam — a malha limite não passa pelos vértices originais
  - Existem também esquemas **interpoladores** (ex.: _butterfly_)
:::
:::col width=45%
::img src=mesh_subdivision.png height=80%
:::
---
# Subdivisão de Catmull-Clark
:::col 
- Funciona em malhas de **quadriláteros** (e converte $n$-gonos em quadriláteros já no primeiro passo). 
- A subdivisão produz 2 pontos novos:
  - **Ponto de face** $\mathbf{f}$: centroide (média dos vértices da face)
  - **Ponto de aresta** $\mathbf{e}$: média dos 2 extremos da aresta e dos 2 pontos de face adjacentes
:::
::: col
:: img src=catmull_newpoints.png height=80%
:::
---
# Subdivisão de Catmull-Clark (II)
::: col width=55%
- Posteriormente, cada vértice é reposicionado como:
$\mathbf{v'} = \frac{\mathbf{F} + 2\mathbf{R} + (n-3)\,\mathbf{v}}{n}$
  onde
  - $n$ é a valência do vértice
  - $\mathbf{F}$ é a média dos pontos de face vizinhos
  - $\mathbf{R}$ é a média dos pontos médios das arestas vizinhas
- Limite **B-spline bicúbica** ($C^2$); em **vértices extraordinários** (valência $\ne 4$) cai para $C^1$
:::
:::col width=45%
::img src=catmull_newvertices.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F14+-+Malhas%2Fmesh_subdivision.zip)
:::
---
# Subdivisão de Doo-Sabin
:::col 
- Esquema opera **cortando** cada vértice e substituindo por uma face
- Como consequência, arestas dão origem a faces quadrangulares
- Os vértices originais são **descartados** e cada par (face, vértice) gera **um novo vértice** no interior da face
- Reconexão gera três tipos de face:
  - **Face-F**: uma por face original (encolhida)
  - **Face-E**: uma por aresta interior
  - **Face-V**: uma por vértice interior
:::
:::col 
::img src=doo-sabin.png height=80%
:::
---
# Subdivisão de Doo-Sabin (II)
:::col 
- Para o vértice $\mathbf{v}$ de uma face de centroide $\mathbf{c}$, a nova posição é a média 
   $\mathbf{v'} = \tfrac14\left(\mathbf{v} + \mathbf{m}_{\text{ant}} + \mathbf{m}_{\text{post}} + \mathbf{c}\right)$
   onde $\mathbf{m}_{\text{ant}}$, $\mathbf{m}_{\text{post}}$ os pontos médios das **duas arestas** da face incidentes em $\mathbf{v}$
- O ponto é "puxado" do canto $\mathbf{v}$ para dentro da face
- Limite **B-spline biquadrática** ($C^1$)
- Produz vértices sempre de valência $4$ (mesmo a partir de $n$-gonos)
:::
:::col 
::img src=doo-sabin.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F14+-+Malhas%2Fmesh_subdivision.zip)
:::
---
# Subdivisão de Loop
:::col width=60%
- Esquema **aproximante** para malhas **triangulares** (Charles Loop, 1987)
  - Malhas não triangulares são trianguladas antes
- Cada triângulo é dividido em **4**, criando um novo vértice por aresta:
  - **Vértice de aresta**: $\tfrac38$ de cada extremo da aresta $+ \tfrac18$ de cada vértice oposto
  - **Vértice antigo**, de valência $n$, é suavizado:
  $\mathbf{v'} = (1 - n\beta)\,\mathbf{v} + \beta \sum_{i} \mathbf{v}_i$
  com $\beta = \tfrac{3}{8n}$ ($\beta=\tfrac{3}{16}$ se $n=3$)
- $C^2$ nos vértices regulares (valência $6$), $C^1$ nos extraordinários
- É o análogo triangular de Catmull-Clark
:::
:::col width=40%
::img src=loop_newpoints.png height=75%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F14+-+Malhas%2Fmesh_subdivision.zip)
:::
---
# Normais
:::col width=55%
- Para iluminação, cada vértice/face precisa de uma **normal**
- **Normais por face** são fáceis: produto vetorial de dois vetores alinhados com arestas do triângulo
- Mas malhas apenas **aproximam** superfícies curvas:
  - Normais por face dão aspecto **"facetado"** (cada face com cor chapada)
- **Solução**: normais **por vértice** (nem sempre numa relação 1-para-1 com as faces)
:::
:::col width=45%
::img src=normals_faceted.png height=55%
:::
---
# "Auto-smooth"
- **Normal por vértice** = "média" (normalizada) das normais das **faces incidentes**
- **Arestas vivas** (cantos) são detectadas estabelecendo um **ângulo máximo** entre as normais de faces adjacentes
  - Acima do limite, a aresta é mantida "dura" (vértices duplicados); abaixo, é suavizada
:::row
::img src=autosmooth_flat.png height=55%
::img src=autosmooth_smooth.png height=55%
::img src=autosmooth_sharp.png height=55%
:::
- Facetado (normal por face) · suave demais (tudo mediado) · **auto-smooth** (cantos preservados)
---
:::center
# Obrigado!
:::
