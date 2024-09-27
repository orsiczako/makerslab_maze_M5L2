from pygame import *

# GameSprite osztály meghatározása
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))  # Sprite mérete
        self.speed = player_speed
        self.rect = self.image.get_rect()  # Sprite pozíciója
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        # Sprite újrarajzolása a képernyőn
        window.blit(self.image, (self.rect.x, self.rect.y))

# Inicializálás
init()

# Ablak méretei
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")

# Háttérkép beállítása
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

# Zene inicializálás
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

# Óra és FPS beállítása
clock = time.Clock()
FPS = 60

# GameSprite példányok létrehozása
player = GameSprite('hero.png', 20, 400, 4)  # Játékos sprite
enemy = GameSprite('cyborg.png', 600, 250, 2)   # Ellenség sprite 
treasure = GameSprite('treasure.png', 600, 400, 0)  # Kincs sprite

# Hangfájl betöltése a kincs megszerzéséhez
treasure_sound = mixer.Sound('money.ogg')

# Játékmenet
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Háttér kirajzolása
    window.blit(background, (0, 0))
    
    # Sprite-ok kirajzolása
    player.reset()
    enemy.reset()
    treasure.reset()

    # Ellenőrizd, hogy a játékos elérte-e a kincset
    if player.rect.colliderect(treasure.rect):
        treasure_sound.play()  # Hang lejátszása, ha a játékos megszerzi a kincset

    # Képernyő frissítése
    display.update()
    
    # FPS beállítása
    clock.tick(FPS)
