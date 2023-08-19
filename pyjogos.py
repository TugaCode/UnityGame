import pygame
import random

pygame.init()

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 40
PLATFORM_HEIGHT = 10
SPIKE_SIZE = 20
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Definir cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Criar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity_y = 0
        self.jumping = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity_y = 0
            self.jumping = False

    def jump(self):
        if not self.jumping:
            self.velocity_y = JUMP_STRENGTH
            self.jumping = True

    def move(self, direction):
        self.rect.x += direction * 5

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.Surface((width, PLATFORM_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((SPIKE_SIZE, SPIKE_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
platforms = pygame.sprite.Group()
spikes = pygame.sprite.Group()

for i in range(10):
    platform = Platform(random.randint(0, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), random.randint(50, 150))
    platforms.add(platform)
    all_sprites.add(platform)

for i in range(5):
    spike = Spike(random.randint(0, SCREEN_WIDTH - SPIKE_SIZE), random.randint(100, SCREEN_HEIGHT - SPIKE_SIZE))
    spikes.add(spike)
    all_sprites.add(spike)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1)
    if keys[pygame.K_RIGHT]:
        player.move(1)

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits:
        player.rect.bottom = hits[0].rect.top
        player.velocity_y = 0

    spike_hits = pygame.sprite.spritecollide(player, spikes, False)
    if spike_hits:
        player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        player.velocity_y = 0
        player.jumping = False

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

