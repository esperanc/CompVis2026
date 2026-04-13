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
:::col
# Exemplo
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
:::col
::iframe src="https://esperanc.github.io/Py5Script/view.html?zip=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&name=raymarching_simples"
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
:::col
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
:::col
::iframe src="https://esperanc.github.io/Py5Script/view.html?zip=KoUQzgIgQggg9jRSoGEDSBLAYgTwFIBaA1ALbBwDuIiaAsrInkjAMYBMALgDYAmA4gDk4AGQB2UAKwE+ANRIBJABJQcBAOoAPAG4BNNQEU4aACpH5KGAHN5fHmABGbPAAt7KKBwCmMgJwAvAEM+LABrAgANeTRzKxsARglwgGYhPQAlLhYMGB8bbXTjINCI+TgUbOsLStjRAkzRDM8sfyKwyIBXAjYNPzd5MHLYqpjrEgIcPR4AM3ZnZ2kZHGESO3YKDDRDNAWFRQFeRRkKNBQQgDZByqgAKxYSGWd+GQg9CTYdcNo4AWuYCmELGxaBAYGB5FgeFh9CEeLRNkYdjY0hNwiwjKZosM+C4dJxRHcfHF7CRDLRrvJjoZqpZiT5jDxFHgtAE2OR4dTZvNZDg0HwEslUmoMlkQpjYsoQvIIAAGSwsPhcAAs6g0IHUEkC4TSEhOopG8USKTg6UyGA1ETSMmJXBI9iSeA4JzwAAdgPdet04vwuFp7Bh+vJ4NSRgFRAIph88CiQnA1EkeM6CIo0kZxCFhHxnFwAmoeHAeChnRQCFhpc6TGAxdY+YbBcKzX4LVaSDa7Q6nc6ZAqOAQAMoBvnO+x8DTOlg4SzO4R+EAUYEwZ0AeQocA5I9cZHzbC4ML4ljAQRkibYzmlm2d+l7c5AKEszEQIHkAEd5OEBE+KAAFHT2IjMAD0d6IFAgbAWwER4NKETODMJ5cosyyrN0FB3DI1wBG+Q5sIqlhBFwogBIoVgECQ+ThPoADst7Oo8yY4DmeBenwwCWDw9zXLQOBQM4wB8C0WpYYqVGiDI7Q5gQWh3LK9hqKWAjuHExhqD4YSaGoOYyEkSmlncSrLs6RItra9ocPEjwQPorEyCojjOlwOhJGkWESAIHzIhhlhUZObCODuZk5oqRi9lAVEVGxaHyVAbAaVpymqRo+h2gIzrer62S5IcAiOBk9hYAQibhDwrlavR4SWJYmBReotBnsEiUpClCppRQli0L2irHMYlbmFAoi5T49XJalfo5EoMj6AST7qAI0o5j47TadKumKuYq5sVwvDSnEWgLGAvH8U5jhCTEaBTNZwh-PoaD3og+gYHAzgsAEARnOGID6FgwEgFA+gPswfDjJMsFzAsSwrGA7AaCh7EYclR24QqBFEZYJFkZR1GGa2JlKHUOh+PIuEyHgmRsD4YA8AJR3CaJ4mSSQsqo7o5GE4dajAF5zrXI4GoFlAQ6iJZxjAFgHxbVAwAhAI8i9sAEiKOEcQCMAlpQMYUqymSwBxPpXNsDz7i2nxjzuAI+gPFMaQgFwxgyBYuQQLOtAoB1Ovc34vOGz4xtQFgwsCHgxggD4i7q61ztziCGjLkYuLzSwSSWYzHyJy2XDDmkn51PlEQsJYn7BRMQrOq8fhoBZcTCL8S44DAWjCFxagQbNagCK47jXHocSZCQICWK8fXMWgsftPHlnhRxXFcJ4bN58F4FqLQpcgu0TstU7HUAjAbCVwui413XXGDY1Pp+lAO0YFAs3MSj4QbdRnve348pZqhxiWzo+bsZxUB+J3FDDuNXy7QCwhEsJ4FcHJ7jSgpngdoeQ04rFmigZwv81BxH-rIRK25gGnEsMIXsMANA72EmeFAYwHBsFLEoH46ouDAGlGkPgaBFC4z8LQOUlCODyg0HQvi-N9DOiUN1YYjIDiLFPk-TM3cZBvxAB-dgWAuEjl4T4fhS4KDOh8NReei8bASDpnENuzgdH4yIoIxQwjYgAwoVQvgll84-1xKJAgMgBAgDSBgZwnVLHWBYfZfGKMCEZVYaUdeYJl7AhAOo1cIxULQPCLAvRBjXAKjOH2Yx1VS52KnFSfUwx8lDEKb41hXx2D7GJDI9+cAWAoC7mIJUnhTgDAqHkoprTgz5McWwZxrj3GeP+GzdonhFBKjQFeKs7TJkFODHsa4tD6GMOYTAHsvYJCKmGSEcsvYQgkJOOQxwVDGTOE8FrR6JAhDmAyQvfGfAnIijARAmwBAbHSiRJkZMcBQ7r1CsREgPgcCXP4bhIJUoYAURsKAz8JszYwSFlgXs+hpTOADjCKYWs0i+ywLQcFfAQgACc0A4FAeAmJVQk7M2kFwd2dtqFzLUBIOhDCmGyCkAQvFbyWAfNWijBUPIuoTIVAoZBIRYavIgC1FWxgZYaE-MYDAoC4kwLgbc95KZo7UgWBQfg5U0B+AZgqd2EAfE2BtJctol8AgWCIA4025tLbW1tgqqBSr5AgDiFAWSPgQC9lccAdVSgzw9VUFqOIdwcJwtFmkPAWt0aiFIbUfx7C7hYAkIwrgqgW7N3mswkJKNRAuAINKAQvp7SimCj81iX8L7rJBQDQuPAICOH+QQCwpkFS9giMW+whws3tDEM4CQ5gAAcrUMAu0edYg5rzFCrgca6d0jgNBMRPmaQdKAR38CwO0Xk2dNAhGMPPGKw7R0dQrJiFQFpQ0kBwrSHAMksAHnCHZHNia4AbLBLUs4YydkoDjScWozIDA0lkkODAOqBEVvHt-EVkRZ4qA+FwEAGFiYOUOthOAXQNAW3zfMItJa8DplEAOs9PUH68xgzNUOyaJDaQmGwSwGHeUkYNsOL2vM4AYXscFd2shji3LHAnMEbqPXNG9b68wspJXStlfKyDX8uLtDbKZGUNI-l3tkpWFlfYOAUbPCQO5snLiYewwWvDrGAUqfHvJZwHHyJPj0HgLJ+ipJTgsEQqu+kfCgDALAZwv1bw3UfC+SI+E0m9l+L9eAVAkAhBunF+LMA9h4otOhFAEgKDeCgBdfQ8hgCIAQPeVAmAsCBEgGwPggEkCfkVMwAhCW4tfAYFVBJUFwgwU5KDRCENuiXioCgT6MBro3Tug9J6L03ofS+j9P69WboQBq0BAgOGCBxBaMENo8hOjdF6FgLLP0dA3QoDAEEwg8vASfBYe8ABeIAA&name=raymarching_normal"
---
# Veja também
- [Ray Marching and making 3D Worlds with math](https://youtu.be/BNZtUB7yhX4)
- [Ray Marching for dummies](https://youtu.be/PGtv-dBi2wE)