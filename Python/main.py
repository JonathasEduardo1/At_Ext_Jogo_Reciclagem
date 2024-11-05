import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Vamos reciclar?")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Carregar imagem de fundo
background_img = pygame.image.load('background.png')

# Carregar imagens das lixeiras
lixeira_papel_img = pygame.image.load('lixeira_papel.png')
lixeira_plastico_img = pygame.image.load('lixeira_plastico.png')
lixeira_vidro_img = pygame.image.load('lixeira_vidro.png')
lixeira_metal_img = pygame.image.load('lixeira_metal.png')
lixeira_organico_img = pygame.image.load('lixeira_organico.png')

# Carregar imagens dos itens de lixo
imagens_lixo = {
    "papel": pygame.image.load('papel.png'),
    "plastico": pygame.image.load('plastico.png'),
    "vidro": pygame.image.load('vidro.png'),
    "metal": pygame.image.load('metal.png'),
    "organico": pygame.image.load('organico.png')
}

# Posições das lixeiras
lixeiras = {
    "papel": pygame.Rect(75, 400, 50, 50),
    "plastico": pygame.Rect(175, 400, 50, 50),
    "vidro": pygame.Rect(275, 400, 50, 50),
    "metal": pygame.Rect(375, 400, 50, 50),
    "organico": pygame.Rect(475, 400, 50, 50)
}

# Lista de itens de lixo
itens_lixo = ["papel", "plastico", "vidro", "metal", "organico"]

# Função para desenhar o lixo
def draw_trash(trash_pos, trash_type):
    screen.blit(imagens_lixo[trash_type], (trash_pos[0], trash_pos[1]))

# Função para desenhar o botão
def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.SysFont('arial', 35)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    score = 0
    message = ""
    message_timer = 0

    # Gerar posição inicial do lixo no topo da tela
    trash_pos = [random.randrange(1, 40) * 20, 0]
    trash_type = random.choice(itens_lixo)

    font = pygame.font.SysFont('arial', 25)

    # Definir o botão de encerrar
    button_rect = pygame.Rect(650, 20, 120, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    trash_pos[1] -= 30
                elif event.key == pygame.K_DOWN:
                    trash_pos[1] += 30
                elif event.key == pygame.K_LEFT:
                    trash_pos[0] -= 30
                elif event.key == pygame.K_RIGHT:
                    trash_pos[0] += 30
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Verificar se o lixo foi entregue na lixeira correta
        for lixeira, rect in lixeiras.items():
            if rect.collidepoint(trash_pos):
                if lixeira == trash_type:
                    score += 1
                    message = "PARABÉNS! Você reciclou corretamente!!!"
                    
                else:
                    message = "Esta não é a lixeira correta, mais atenção na próxima!"
                    
                message_timer = pygame.time.get_ticks()
                trash_pos = [random.randrange(1, 40) * 20, 0]
                trash_type = random.choice(itens_lixo)

        # Desenhar na tela
        screen.blit(background_img, (0, 0))  # Desenhar o fundo
        draw_trash(trash_pos, trash_type)

        # Desenhar lixeiras
        screen.blit(lixeira_papel_img, lixeiras["papel"])
        screen.blit(lixeira_plastico_img, lixeiras["plastico"])
        screen.blit(lixeira_vidro_img, lixeiras["vidro"])
        screen.blit(lixeira_metal_img, lixeiras["metal"])
        screen.blit(lixeira_organico_img, lixeiras["organico"])

        # Mostrar pontuação
        score_text = font.render(f'Pontuação: {score}', True, BLACK)
        screen.blit(score_text, [0, 0])

        # Mostrar mensagem de feedback
        if message:
            message_text = font.render(message, True, RED)
            screen.blit(message_text, [50, 50])
            if pygame.time.get_ticks() - message_timer > 4000:  # Mostrar por 4 segundos
                message = ""

        # Desenhar o botão de encerrar
        draw_button("Encerrar", button_rect, RED)

        pygame.display.flip()
        clock.tick(50)

if __name__ == "__main__":
    main()
