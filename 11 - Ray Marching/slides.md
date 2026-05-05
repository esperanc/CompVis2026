:::center
# Computação Visual
## 11 - Ray Marching
:::
---
# Interseções com raios
- Tipicamente, temos que encontrar raízes de funções em $t$
- Para funções moderadamente complexas, não há soluções algébricas
- Nesses casos, são empregados métodos _numéricos_
- O método mais simples é o _step tracing_ 
  - Pontos são amostrados ao longo do raio até encontrar uma interseção ou a amostra sair da cena
  - Ineficiente para objetos distantes ou muito pequenos
---
# SDFs (Signed Distance Functions)
- Se a cena é modelada por funções de distância, para qualquer ponto sabemos exatamente quão distantes estamos do objeto
  - Podemos fazer _step tracing_ com passos variáveis!
- Avaliamos a SDF no ponto inicial $P_0$ do raio
- Se $d = SDF(P_0) > 0$, avançamos $d$ unidades ao longo do raio
  - $P_1 = P_0 + d \vec v$
  - Em geral, $P_{i+1} = P_i + SDF(P_i) \vec v$
- Repetimos sucessivamente até
   1. atingir um objeto, ($d \leq \epsilon$), ou
   2. exceder o limite de iterações, ou
   3. ponto ficar distante demais
---
:::center
::img src=ray_marching.svg width=90%
:::
---
# Câmera
::img src=ray_camera.svg width=90%
---
# Geração de raios
- O plano de projeção é perpendicular a `eye-center`, está a uma distância focal `flen` de `eye` e o eixo `y_E` tem a direção de `up` projetado sobre o plano
```glsl
vec3 rayDirection(vec2 fragCoord) {
    
  vec2 uv = fragCoord.xy / iResolution.xy - 0.5 ; // Normalized coordinates
  uv.x *= iResolution.x / iResolution.y; // Aspect ratio

  vec3 z_E = normalize(eye-center); // Vector center-eye
  vec3 x_E = normalize(cross(up,z_E));  // Vector to right of proj plane
  vec3 y_E = normalize(cross(z_E,x_E));  // Vector to top of proj plane
  vec3 C = eye - flen*z_E; // Center of projection plane
  vec3 P = C + x_E*uv.x + y_E*uv.y; // Point on proj plane
  return normalize (P - eye);
}
```
---
:::col ratio=70%
# Ray marching básico
```glsl
float rayMarch (vec3 dir) {
  float depth = 0.;
  for (int i = 0; i < MAX_MARCHING_STEPS; i++) {
    float dist = sceneSDF(eye + depth * dir);
    if (dist < EPSILON) return depth;
    depth += dist;
    if (depth >= MAX_DIST) return MAX_DIST;
  }
  return MAX_DIST;
}
```
:::
:::col ratio=30%
::img src=raymarching_simples.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_simples.zip)
:::
---
# Movendo a câmera
:::col ratio=70%
- Podemos usar o mouse para mover a câmera
- Assumindo que `iMouse` contém a posição do mouse em coordenadas de tela
```glsl
mat2 rot2d (float angle) {
    float c = cos(angle), s=sin(angle);
    return mat2(c, -s, s, c);
}
vec3 getEye () {
    vec2 m = iMouse.xy/iResolution.xy*2.-1.; // range [-1,1]
    vec3 eye = defEye;
    eye.yz *= rot2d(-m.y*3.1416/2.);
    eye.xz *= rot2d(m.x*3.1416);
    return eye;
}
```
:::
:::col ratio=30%
::img src=raymarching_mouse.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_mouse.zip)
:::
:::
---
# Normais
- Precisamos de normais para o modelo de iluminação
- Como vimos, a normal de uma função implícita $f(x,y,z)$ é dada por
$$
\nabla(f) = \left[ \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right]^\top
$$
- Não podemos fazer diferenciação exata, mas podemos aproximar o gradiente por diferenças finitas:
$$
\nabla(f) \approx 
\begin{bmatrix} 
f(x,y,z)-f(x-\epsilon,y,z)\\
f(x,y,z)-f(x,y-\epsilon,z)\\
f(x,y,z)-f(x,y,z-\epsilon)
\end{bmatrix},
$$
onde $\epsilon$ é um valor pequeno.
---
:::col ratio=70%
# Exemplo
```glsl
vec3 normal(vec3 p) {
    float d = sceneSDF(p);
    vec2 e = vec2(0., 0.01);
    return normalize(vec3(d)-
                    vec3(sceneSDF(p-e.yxx),
                         sceneSDF(p-e.xyx),
                         sceneSDF(p-e.xxy)));
}
...
void main () {
  vec3 dir = rayDirection(gl_FragCoord.xy);
  float dist = rayMarch(dir);
  float hit = step(dist, MAX_DIST - EPSILON);
  vec3 norm = normal(eye+dist*dir);
  gl_FragColor = vec4(hit*abs(norm), 1.0);
}
```
::: 
:::col ratio=30%
::img src="raymarching_normal.png" height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_normal.zip)
:::
--- 
:::col ratio=70%
# Iluminação
```glsl
const vec3 lightPos = vec3(10);  // Light position
const vec3 lightColor = vec3 (1); // Light color
const vec3 matColor = vec3 (1,0,0); // material Color
const float matDiff = 0.8; // Diffuse coefficient
const float matAmb = 0.3; // Ambient coefficient
const float matSpec = 0.8; // Specular coefficient
const float matShine = 20.0; // Shininess power

vec3 lighting (vec3 p) {
    vec3 n = normal(p);
    vec3 l = normalize(lightPos - p);
    vec3 e = normalize(eye - p);
    vec3 ia = matAmb * lightColor * matColor;
    vec3 id = matDiff * max(0.,dot(l, n)) * lightColor * matColor;
    vec3 r = reflect(-l,n);
    vec3 is = matSpec * pow(max(0., dot(e,r)),matShine) * lightColor;
    return ia+id+is;
}
```
:::
::: col ratio=30%
:: img src=raymarching_light.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_light.zip)
:::
---
:::col ratio=70%
# Operações de conjunto (booleanas)
- SDFs também podem ser combinadas usando operações de conjunto (booleanas)
| Op booleana | SDF equivalente |
| --- | --- |
| $A \cup B$ | $\min(A,B)$ |
| $A \cap B$ | $\max(A,B)$ |
| $A \setminus B$ | $\max(A,-B)$ |
| $B \setminus A$ | $\max(-A,B)$ |
:::
::: col ratio=30%
:: img src=raymarching_boolean.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_boolean.zip)
:::
---
# Suavização / expansão
:::col ratio=70%
- Uma SDF pode ser suavizada simplesmente subtraindo um valor $r$ de seus valores
```glsl
float smooth(float sdf, float r) { return sdf - r; }
```
:::
:::col ratio=30%
:: img src=raymarching_smooth.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_smooth.zip)
:::
---
# Operações booleanas suavizadas
:::col ratio=70%
- É possível obter versões suavizadas das operações booleanas usando uma função min/max _suavizada_
- Há diversas possibilidades, exploradas [neste artigo](https://iquilezles.org/articles/smin/) de Inigo Quilez
- Uma implementação bastante usada é a versão quadrática
```glsl
float smin( float a, float b, float k )
{
    k *= 4.0;
    float h = max( k-abs(a-b), 0.0 )/k;
    return min(a,b) - h*h*k*(1.0/4.0);
}
```
:::
:::col ratio=30%
:: img src=raymarching_smooth_min.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_smooth_min.zip)
:::
---
# Transformações
- Aplicar uma transformação a uma SDF envolve aplicar a inversa da transformação ao ponto antes de avaliá-la.
- Para rotações, a rotação inversa de $\theta$ usa-se o mesmo eixo mas um ângulo $-\theta$.
- Para transladar $v$ a distãncia $||v||$ é preservada. A translação inversa é a translação pelo vetor $-v$.
- Para uma escala **uniforme** por $s$, precisamos tomar cuidado, pois as relações de distância são alteradas. 
 - Aplicamos $s$ à distância avaliada, para efetivar a escala
```glsl
float opScale( in vec3 p, in float s )
{
    return primitive(p/s)*s;
}
```
---
# Espelhamento
:::col ratio=60%
- Podemos obter uma cópia espelhada de um objeto simplesmente espelhando o ponto de amostra com relação a um plano

```glsl
vec3 opSymX (vec3 p) {
    p.x = abs(p.x);
    return p;
}

vec3 opSymY (vec3 p) {
    p.y = abs(p.y);
    return p;
}
```
:::
:::col ratio=40%
::img src=raymarching_mirror.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_mirror.zip)
:::
---
# Repetição
:::col ratio=60%
- Cópias podem ser obtidas subdividindo o espaço para obter os sistemas de coordenadas locais de cada cópia
- Por exemplo, para obter repetições numa grade de células de tamanho `s`: 
```glsl
vec3 opRepeat (vec3 p, float s) {
    return p - s*round(p/s);
}
```
- É possível também limitar o número de repetições. Para ter entre $2n+1$ repetições ao redor da origem, fazemos: 
```glsl
vec3 opLimRepeat (vec3 p, float s, vec3 n) {
    return p - s*clamp(round(p/s),-n,n);
}
```
- Importante: assume que os objetos repetidos são simétricos com relação aos planos coordenados.
  - Ver [este artigo](https://iquilezles.org/articles/sdfrepetition/) para uma discussão mais aprofundada.
:::
:::col ratio=40%
::img src=raymarching_repeat.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_repeat.zip)
:::
---
# Usando materiais
:::col ratio=60%
- Para poder distinguir entre os objetos da cena, criamos uma função semelhante à da SDF, mas que retorna o material ao invés da distância
```glsl
vec3 sceneMat (vec3 p) {
    float ball = sphereSDF(p-vec3(-1.,0,0),0.8);
    float block = blockSDF(p-vec3(1.,0,0), vec3(0.8));
    float d = min(ball,block);
    if (d == ball) return vec3(1,1,0);
    return vec3(0,1,1);
}
```
:::
:::col ratio=40%
::img src=raymarching_material.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_material.zip)
:::
---
# Cubemaps
:::col
- Textura que envolve toda a cena.
  - Também chamada de _skymap_ ou _skybox_
- WebGL tem suporte a cubemaps, mas P5.js não
  - É necessário acessar funções WebGL diretamente para criar cubemaps
- Precisamos de 6 imagens, uma para cada face de um cubo centrado na origem mas de tamanho em tese infinitamente grande
  - Imagens quadradas de mesmo tamanho e resolução  
:::
:::col
```python
urls = [
  'posx.jpg', 'negx.jpg', 
  'posy.jpg', 'negy.jpg', 
  'posz.jpg', 'negz.jpg'
  ]
images = [loadImage(url) 
  for url in urls]
```
:::
---
# Carregando a textura do cubemap
```python
def createCubemap():
  """ Create cubemap from images """
  gl = drawingContext; 
  tex = gl.createTexture();
  gl.bindTexture(gl.TEXTURE_CUBE_MAP, tex)
  targets = [
    gl.TEXTURE_CUBE_MAP_POSITIVE_X, gl.TEXTURE_CUBE_MAP_NEGATIVE_X,
    gl.TEXTURE_CUBE_MAP_POSITIVE_Y, gl.TEXTURE_CUBE_MAP_NEGATIVE_Y,
    gl.TEXTURE_CUBE_MAP_POSITIVE_Z, gl.TEXTURE_CUBE_MAP_NEGATIVE_Z
  ]
  for img,target in zip(cubemapImages,targets):
      # the actual image element is in img.canvas
      gl.texImage2D(target, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, 
          img.canvas)
  gl.texParameteri(gl.TEXTURE_CUBE_MAP, gl.TEXTURE_MIN_FILTER, gl.LINEAR)
  return tex
```
---
# Passando a textura para o shader
```python
def draw(): 
  ...
  # Vincula a textura manualmente ao slot 0
  gl = drawingContext
  gl.activeTexture(gl.TEXTURE0)
  gl.bindTexture(gl.TEXTURE_CUBE_MAP, cubemap)
  
  # p5 não entende cubemaps. Uniforme tem que ser
  # setado manualmente
  uCubemapLoc = gl.getUniformLocation(my_shader._glProgram, 'uCubemap')
  gl.uniform1i(uCubemapLoc, 0)
```
---
# Acessando a textura no shader
:::col ratio=60%
- Ao invés de coordenadas u,v, usa-se um vetor em 3D!
```glsl
uniform samplerCube uCubemap; 
...
void main() {
  vec3 dir = rayDirection(eye, 
    gl_FragCoord.xy);
  // cubemap color needs to flip x 
  // for left-handed coord system
  vec3 color = textureCube(uCubemap, 
     dir*vec3(-1,1,1)).rgb; 
  ...
}
```
:::
:::col ratio=40%
::img src=raymarching_cubemap.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_cubemap.zip)
:::
---
# Reflexão com cubemap
:::col ratio=60%
- Podemos acrescentar reflexão à cena, calculando o raio refletido no ponto de interseção
```glsl
  vec3 R = reflect(-e,n);
  vec3 T = textureCube(uCubemap, 
    R*vec3(-1,1,1)).rgb; // Flip x
```
- A cor do modelo de iluminação pode ser combinada com a cor da textura:
  - Modulação: `C*T`
  - Mistura: `C*0.5 + T*0.5`
:::
:::col ratio=40%
::img src=raymarching_cubemap_reflect.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_cubemap_reflect.zip)
:::
---
# Reflexão "recursiva" (1)
:::col ratio=35%
- Raios refletido podem atingir outros objetos
- A cor final depende do que o raio refletido "vê"
- É possível simular múltiplas reflexões
  - Embora não seja "recursivo", em termos de código, podemos repetir os cálculos
- Refatoramos o código para que a função `lighting` retorne também a nova origem e direção do raio refletido
:::
:::col ratio=65%
```glsl
vec3 lighting (vec3 eye, inout vec3 p, 
               out vec3 R) {
    vec3 n = normal(p);
    vec3 l = normalize(lightPos - p);
    vec3 e = normalize(eye - p);
    vec3 matColor = sceneMat(p);
    vec3 ia = matAmb * lightColor * matColor;
    vec3 id = matDiff * max(0.,dot(l, n)) * 
      lightColor * matColor;
    vec3 r = reflect(-l,n);
    vec3 is = matSpec * pow(max(0., dot(e,r)),matShine) * lightColor;
    R = reflect(-e,n); // Bounce direction
    p += n*5.*EPSILON;  // Bounce point
    return (ia+id+is);
}
```
:::
---
# Reflexão "recursiva" (2)
:::col ratio=40%
- Encapsulamos o código para obter a cor a partir de um raio em uma função separada `render()`
  - Além de retornar a cor, retorna também
   - O raio refletido (nova posição e direção)
   - Uma fração para misturar a cor vista a partir do raio 
   refletido
:::
:::col ratio=60%
```glsl
vec3 render (inout vec3 eye, inout vec3 dir, 
             out float delta) {
  float dist = rayMarch(eye, dir);
  if (dist > MAX_DIST-EPSILON) {
     delta = 0.;
     return textureCube(uCubemap, dir*vec3(-1,1,1)).rgb; 
  }
  vec3 p = eye+dist*dir;
  vec3 R;
  vec3 color = lighting(eye, p, dir);
  eye = p; 
  delta = 0.8;
  return color;
}
```
:::
---
# Reflexão "recursiva" (3)
:::col ratio=60%
- `render()` é chamada múltiplas vezes para simular reflexões múltiplas
```glsl
void main( ) {
  vec3 eye = getEye();
  vec3 dir = rayDirection(eye, gl_FragCoord.xy);
  float delta;
  float alpha = 1.;
  vec3 color = render(eye,dir, delta);
  // bounces
  for (int i = 0; i < 5; i++) {
    alpha *=delta;
    color = mix(color,
        render(eye,dir,delta),alpha);
  }
  gl_FragColor = vec4(color, 1.);
}
```
:::
:::col ratio=40%
::img src=raymarching_cubemap_r_reflect.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_cubemap_r_reflect.zip)
:::
---
# Refração (1)
- A ideia é similar, mas agora o raio pode penetrar no objeto e precisamos levar levar em conta múltiplos "bounces" 
::img src=refracao.svg height=70%
---
# Refração (2)
:::col ratio=60%
- A função `refract(in, out, refr)` faz um papel semelhante ao `reflect()`
- Usa-se `refr` maior que 1 para um raio que sai do objeto, e menor que 1 para um raio que entra
- `refract()` pode retornar um vetor nulo caso ocorra reflexão total interna
- Um raio que caminha dentro do objeto deve considerar
  - A normal com sentido invertido
  - A SDF com sinal trocado: dentro é positivo e fora é negativo
:::
:::col ratio=40%
::img src=raymarching_cubemap_r_refract.png height=70%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_cubemap_arcball_r_refract.zip)
:::
---
# Interação com arcball

- Infelizmente não podemos mais usar o orbitControl() do p5! 
- Precisamos implementar a rotação da câmera e o zoom manualmente
  - a constante `eye` pode ser passada como um `uniform`
- Um manipulador intuitivo para rotação pode ser implementado usando o conceito do **arcball**
  - Imagina-se que existe uma grande esfera no centro da tela que pode ser girada por clique e arraste
  - A rotação é calculada projetando-se os pontos de início e fim do arrasto na superfície da esfera
  - O eixo de rotação é o produto vetorial dos vetores que vão do centro da esfera aos pontos de início e fim
  - O ângulo de rotação é o ângulo entre os vetores que vão do centro da esfera aos pontos de início e fim
---
# Arcball
::img src=arcball.svg height=90%
---
# Cálculo da rotação
```python
def get_rotation (a, b):
    """ Returns the rotation axis and angle that rotates a into b  """
    a = a.copy().normalize()
    b = b.copy().normalize()
    axis = a.cross(b)
    if axis.mag() < 1e-6:
        return createVector(0, 1, 0), 0.0   # no rotation
    return axis.normalize(), abs(a.angleBetween(b))
```
---
# Coordenadas de olho $\times$ coordenadas de tela

- A rotação é calculada em coordenadas de _tela_ mas tem que ser aplicada em coordenadas de mundo
  - $x_E, y_E, z_E$ expressos em coordenadas de mundo
  - Precisamos montar esse sistema de forma semelhante ao feito no shader
```python
def get_camera_axes(eye_dir):
    """Returns the right and up vectors of the camera 
    in world space."""
    world_up = createVector(0, 1, 0)

    right = world_up.copy().cross(eye_dir).normalize()  
    up    = eye_dir.copy().cross(right).normalize()   
    
    return right, up
```
---
# Rotação de um vetor em torno de um eixo
- Lembram?
```python
def rot_around_axis (v, u, ang):
    """ Returns v rotated by ang around axis u """
    # Rodrigues formula
    # Term 1: v * cos(ang)
    term1 = p5.Vector.mult(v, cos(ang))
    
    # Term 2: (u x v) * sin(ang)
    crossProd = p5.Vector.cross(u, v)
    term2 = p5.Vector.mult(crossProd, sin(ang))
    
    # Term 3: u * (u . v) * (1 - cos(ang))
    dotProd = p5.Vector.dot(u, v)
    term3 = p5.Vector.mult(u, dotProd * (1 - cos(ang)))
    
    # Combine all terms
    return term1.add(term2).add(term3)
```
---
# Obtendo o ponto do arcball
```python
def arcball_point():
    """ Arcball point from mouse point """
    p = createVector(mouseX, height-mouseY)
    p.z = max(0, r-p.dist(c))
    return p
    
def mousePressed():
    """ Save start point for drag """
    global saved
    saved = eye_dir, arcball_point()
```
--- 
# Realizando o arraste
```python
def mouseDragged():
    prev_dir, a = saved 
    b = arcball_point()
    
    # Subtract center point
    a_rel = a.copy().sub(c)
    b_rel = b.copy().sub(c)
    
    # Rotation axis in screen space
    u_screen, ang = get_rotation(a_rel, b_rel)
    
    # Rotation axis in world space
    x_world, y_world = get_camera_axes(prev_dir)
    u_world = p5.Vector.mult(x_world,  u_screen.x)
    u_world.add(p5.Vector.mult(y_world,  u_screen.y))
    u_world.add(p5.Vector.mult(prev_dir, u_screen.z))
    u_world.normalize()
    
    # Rotate camera in the opposite direction of the object rotation
    global eye_dir
    eye_dir = rot_around_axis(prev_dir, u_world, -ang) 
```
---
::img src=raymarching_cubemap_arcball_r_reflect.png height=80%
[link](https://esperanc.github.io/Py5Script/ide.html?sketch=https%3A%2F%2Fesperanc.github.io%2FCompVis2026%2F11+-+Ray+Marching%2Fraymarching_cubemap_arcball_r_reflect.zip)
---
# Veja também
- [Ray Marching and making 3D Worlds with math](https://youtu.be/BNZtUB7yhX4)
- [Ray Marching for dummies](https://youtu.be/PGtv-dBi2wE)
- [Canal Art of Code](https://www.youtube.com/@TheArtofCodeIsCool)
---
:::center
# Obrigado
:::