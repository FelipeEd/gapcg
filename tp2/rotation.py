import numpy as np
import pygame
from quat import *
from cube import *
"""
OBS: Para rodar o programa é necessario instalar os pacotes numpy e pygame.

Implementar:

1. Multiplicação de quaternion usando 8 multiplicações de ponto flutuante.(implementado no arquivo quat.py)
2. Rotação usando quaternions.
3. Slerp.

"""
# Resolução da tela
width, height = 640, 640
max_x, max_y = width // 2, height // 2


def main():
    pygame.init()
    screen = pygame.display.set_mode([width, height])

    # Cubo ------------------------------------------------------

    # 0.5 é o tamanho do cubo considerarndo que a tela vai de  -1 a 1
    cube = Cube(0.5)
    eixo = [1, 1, 1]
    angulo_por_frame = 0.001
    # --------------------------------------------------------------------------
    running = True
    while running:
        # Cor do fundo da tela
        screen.fill((30, 30, 45))

        for event in pygame.event.get():
            # Detecta click em fechar
            if event.type == pygame.QUIT:
                running = False

        # Desenha o cubo
        cube.draw(screen)

        # A cada frame rotaciona o cubo por um eixo e angulo,
        # Desenhando na tela o eixo
        cube.rot(eixo, angulo_por_frame, screen)

        # Exibe informações
        myFont = pygame.font.SysFont("Times New Roman", 18)
        msg = myFont.render(
            f'Eixo {eixo[0]:.2f} {eixo[1]:.2f} {eixo[2]:.2f}  Angulo/s {angulo_por_frame}', 1, (255, 255, 255))
        screen.blit(msg, (0, 0))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
