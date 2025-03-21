import pygame

# Inicia o Pygame
pygame.init()

# Carrega a musica para em seguida tocar
pygame.mixer.music.load("error_music.mp3")
pygame.mixer.music.play()

# Mantém o programa rodando até a música terminar (Tive que pegar essa parte abaixo com o ChatGPT pois não estava rodando da maneira que vi na aula do Curso em Vídeo)
while pygame.mixer.music.get_busy():
    pygame.time.Clock()  # Pequeno delay para evitar alto uso da CPU
