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
# Veja também
- [Ray Marching and making 3D Worlds with math](https://youtu.be/BNZtUB7yhX4)
- [Ray Marching for dummies](https://youtu.be/PGtv-dBi2wE)