# El monstruito hambriento

Juego para aprender las tablas de multiplicar. Arriba aparece la cuenta y abajo hay comidas con resultados: tocás la correcta y el monstruito se la come. Si te equivocás la escupe con un "¡puaj!", pero podés probar otra. Nunca se muere ni se pierde nada.

**Jugar:** https://eneassp.github.io/monstruito-hambriento/

## Cómo se juega
- Rondas de 10 cuentas, sin reloj.
- **Sube solo:** empieza con las tablas hasta la del 3 y sube una tabla cuando acertás 8 de 10 a la primera.
- **Elijo yo:** tocás las tablas que querés practicar.
- La pancita de arriba se llena al acertar y baja al fallar. El monstruito se pone panzón si viene bien y flaquito si viene mal.
- La cuenta que fallás vuelve a salir unas preguntas más adelante (o en la ronda siguiente).
- Con las monedas comprás sombreros en la tienda.
- Tocá la cuenta para escucharla en voz alta. Tocá al monstruito y hace cosas (si recién comió, eructa).

Pensado para chicos que están aprendiendo a leer: números grandes, tipografía Lexend, pocas opciones y sin apuro.

## Archivos
- `index.html`: el juego (HTML, CSS y JS en un solo archivo).
- `img/`: las 3 poses del monstruito, ya recortadas y sin fondo.
- `arte/`: las ilustraciones originales de los 4 monstruitos.
- `preparar_imagenes.py`: recorta las poses de `arte/02-moco-gelatina.png` a `img/` (necesita Pillow).
- `build.ps1`: pone la versión en `index.html` y arma el `.zip` completo en `dist/`.
- `VERSION`: versión actual.

## Nueva versión
1. Cambiar `VERSION`.
2. `powershell -ExecutionPolicy Bypass -File build.ps1`
3. Commit, tag `vX.Y.Z`, push y una release en GitHub con el `.zip` de `dist/`.
