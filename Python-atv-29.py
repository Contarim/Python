import pygame
import random

# Inicializar o Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pegue a Bolinha")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Configurações do jogador
player_size = 50
player_color = BLACK
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Configurações da bolinha
ball_size = 20
ball_color = RED
ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
ball_y = random.randint(0, SCREEN_HEIGHT - ball_size)

# Pontuação
score = 0
font = pygame.font.SysFont("Arial", 24)

# Função para desenhar o jogador
def draw_player(x, y):
    pygame.draw.rect(screen, player_color, (x, y, player_size, player_size))

# Função para desenhar a bolinha
def draw_ball(x, y):
    pygame.draw.circle(screen, ball_color, (x, y), ball_size)

# Função para exibir a pontuação
def display_score(score):
    score_text = font.render(f"Pontos: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Função para exibir uma mensagem de fim de jogo
def display_game_over():
    game_over_text = font.render("Parabéns! Você atingiu 10 pontos!", True, BLACK)
    retry_text = font.render("Pressione 'R' para jogar novamente ou 'S' para sair.", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

# Loop principal do jogo
def game_loop():
    global score, player_x, player_y, ball_x, ball_y
    score = 0
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
    ball_y = random.randint(0, SCREEN_HEIGHT - ball_size)

    running = True
    while running:
        screen.fill(WHITE)
        
        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentos do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - player_size:
            player_y += player_speed
        
        # Verificar colisão com a bolinha
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
        if player_rect.colliderect(ball_rect):
            score += 1
            ball_x = random.randint(0, SCREEN_WIDTH - ball_size)
            ball_y = random.randint(0, SCREEN_HEIGHT - ball_size)
        
        # Verificar se a pontuação atingiu 10
        if score >= 3:
            display_game_over()
            pygame.display.update()

            # Esperar o jogador pressionar 'R' para reiniciar ou 'Q' para sair
            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting_for_input = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:  # Sair do jogo
                            running = False
                            waiting_for_input = False
                        elif event.key == pygame.K_r:  # Jogar novamente
                            game_loop()  # Reinicia o jogo

            break
        
        # Desenhar o jogador e a bolinha
        draw_player(player_x, player_y)
        draw_ball(ball_x, ball_y)
        
        # Exibir a pontuação
        display_score(score)
        
        # Atualizar a tela
        pygame.display.update()
        
        # Controlar a taxa de atualização
        pygame.time.Clock().tick(60)

# Iniciar o jogo
game_loop()

# Finalizar o Pygame
pygame.quit()
