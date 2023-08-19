import pygame

# inicialização do Pygame
pygame.init()

# Definição das dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definição das dimensões do quadrado
SQUARE_SIZE = 50
player_rect = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)

# Definição da posição inicial do jogador
player_rect.centerx = SCREEN_WIDTH / 2
player_rect.centery = SCREEN_HEIGHT / 2

# Definição da velocidade de movimento do jogador
PLAYER_SPEED = 2.8

# Loop principal do jogo
while True:
    # Tratamento dos eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Verificação das teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.centery -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player_rect.centery += PLAYER_SPEED
    if keys[pygame.K_a]:
        player_rect.centerx -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player_rect.centerx += PLAYER_SPEED

    # Atualização da posição da câmera
    camera_x = player_rect.centerx - SCREEN_WIDTH / 2
    camera_y = player_rect.centery - SCREEN_HEIGHT / 2

    # Limitação da posição da câmera
    if camera_x < 0:
        camera_x = 0
    if camera_y < 0:
        camera_y = 0
    if camera_x > SCREEN_WIDTH - SQUARE_SIZE:
        camera_x = SCREEN_WIDTH - SQUARE_SIZE
    if camera_y > SCREEN_HEIGHT - SQUARE_SIZE:
        camera_y = SCREEN_HEIGHT - SQUARE_SIZE

    worldx = 960
    worldy = 720
    def gravity(self):
        self.movey += 3.2 # how fast player falls
        
        if self.rect.y > worldy and self.movey >= 0:
            self.movey = 0
            self.rect.y = worldy
    

    # Renderização do quadrado e da tela
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_rect.move(-camera_x, -camera_y))
    pygame.display.flip()

