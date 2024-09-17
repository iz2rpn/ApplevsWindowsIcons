import pygame
import random
import sys
import os

# Inizializza Pygame
pygame.init()

# Dimensioni della finestra
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Apple vs Windows Icons")  # Titolo della finestra

# Colori
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)

# Percorso della cartella delle icone
icon_folder = "img"

# Carica tutte le icone nella cartella come possibili nemici
enemy_icons = []
for filename in os.listdir(icon_folder):
    if filename.endswith(".png"):
        icon_path = os.path.join(icon_folder, filename)
        icon_image = pygame.image.load(
            icon_path
        ).convert_alpha()  # Carica con trasparenza
        enemy_icons.append(
            pygame.transform.scale(icon_image, (40, 40))
        )  # Ridimensiona le icone

# Carica l'icona Apple per l'astronave
apple_icon = pygame.image.load(os.path.join(icon_folder, "apple.png"))
apple_icon = pygame.transform.scale(apple_icon, (50, 50))

# Carica l'immagine del proiettile (puntatore del mouse)
bullet_icon = pygame.image.load(os.path.join(icon_folder, "mouse_pointer.png"))
bullet_icon = pygame.transform.scale(bullet_icon, (20, 20))

# Clock per controllare il frame rate
clock = pygame.time.Clock()

# Font per i testi
font = pygame.font.SysFont(None, 50)


# Classe per l'astronave (icona Apple)
class AppleShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = apple_icon  # Assegna l'immagine dell'icona Apple
        self.rect = self.image.get_rect(
            center=(WIDTH // 2, HEIGHT - 50)
        )  # Posiziona l'astronave
        self.speed = 5  # Velocità di movimento

    def update(self, keys):
        # Movimento a sinistra e a destra con le frecce
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        # Funzione per sparare un proiettile
        return Bullet(self.rect.centerx, self.rect.top)


# Classe per i proiettili (puntatori del mouse)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=-7):
        super().__init__()
        self.image = bullet_icon  # Immagine per il puntatore del mouse
        self.rect = self.image.get_rect(center=(x, y))  # Posiziona il proiettile
        self.speed = speed  # Velocità (possiamo usare anche valori positivi per nemici)

    def update(self):
        # Movimento del proiettile
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()  # Rimuove il proiettile se esce dallo schermo


# Classe per i nemici (icone random dalle icone suddivise)
class EnemyGroup:
    def __init__(self, enemies):
        self.enemies = enemies
        self.direction = 1  # 1: destra, -1: sinistra
        self.speed = 2  # Velocità di movimento
        self.move_down = False  # Determina se devono scendere

    def update(self):
        move_direction = self.direction * self.speed
        self.move_down = False
        for enemy in self.enemies:
            enemy.rect.x += move_direction
            if enemy.rect.right >= WIDTH or enemy.rect.left <= 0:
                self.direction = -self.direction
                self.move_down = True
                break

        if self.move_down:
            for enemy in self.enemies:
                enemy.rect.y += 40  # Scende di un livello

    def shoot(self):
        # Sceglie un nemico casuale per sparare
        shooting_enemy = random.choice(self.enemies)
        return Bullet(shooting_enemy.rect.centerx, shooting_enemy.rect.bottom, speed=5)

    def draw(self, screen):
        for enemy in self.enemies:
            screen.blit(enemy.image, enemy.rect)


# Funzione per il menu iniziale
def main_menu():
    while True:
        screen.fill(LIGHT_BLUE)  # Sfondo del menu
        title_text = font.render("Apple vs Windows Icons", True, WHITE)
        play_text = font.render("Premi INVIO per giocare", True, WHITE)

        # Posiziona il testo
        screen.blit(
            title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100)
        )
        screen.blit(
            play_text, (WIDTH // 2 - play_text.get_width() // 2, HEIGHT // 2 + 50)
        )

        pygame.display.flip()  # Aggiorna il display

        # Controlla se viene premuto INVIO per iniziare il gioco
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Inizia il gioco


# Funzione principale del gioco
def game():
    running = True
    direction = 1  # Direzione iniziale dei nemici (1 per destra, -1 per sinistra)
    score = 0  # Punteggio iniziale

    # Crea l'astronave (giocatore)
    player = AppleShip()
    player_group = pygame.sprite.GroupSingle(
        player
    )  # Gruppo contenente solo il giocatore

    bullets = pygame.sprite.Group()  # Gruppo per i proiettili del giocatore
    enemy_bullets = pygame.sprite.Group()  # Gruppo per i proiettili dei nemici
    enemies = pygame.sprite.Group()  # Gruppo per i nemici

    # Crea i nemici disposti in righe e colonne
    enemy_sprites = []
    for i in range(5):
        for j in range(8):
            enemy = pygame.sprite.Sprite()
            enemy.image = random.choice(enemy_icons)
            enemy.rect = enemy.image.get_rect(topleft=(100 + j * 60, 50 + i * 50))
            enemy_sprites.append(enemy)
    enemy_group = EnemyGroup(enemy_sprites)

    while running:
        screen.fill(LIGHT_BLUE)  # Sfondo blu chiaro

        # Eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_SPACE
                ):  # Spara un proiettile con la barra spaziatrice
                    bullets.add(player.shoot())

        # Aggiorna la posizione del giocatore e dei proiettili
        keys = pygame.key.get_pressed()
        player_group.update(keys)
        bullets.update()
        enemy_bullets.update()

        # Aggiorna la posizione dei nemici
        enemy_group.update()

        # Controllo delle collisioni tra proiettili e nemici
        for bullet in bullets:
            for enemy in enemy_group.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    bullet.kill()
                    enemy_group.enemies.remove(enemy)
                    score += 10  # Aumenta il punteggio

        # Se non ci sono più nemici, il giocatore ha vinto
        if len(enemy_group.enemies) == 0:
            running = False
            print("Hai vinto!")

        # I nemici sparano casualmente
        if (
            random.randint(1, 100) < 5
        ):  # Probabilità che un nemico spari (meno frequente) se no diventa modalità nightmare
            enemy_bullets.add(enemy_group.shoot())

        # Controllo delle collisioni tra i proiettili dei nemici e il giocatore
        if pygame.sprite.spritecollide(player, enemy_bullets, False):
            running = False
            print("Hai perso!")
            main_menu()

        # Disegna il punteggio
        score_text = font.render(f"Punteggio: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Disegna tutti gli sprite
        player_group.draw(screen)
        bullets.draw(screen)
        enemy_bullets.draw(screen)
        enemy_group.draw(screen)

        # Aggiorna il display
        pygame.display.flip()

        # Controlla se i nemici hanno raggiunto la parte inferiore dello schermo
        for enemy in enemy_group.enemies:
            if enemy.rect.bottom >= HEIGHT:
                running = False
                print("Hai perso!")
                main_menu()

        # Frame rate
        clock.tick(60)


if __name__ == "__main__":
    main_menu()  # Mostra il menu principale
    game()  # Avvia il gioco
    pygame.quit()  # Chiudi Pygame
    sys.exit()  # Chiudi da sys
