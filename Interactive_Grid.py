import pygame
import sys

WIDTH = 900
HEIGHT = 900
TAMANHO_PIXEL = 10

LINHAS = WIDTH // TAMANHO_PIXEL
COLUNAS = HEIGHT // TAMANHO_PIXEL

pygame.init()

tela = pygame.display.set_mode((WIDTH, HEIGHT))
tela.fill((200, 200, 200))

# criar grid
def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = [0] * colunas
        matriz.append(linha)
    return matriz

GRID = criar_matriz(linhas=LINHAS, colunas=COLUNAS)

def desenhar_grid(TAMANHO_PIXEL, WIDTH, HEIGHT, GRID):
    for x in range(0, WIDTH, TAMANHO_PIXEL):
        for y in range(0, HEIGHT, TAMANHO_PIXEL):
            retangulo = pygame.Rect(x, y, TAMANHO_PIXEL, TAMANHO_PIXEL)
            pygame.draw.rect(tela, (0, 0, 0), retangulo, 1)
            if GRID[y // TAMANHO_PIXEL][x // TAMANHO_PIXEL] == 1:
                pygame.draw.rect(tela, (0, 0, 0), retangulo)

# loop jogo
while True:
    desenhar_grid(TAMANHO_PIXEL=TAMANHO_PIXEL, WIDTH=WIDTH, HEIGHT=HEIGHT, GRID=GRID)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col, row = mouse_x // TAMANHO_PIXEL, mouse_y // TAMANHO_PIXEL
            GRID[row][col] = 1

    pygame.display.flip()
