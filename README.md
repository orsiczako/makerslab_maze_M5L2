# makerslab_maze_M5L2
### Sziasztok! Csatolom a kódmagyarázatot a Pygame projekt kapcsán, ha valakinek esetleg szüksége lenne a későbbiekben egy kis emlékeztetőre. Jó programozást!:)

#### 1. **Könyvtárak importálása**
A program elején importáljuk a `pygame` könyvtárat:

```python
from pygame import *
```

Ez lehetővé teszi számunkra, hogy hozzáférjünk a Pygame által biztosított funkciókhoz, például a grafika kirajzolásához, a zene lejátszásához és az időzítők használatához.

#### 2. **GameSprite osztály létrehozása**
A `GameSprite` osztály egy sablont ad, amit a játékban használt karakterek (sprite-ok) példányosítására használunk.

```python
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))  # Sprite méretének beállítása
        self.speed = player_speed
        self.rect = self.image.get_rect()  # A sprite négyzetes keretének megadása, ami a pozíciót is jelöli
        self.rect.x = player_x
        self.rect.y = player_y
```

- **`player_image`**: A sprite képfájljának betöltése, amely a karakter vagy tárgy grafikája.
- **`player_x` és `player_y`**: A sprite kezdeti pozíciója a játékablakban.
- **`player_speed`**: A sprite sebessége, ami a mozgásért lesz felelős (játékos esetén).

A **`reset()`** függvény gondoskodik arról, hogy a sprite újra megjelenjen a megfelelő pozícióban:

```python
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  # Kirajzolja a sprite-ot a képernyőre
```

#### 3. **Ablak és grafika inicializálása**
A Pygame ablakot és a játék hátterét is beállítjuk:

```python
init()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
```

Itt létrehozunk egy 700x500 pixeles játékablakot, és a címet **"Maze"**-re állítjuk. A háttérkép is be van töltve és méretezve:

```python
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
```

#### 4. **Zene inicializálása**
A `pygame.mixer`-t használjuk a háttérzene lejátszásához:

```python
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
```

Ez a kód betölti és elindítja a háttérzenét.

#### 5. **Óra és FPS beállítása**
A játékban beállítjuk az FPS-t (képkocka/másodperc), ami azt határozza meg, hogy a játék milyen gyorsan frissül:

```python
clock = time.Clock()
FPS = 60
```

Ez azt jelenti, hogy a játék másodpercenként 60-szor frissül.

#### 6. **Sprite példányok létrehozása**
Itt három sprite-ot hozunk létre: a játékost, az ellenséget és a kincset:

```python
player = GameSprite('hero.png', 20, 400, 4)  # Játékos sprite
enemy = GameSprite('cyborg.png', 600, 250, 2)  # Ellenség sprite
treasure = GameSprite('treasure.png', 600, 400, 0)  # Kincs sprite
```

- A játékos a **`hero.png`** képet használja, a bal alsó sarok közelében kezd (x=20, y=400), és sebessége 4.
- Az ellenség a **`cyborg.png`** képet használja, és a képernyő közepén helyezkedik el.
- A kincs a **`treasure.png`** képet használja, és a jobb alsó sarok közelében van.

#### 7. **Hang lejátszása kincs megszerzésekor**
Ha a játékos eléri a kincset, lejátszunk egy hangot:

```python
treasure_sound = mixer.Sound('money.ogg')
```

Ez a hang akkor játszódik le, ha a játékos és a kincs pozíciója átfedi egymást:

```python
if player.rect.colliderect(treasure.rect):
    treasure_sound.play()  # A hang lejátszása
```

A **`colliderect`** függvény azt ellenőrzi, hogy két sprite "ütközik-e" egymással, ebben az esetben a játékos és a kincs.

#### 8. **A játékmenet ciklusa**
Ez a rész felel a játék folyamatos futásáért:

```python
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
```

Ez a ciklus folyamatosan ellenőrzi, hogy van-e kilépési esemény (például, ha a felhasználó bezárja az ablakot).

A játék megjelenítése és frissítése is itt történik:

```python
window.blit(background, (0, 0))  # Háttér kirajzolása
player.reset()  # Játékos kirajzolása
enemy.reset()  # Ellenség kirajzolása
treasure.reset()  # Kincs kirajzolása

display.update()  # Képernyő frissítése
clock.tick(FPS)  # Játék sebességének korlátozása az FPS alapján
```

Ez biztosítja, hogy minden sprite frissüljön a képernyőn, a játék folyamatosan fusson és az FPS (60 képkocka/másodperc) szabályozza a sebességet.

### Összefoglalás:
- A kód egy egyszerű labirintus-játékot hoz létre, ahol a játékosnak el kell érnie a kincset.
- A sprite-ok (játékos, ellenség, kincs) a `GameSprite` osztályból származnak, és egyedi képekkel és pozíciókkal rendelkeznek.
- Amikor a játékos eléri a kincset, egy hangfájl játszódik le.
- A játék folyamatosan frissül, és a grafika újrarajzolódik minden képkocka során.

Ez a kód alapvető játékmenetet valósít meg a Pygame-ben, ahol különféle objektumokat (sprite-okat) kezelünk, háttérzenét játszunk, és interakciót biztosítunk a játékos és a kincs között.
