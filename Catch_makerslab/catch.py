# A pygame könyvtár importálása
import pygame
from pygame import *  # Minden pygame modult importálunk a könnyebb használat érdekében

# --- Ablak beállítások ---
# A játék ablakának méretének beállítása: 700 pixel széles és 500 pixel magas
window = display.set_mode((700, 500))
# Az ablak címének ("Catch") beállítása
display.set_caption("Catch")

# A háttérkép betöltése ("background.jpg") és annak méretezése az ablakhoz (700x500 pixel)
background = transform.scale(image.load("background.png"), (700, 500))

# --- Sprite-ok pozíciói és sebessége ---
# Első sprite (sprite1) kezdeti pozíciója. Ezek a változók (x1, y1) határozzák meg a sprite képernyőn való megjelenési helyét.
x1, y1 = 350, 250  # Sprite1 kezdeti pozíciója a képernyő közepén (350, 250)

# Második sprite (sprite2) kezdeti pozíciója. Ezek a változók (x2, y2) határozzák meg a sprite helyét.
x2, y2 = 100, 100  # Sprite2 kezdeti pozíciója (100, 100)

# A sprite-ok mozgási sebessége. Ez az érték határozza meg, hogy a sprite milyen gyorsan mozogjon a nyilak vagy gombok lenyomására.
speed = 7

# A játék futásának ellenőrzésére szolgáló változó. Amíg a `game` értéke True, a játék futni fog.
game = True

# --- Játék óra és FPS beállítások ---
# Egy Clock objektum létrehozása, amely a játék sebességének (FPS) vezérlésére szolgál
clock = time.Clock()

# A másodpercenkénti képkockaszám (FPS) beállítása 60-ra. Ez azt jelenti, hogy a játék 60 képkockát próbál megjeleníteni másodpercenként.
FPS = 60

# --- Fő játék ciklus ---
# A játék fő ciklusa, amely addig fut, amíg a játékos be nem zárja a játékot
while game:
    # A háttérkép másolása a képernyőre a (0, 0) pozícióban. Ez minden egyes képkocka előtt újrarajzolja a hátteret.
    window.blit(background, (0, 0))

    # --- Események kezelése ---
    # Ez a ciklus feldolgozza az összes eseményt (például billentyűleütéseket, egérmozgásokat, stb.)
    for e in event.get():
        # Ellenőrzi, hogy történt-e 'QUIT' esemény (például az ablak bezárása)
        if e.type == QUIT:
            game = False  # Ha a játékos bezárja az ablakot, a játék ciklus megáll

    # --- Billentyűk lenyomásának kezelése ---
    # Lekérdezi az összes billentyű állapotát, így ellenőrizhetjük, hogy melyik billentyűt nyomták meg
    keys_pressed = key.get_pressed()

    # --- Sprite1 mozgása (nyilak segítségével) ---
    # Ellenőrzi, hogy a bal nyíl lenyomva van-e, és hogy a sprite1 x1 pozíciója nagyobb-e, mint 5 (így nem megy ki a képernyőről balra)
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed  # Sprite1 balra mozgatása a sebesség kivonásával x1-ből

    # Ellenőrzi, hogy a jobb nyíl lenyomva van-e, és hogy a sprite1 x1 pozíciója kisebb-e, mint 595 (nem megy ki a képernyőről jobbra)
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed  # Sprite1 jobbra mozgatása a sebesség hozzáadásával x1-hez

    # Ellenőrzi, hogy a felfelé nyíl lenyomva van-e, és hogy a sprite1 y1 pozíciója nagyobb-e, mint 5 (így nem megy ki a képernyőről felfelé)
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed  # Sprite1 felfelé mozgatása a sebesség kivonásával y1-ből

    # Ellenőrzi, hogy a lefelé nyíl lenyomva van-e, és hogy a sprite1 y1 pozíciója kisebb-e, mint 395 (nem megy ki a képernyőről lefelé)
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed  # Sprite1 lefelé mozgatása a sebesség hozzáadásával y1-hez

    # --- Sprite2 mozgása (WASD gombok segítségével) ---
    # Ellenőrzi, hogy az 'A' gomb lenyomva van-e, és hogy a sprite2 x2 pozíciója nagyobb-e, mint 5 (nem megy ki balra a képernyőről)
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed  # Sprite2 balra mozgatása a sebesség kivonásával x2-ből

    # Ellenőrzi, hogy a 'D' gomb lenyomva van-e, és hogy a sprite2 x2 pozíciója kisebb-e, mint 595 (nem megy ki jobbra a képernyőről)
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed  # Sprite2 jobbra mozgatása a sebesség hozzáadásával x2-höz

    # Ellenőrzi, hogy a 'W' gomb lenyomva van-e, és hogy a sprite2 y2 pozíciója nagyobb-e, mint 5 (nem megy ki felfelé a képernyőről)
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed  # Sprite2 felfelé mozgatása a sebesség kivonásával y2-ből

    # Ellenőrzi, hogy az 'S' gomb lenyomva van-e, és hogy a sprite2 y2 pozíciója kisebb-e, mint 395 (nem megy ki lefelé a képernyőről)
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed  # Sprite2 lefelé mozgatása a sebesség hozzáadásával y2-höz

    # --- Sprite-ok kirajzolása ---
    # Sprite1 képének betöltése (sprite1.png), méretezése 100x100 pixelre, és kirajzolása az aktuális (x1, y1) pozícióban
    window.blit(transform.scale(image.load("sprite1.png"), (100, 100)), (x1, y1))

    # Sprite2 képének betöltése (sprite2.png), méretezése 100x100 pixelre, és kirajzolása az aktuális (x2, y2) pozícióban
    window.blit(transform.scale(image.load("sprite2.png"), (100, 100)), (x2, y2))

    # --- Képernyő frissítése ---
    # Az ablak tartalmának frissítése, hogy a változások megjelenjenek a képernyőn
    display.update()

    # --- Képkockaszám beállítása ---
    # A játék sebességének (FPS) szabályozása, hogy másodpercenként legfeljebb 60 képkockát jelenítsen meg. Ha túl gyors lenne a játék, ez lassítja.
    clock.tick(FPS)
