# Recorta las 3 poses de arte/02-moco-gelatina.png, saca el fondo crema
# y las alinea por los pies en img/moco-normal.png, moco-panzon.png, moco-flaquito.png
import sys
from collections import deque
from pathlib import Path
from PIL import Image, ImageFilter

raiz = Path(__file__).resolve().parent
src = Image.open(raiz / 'arte' / '02-moco-gelatina.png').convert('RGB')
w, h = src.size
px = src.load()

def es_verde(p):
    r, g, b = p
    return g - r > 18

# Fondo = todo lo no verde que se alcanza desde el borde (ojos y boca quedan adentro)
fondo = bytearray(w * h)
cola = deque()
for x in range(w):
    cola.extend([(x, 0), (x, h - 1)])
for y in range(h):
    cola.extend([(0, y), (w - 1, y)])
while cola:
    x, y = cola.popleft()
    i = y * w + x
    if fondo[i] or es_verde(px[x, y]):
        continue
    fondo[i] = 1
    if x > 0: cola.append((x - 1, y))
    if x < w - 1: cola.append((x + 1, y))
    if y > 0: cola.append((x, y - 1))
    if y < h - 1: cola.append((x, y + 1))

mascara = Image.frombytes('L', (w, h), bytes(0 if f else 255 for f in fondo))
mascara = mascara.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
rgba = src.copy()
rgba.putalpha(mascara)

# Cada pose ocupa un tercio; el orden de la hoja es normal, panzón, flaquito
nombres = ['normal', 'panzon', 'flaquito']
cortes = [(0, 545), (545, 1110), (1110, w)]
recortes = []
for (x0, x1) in cortes:
    parte = rgba.crop((x0, 0, x1, h))
    recortes.append(parte.crop(parte.getchannel('A').point(lambda a: 255 if a > 20 else 0).getbbox()))

ancho = max(r.width for r in recortes) + 20
alto = max(r.height for r in recortes) + 20
escala = 460 / alto
salida = raiz / 'img'
salida.mkdir(exist_ok=True)
for nombre, r in zip(nombres, recortes):
    lienzo = Image.new('RGBA', (ancho, alto), (0, 0, 0, 0))
    lienzo.paste(r, ((ancho - r.width) // 2, alto - 10 - r.height), r)
    lienzo = lienzo.resize((round(ancho * escala), round(alto * escala)), Image.LANCZOS)
    lienzo.save(salida / f'moco-{nombre}.png', optimize=True)
    print(nombre, r.size, '->', lienzo.size)
